#!/usr/bin/env python3

import csv

# 要写入的数据
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles']
]

# 打开 CSV 文件
with open('output.csv', mode='w', encoding='utf-8', newline='') as file:
    # 创建 csv.writer 对象
    csv_writer = csv.writer(file)

    # 写入数据
    for row in data:
        csv_writer.writerow(row)

# 打开 CSV 文件
with open('output.csv', mode='r', encoding='utf-8') as file:
    # 创建 csv.reader 对象
    csv_reader = csv.reader(file)

    # 逐行读取数据
    for row in csv_reader:
        print(row)

# with open('data.csv', mode='r', encoding='utf-8') as file:
#     csv_dict_reader = csv.DictReader(file)
#
#     for row in csv_dict_reader:
#         print(row)

data = [
    {'Name': 'Alice', 'Age': '30', 'City': 'New York'},
    {'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles'}
]

with open('output.csv', mode='w', encoding='utf-8', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    csv_dict_writer = csv.DictWriter(file, fieldnames=fieldnames)

    # 写入表头
    csv_dict_writer.writeheader()

    # 写入数据
    for row in data:
        csv_dict_writer.writerow(row)

data = [['Name', 'Age'], ['Alice', 25], ['Bob', 30]]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # 写入多行

# 读取
with open('output.csv', 'r') as file:
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        print(row['Name'], row['Age'])  # 通过字段名访问

# 写入
fieldnames = ['Name', 'Age']
with open('output.csv', 'w', newline='') as file:
    dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    dict_writer.writeheader()  # 写入表头
    dict_writer.writerow({'Name': 'Alice', 'Age': 25})





