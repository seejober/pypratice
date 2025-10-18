#!   /usr/bin/env python3

import numpy as np

a = np.arange(24)
print(a.ndim)  # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
print(b.ndim)

a = np.array([[1,2,3],[4,5,6]])
print (a.shape)

a = np.array([[1,2,3],[4,5,6]])
a.shape =  (3,2)
print (a)

# 数组的 dtype 为 int8（一个字节）
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)

# 数组的 dtype 现在为 float64（八个字节）
y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(y.itemsize)
x = np.array([1,2,3,4,5])
print (x.flags)

x=np.empty((3,2),dtype = int)
print(x)

# 默认为浮点数
x = np.zeros(5)
print(x)

# 设置类型为整数
y = np.zeros((5,), dtype=int)
print(y)

# 自定义类型
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z)

# 默认为浮点数
x = np.ones(5)
print(x)

# 自定义类型
x = np.ones([2, 2], dtype=int)
print(x)

# 创建一个 3x3 的二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 创建一个与 arr 形状相同的，所有元素都为 0 的数组
zeros_arr = np.zeros_like(arr)
print(zeros_arr)

# 创建一个 3x3 的二维数组
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 创建一个与 arr 形状相同的，所有元素都为 1 的数组
ones_arr = np.ones_like(arr)
print(ones_arr)

x =  [1,2,3]
a = np.asarray(x)
print (a)

x =  (1,2,3)
a = np.asarray(x)
print (a)

x =  [(1,2,3),(4,5,6)]
a = np.asarray(x)
print (a)

x =  [1,2,3]
a = np.asarray(x, dtype =  float)
print (a)

s =  b'Hello World'
a = np.frombuffer(s, dtype =  'S1')
print (a)

# 使用 range 函数创建列表对象
list = range(5)
it = iter(list)

# 使用迭代器创建 ndarray
x = np.fromiter(it, dtype=float)
print(x)

x = np.arange(5)
print (x)

# 设置了 dtype
x = np.arange(5, dtype =  float)
print (x)

x = np.arange(10,20,2)
print (x)

a = np.linspace(1,10,10)
print(a)

a = np.linspace(1,1,10)
print(a)

a = np.linspace(10, 20,  5, endpoint =  False)
print(a)

a = np.linspace(1, 10, 10, retstep=True)
print(a)
# 拓展例子
b = np.linspace(1, 10, 10).reshape([10, 1])
print(b)
# 默认底数是 10
a = np.logspace(1.0,  2.0, num =  10)
print (a)

a = np.logspace(0,9,10,base=2)
print (a)
a = np.arange(10)
s = slice(2,7,2)   # 从索引 2 开始到索引 7 停止，间隔为2
print (a[s])

a = np.arange(10)
b = a[2:7:2]   # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)
a = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
b = a[5]
print(b)

a = np.arange(10)
print(a[2:])
a = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
print(a[2:5])
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)
# 从某个索引处开始切割
print('从数组索引 a[1:] 处开始切割')
print(a[1:])

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print (a[...,1])   # 第2列元素
print (a[1,...])   # 第2行元素
print (a[...,1:])  # 第2列及剩下的所有元素
x = np.array([[1,  2],  [3,  4],  [5,  6]])
y = x[[0,1,2],  [0,1,0]]
print (y)
x = np.array([[0,  1,  2],[3,  4,  5],[6,  7,  8],[9,  10,  11]])
print ('我们的数组是：' )
print (x)
print ('\n')
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[rows,cols]
print  ('这个数组的四个角元素是：')
print (y)














