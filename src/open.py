#!/usr/bin/env python3

# 打开一个文件
f = open("./foo.txt", "w+",encoding="utf-8")

n=f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n")
print(n)
# 关闭打开的文件
f.close()

f = open("./foo.txt", "r+",encoding="utf-8")

strs = f.read()
print(strs)

# 关闭打开的文件
f.close()

# 打开一个文件
f = open("./foo.txt", "r",encoding="utf-8")

s = f.readline()
print(s)
# 关闭打开的文件
f.close()

# 打开一个文件
f = open("./foo.txt", "r",encoding="utf-8")

strs = f.readlines()
print(strs)

# 关闭打开的文件
f.close()

# 打开一个文件
f = open("./foo.txt", "r",encoding="utf-8")

for line in f:
    print(line, end='')

# 关闭打开的文件
f.close()

# 打开一个文件
f = open("./foo1.txt", "w",   encoding="utf-8")

value = ('www.runoob.com', 14)
st = str(value)
f.write(st)

# 关闭打开的文件
f.close()
f = open('./foo.txt', 'rb+')
n=f.write(b'0123456789abcdef')
print(n)
n = f.seek(5)
print(n)

print(f.read(1))
# 关闭打开的文件
f.close()
with open('./foo.txt', 'r', encoding='utf-8') as f:
    s = f.readline()
    print(s)

