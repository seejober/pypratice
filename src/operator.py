#!/usr/bin/env python3

# 导入 operator 模块
import operator

# 数字
x = 10
y = 20

print("x:", x, ", y:", y)
print("operator.lt(x,y): ", operator.lt(x, y))
print("operator.gt(y,x): ", operator.gt(y, x))
print("operator.eq(x,x): ", operator.eq(x, x))
print("operator.ne(y,y): ", operator.ne(y, y))
print("operator.le(x,y): ", operator.le(x, y))
print("operator.ge(y,x): ", operator.ge(y, x))
print()

# 字符串
x = "Google"
y = "Runoob"

print("x:", x, ", y:", y)
print("operator.lt(x,y): ", operator.lt(x, y))
print("operator.gt(y,x): ", operator.gt(y, x))
print("operator.eq(x,x): ", operator.eq(x, x))
print("operator.ne(y,y): ", operator.ne(y, y))
print("operator.le(x,y): ", operator.le(x, y))
print("operator.ge(y,x): ", operator.ge(y, x))
print()

# 查看返回值
print("type((operator.lt(x,y)): ", type(operator.lt(x, y)))

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))




