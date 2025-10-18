#!/usr/bin/python3

a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)#2.1

c = a % b
print("5 - c 的值为：", c)#1

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("6 - c 的值为：", c)#8

a = 10
b = 5
c = a // b
print("7 - c 的值为：", c)#2

a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)#31

c += a
print("2 - c 的值为：", c)#52

c *= a
print("3 - c 的值为：", c)#1092

c /= a
print("4 - c 的值为：", c)#52.0

c = 2
c %= a
print("5 - c 的值为：", c)#2

c **= a
print("6 - c 的值为：", c)#2097152

c //= a
print("7 - c 的值为：", c)#99864