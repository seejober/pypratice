#!/usr/bin/python3

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值




x = bytes("hello", encoding="utf-8")
print(x)

x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
print(y)
z = x + b"world"  # 拼接操作，得到 b"helloworld"
print(z)

x = b"hello"
if x[0] == ord("h"):
    print("The first element is 'h'")

    # 使用大括号 {} 来创建空字典
emptyDict = {}

# 打印字典
print(emptyDict)

# 查看字典的数量
print("Length:", len(emptyDict))

# 查看类型
print(type(emptyDict))


# emptyDict = dict()

# 打印字典
print(emptyDict)

# 查看字典的数量
print("Length:", len(emptyDict))

# 查看类型
print(type(emptyDict))

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("tinydict['Name']: ", tinydict['Name'])
print("tinydict['Age']: ", tinydict['Age'])

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

tinydict['Age'] = 8  # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息

print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del tinydict['Name']  # 删除键 'Name'
tinydict.clear()  # 清空字典
del tinydict  # 删除字典

# print("tinydict['Age']: ", tinydict['Age'])
# print("tinydict['School']: ", tinydict['School'])

tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}

print("tinydict['Name']: ", tinydict['Name'])

