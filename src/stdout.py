#!/usr/bin/python3
import sys

x = 'runoob'
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
sys.stdout.write(x + '\n')

y = 'mm'
z = 'nn'

print( y )
print( z )
print( y,end="" )
print( z,end="" )
print( z )
m = "Hello Eric, would you like to learn some Python today?"
print(m)