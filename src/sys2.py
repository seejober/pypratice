#!/usr/bin/env python3

import sys


print("程序开始")



print("Python 版本:", sys.version)
print("版本信息:", sys.version_info)

print("模块搜索路径:", sys.path)
sys.path.append('/custom/path')
print("更新后的模块搜索路径:", sys.path)

# 重定向标准输出到文件
with open('output.txt', 'w') as f:
    sys.stdout = f
    print("这行内容将写入 output.txt")

# 恢复标准输出
sys.stdout = sys.__stdout__
print("这行内容将显示在控制台")

sys.exit(0)
print("这行代码不会执行")