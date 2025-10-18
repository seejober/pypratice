#!/usr/bin/env python3
import pickle


# 创建一个 Python 对象
data2 = {
    'name': 'Alice',
    'age': 25,
    'hobbies': ['reading', 'traveling']
}

# 将对象序列化并保存到文件
with open('data.pkl', 'wb') as file:
    pickle.dump(data2, file)


with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()

import pprint, pickle

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getstate__(self):
        # 自定义序列化逻辑
        return {'name': self.name, 'age': self.age}

    def __setstate__(self, state):
        # 自定义反序列化逻辑
        self.name = state['name']
        self.age = state['age']

# 创建对象并序列化
person = Person('Bob', 30)
with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)

# 反序列化对象
with open('person.pkl', 'rb') as file:
    loaded_person = pickle.load(file)

print(loaded_person.name, loaded_person.age)