#!/usr/bin/env python3

from io import StringIO

# 创建 StringIO 对象
string_io = StringIO()

# 写入数据
string_io.write("Python is awesome!\n")
string_io.write("StringIO is useful!")

# 移动指针到开头
string_io.seek(0)

# 读取数据
print(string_io.read())

# 关闭 StringIO 对象
string_io.close()

# 创建一个 StringIO 对象
string_io = StringIO()

# 写入字符串
string_io.write("Hello, World!\n")
string_io.write("This is a test.")

# 移动文件指针到开头
string_io.seek(0)

# 读取内容
content = string_io.read()
print(content)

# 获取所有内容
value = string_io.getvalue()
print(value)

# 关闭 StringIO 对象
string_io.close()