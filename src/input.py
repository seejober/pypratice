#!/usr/bin/env python3

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    print(repr(x * x * x).rjust(4))

    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))




print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

print('{1} 和 {0}'.format('Google', 'Runoob'))

print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
import math

print('常量 PI 的值近似为： {}。'.format(math.pi))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}

for name, number in table.items():
     print('{0:10} ==> {1:10d}'.format(name, number))

print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
print('常量 PI 的值近似为：%5.3f。' % math.pi)

print('常量 PI 的值近似为：{:.3f}' .format(math.pi))






