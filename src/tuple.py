#!/usr/bin/python3

def myTest(tuple):
    print(tuple)

if __name__== "__main__":
    tuple = ('a','b','c','d','e','f','g')
    print(tuple[0])
    print(tuple[1:5])
    myTest(tuple)
    print(tuple)

    tup1 = ()  # 空元组
    tup2 = (20,)  # 一个元素，需要在元素后添加逗号