#!/usr/bin/env python3
import zlib
s = b'witch which has which witches wrist watch'

print(len(s))

t = zlib.compress(s)
print(len(t))

n = zlib.decompress(t)
print(n)
m=zlib.crc32(s)
print(m)

from timeit import Timer

print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())







