#!/usr/bin/python3

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

print("datatype of num_new:", isinstance(num_new, float))


class A:
    pass


class B(A):
    pass


print("isinstance(A(), A):", isinstance(A(), A))

print("type(A()) == A:", type(A()) == A)

print("isinstance(B(), A):", isinstance(B(), A))

print("type(B()) == A:", type(B()) == A)

print("issubclass(bool, int):", issubclass(bool, int))

print("True==1:", True == 1)

print("False==0:", False == 0)

print("True+1:", True + 1)

print("False+0:", False + 0)

# print("1 is True:",1 is True)

# print("0 is False:",0 is False)

var1 = 1
var2 = 10
del var2
print("var1:", var1)
# print("var2:",var2)
print("17 / 3:", 17 / 3)  # 浮点

print("17 // 3:", 17 // 3)  # 整数
print("17 % 3:", 17 % 3)

print("2**5:", 2 ** 5)
