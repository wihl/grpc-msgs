#!/usr/bin/env python3

from concurrent import futures
import time
import logging
import binascii
from random import choice
from string import ascii_uppercase
import os
import sys

import grpc

import route_guide_pb2
import route_guide_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

TBL = bytes.maketrans(bytearray(range(256)),
                      bytearray([ord(b'A') + b % 26 for b in range(256)]))

def fast_random_string(num_bytes):
    return os.urandom(num_bytes).translate(TBL)

def toSigned32(n):
    """https://stackoverflow.com/a/37095855"""
    n = n & 0xffffffff
    return (n ^ 0x80000000) - 0x80000000

class RouteGuideServicer(route_guide_pb2_grpc.RouteGuideServicer):
    """Provides methods that implement functionality of route guide server."""

    def GenRepeated(self, request, context):
        bytes_per_row = request.bytes_per_row
        num_rows = request.num_rows
        print("Repeated: requested bytes per row", bytes_per_row,
              "num rows", num_rows)

        resp = []
        for i in range(num_rows):
            row = fast_random_string(bytes_per_row)
            # In Python 3, crc32 returns an unsigned
            # https://docs.python.org/3/library/binascii.html
            crc = toSigned32(binascii.crc32(row))
            # Check that CRC is working - randomly put in a bad value
            # if i % 100 == 0:
            #     crc = -1
            resp.append(route_guide_pb2.StreamResponse(row=row, crc=crc))
        return route_guide_pb2.UniaryResponse(msg=resp)

    def GenStream(self, request, context):
        bytes_per_row = request.bytes_per_row
        num_rows = request.num_rows
        print("Streamed: requested bytes per row", bytes_per_row,
              "num rows", num_rows)
        for i in range(num_rows):
            row = fast_random_string(bytes_per_row)
            # In Python 3, crc32 returns an unsigned
            # https://docs.python.org/3/library/binascii.html
            crc = toSigned32(binascii.crc32(row))
            # Check that CRC is working - randomly put in a bad value
            # if i % 100 == 0:
            #     crc = -1
            resp_row = route_guide_pb2.StreamResponse(row=row, crc=crc)
            yield resp_row


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    route_guide_pb2_grpc.add_RouteGuideServicer_to_server(
        RouteGuideServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
