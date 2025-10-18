#!/usr/bin/env python3
import hashlib

sha256_hash = hashlib.new('sha256')
sha256_hash.update(b'RUNOOB')
print(sha256_hash.hexdigest())
md5_hash = hashlib.md5(b'RUNOOB')
print(md5_hash.hexdigest())

sha256_hash = hashlib.sha256()
sha256_hash.update(b'Hello, ')
sha256_hash.update(b'Runoob!')
print(sha256_hash.hexdigest())

md5_hash = hashlib.md5(b'RUNOOB')
print(md5_hash.hexdigest())

sha1_hash = hashlib.sha1(b'RUNOOB')
print(sha1_hash.digest())

md5_hash = hashlib.md5(b'RUNOOB')
print(md5_hash.hexdigest())

sha1_hash = hashlib.sha1(b'RUNOOB')
print(sha1_hash.hexdigest())

sha256_hash = hashlib.sha256(b'RUNOOB')
print(sha256_hash.hexdigest())

sha512_hash = hashlib.sha512(b'RUNOOB')
print(sha512_hash.hexdigest())



