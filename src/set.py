#!/usr/bin/python3

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu','Runoob'}

print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')


# set可以进行集合运算
a = set('abracadabra') #arcbd
b = set('alacazam') # alczm

print("a:",a)

print("b:",b)

print(a - b)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素

a = {x for x in 'abracadabra' if x not in 'abc'}
print("a:",a)

thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
thisset.update({1,3})
print(thisset)
thisset.update([1,4],[5,6])
print(thisset)
thisset.remove("Taobao")
print(thisset)
thisset.discard( "Runoob" )
thisset.discard( "xxxx" )
print(thisset)
x = thisset.pop()
print(x)
print(thisset)

print("Runoob" in thisset)
thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
x = thisset.pop()

print(x)

thisset.clear()
print(thisset)