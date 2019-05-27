from __future__ import print_function

import logging
import binascii
import time
import argparse

import grpc

import route_guide_pb2
import route_guide_pb2_grpc

def gen_repeated(stub, bytes_per_row, num_rows, show_progress):
    stream_desc = route_guide_pb2.StreamDesc(
        bytes_per_row=bytes_per_row,
        num_rows=num_rows)
    if show_progress:
        print(" %d bytes per row, %d rows" % (bytes_per_row, num_rows))
    i = 1
    for msg in stub.GenRepeated(stream_desc).msg:
        local_crc = binascii.crc32(msg.row)
        sent_crc = msg.crc
        if local_crc != sent_crc:
            print("row %d CRCs don't match: local %d, remote %d" %
                  (i, local_crc, sent_crc))
        i += 1

def gen_stream(stub, bytes_per_row, num_rows, show_progress):
    stream_desc = route_guide_pb2.StreamDesc(
        bytes_per_row=bytes_per_row,
        num_rows=num_rows)
    print(" %d bytes per row, %d rows" % (bytes_per_row, num_rows))

    i = 1
    for msg in stub.GenStream(stream_desc):
        local_crc = binascii.crc32(msg.row)
        sent_crc = msg.crc
        if local_crc != sent_crc:
            print("row %d CRCs don't match: local %d, remote %d" %
                  (i, local_crc, sent_crc))
        if show_progress:
            if i % 1000 == 0:
                print("%04d" % i)
        i += 1

def run(bytes_per_row, num_rows, max_msg, pagesize):
    options = [('grpc.max_receive_message_length', max_msg)]
    with grpc.insecure_channel('localhost:50052', options=options) as channel:
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)

        ### Repeat messages
        # Message sizes over 1 GB seem to break
        if max_msg < (1024 * 1024 * 1024):
            print("-------------- call repeated --------------")
            start = time.time()
            gen_repeated(stub, bytes_per_row, num_rows, True)
            print("elapsed time:", time.time() - start)
        else:
            print("Message size too large; skipping repeat rows.")

        ### Simulated paging
        if pagesize > 0:
            print("-------------- call paging ----------------")
            num_pages = num_rows / pagesize
            last_page = num_rows % pagesize
            print ("Number of pages: %d" % (num_pages +
                                            (1 if last_page > 0 else 0)))
            start = time.time()
            for i in range(num_pages):
                gen_repeated(stub, bytes_per_row, pagesize, False)
            if last_page > 0:
                gen_repeated(stub, bytes_per_row, last_page, False)
            print("elapsed time:", time.time() - start)

        ### Streaming
        print("-------------- call stream ----------------")
        start = time.time()
        gen_stream(stub, bytes_per_row, num_rows, True)
        print("elapsed time:", time.time() - start)


if __name__ == '__main__':
    logging.basicConfig()
    parser = argparse.ArgumentParser(
        description='Compare times for gRPC responses.')
    parser.add_argument('-b', '--bytes_per_row', type=int, default=10240,
                        help='Number of bytes per row')
    parser.add_argument('-n', '--num_rows', type=int, default=200,
                        help='Number of rows')
    parser.add_argument('-m', '--max_message', type=int, default=1024*1024*8,
                        help='Maximum message size')
    parser.add_argument('-p', '--pagesize', type=int, default=0,
                        help='Simulate paging using specified page size')

    args = parser.parse_args()
    max_message = args.max_message
    if max_message >= 0:
        if max_message < (args.num_rows * (args.bytes_per_row + 16)):
            print("WARNING: Max message size likely too low. Try %d\n\n"
                  % (args.num_rows * (args.bytes_per_row + 16)))
    else:
        max_message = -1
    run(args.bytes_per_row, args.num_rows, max_message, args.pagesize)
