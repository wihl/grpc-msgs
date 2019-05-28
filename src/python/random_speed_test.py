#!/usr/bin/env python3

from random import choice
from string import ascii_uppercase
import time
import os
import sys
import binascii


N_CHAR=10240
ITER=1000

# start = time.time()
# for i in range(ITER):
#     row = ''.join(choice(ascii_uppercase) for j in range(N_CHAR))
# print("join choice elapsed time:", time.time() - start)
#
# start = time.time()
# min_lc = ord(b'A')
# len_lc = 26
# for i in range(ITER):
#     ba = bytearray(os.urandom(N_CHAR))
#     for i, b in enumerate(ba):
#         ba[i] = min_lc + b % len_lc
#     row = ba
# print("bytearray elapsed time:", time.time() - start)

# From https://stackoverflow.com/questions/16308989/fastest-method-to-generate-big-random-string-with-lower-latin-letters
# (modified for uppercase)
start = time.time()
tbl = bytes.maketrans(bytearray(range(256)),
                      bytearray([ord(b'A') + b % 26 for b in range(256)]))
row = os.urandom(N_CHAR).translate(tbl)
print("translation elapsed time:", time.time() - start)
print (type(row))

print(binascii.crc32(row))
