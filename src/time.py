#!/usr/bin/env python3

import time  # 引入time模块
import os


ticks = time.time()
print ("当前时间戳为:", ticks)

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)

print("time.asctime(t): %s " % time.asctime(localtime))

localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

print("time.altzone %d " % time.altzone)

print ("time.ctime() : %s" % time.ctime())

print ("gmtime :", time.gmtime(1455508609.34375))

print ("localtime(): ", time.localtime(1455508609.34375))

import time

t = (2016, 2, 17, 17, 3, 38, 1, 48, 0)
secs = time.mktime( t )
print ("time.mktime(t) : %f" %  secs)
print ("asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)))

print ("Start : %s" % time.ctime())
time.sleep( 1 )
print ("End : %s" % time.ctime())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

struct_time = time.strptime("30 Nov 00", "%d %b %y")
print ("返回元组: ", struct_time)

# os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
# time.tzset()
# print(time.strftime('%X %x %Z'))
#
# os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
# time.tzset()
# print(time.strftime('%X %x %Z'))

scale = 50
print("执行开始".center(scale//2,"-"))  # .center() 控制输出的样式，宽度为 25//2，即 22，汉字居中，两侧填充 -

start = time.perf_counter() # 调用一次 perf_counter()，从计算机系统里随机选一个时间点A，计算其距离当前时间点B1有多少秒。当第二次调用该函数时，默认从第一次调用的时间点A算起，距离当前时间点B2有多少秒。两个函数取差，即实现从时间点B1到B2的计时功能。
for i in range(scale+1):
    a = '*' * i             # i 个长度的 * 符号
    b = '.' * (scale-i)  # scale-i） 个长度的 . 符号。符号 * 和 . 总长度为50
    c = (i/scale)*100  # 显示当前进度，百分之多少
    dur = time.perf_counter() - start    # 计时，计算进度条走到某一百分比的用时
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')  # \r用来在每次输出完成后，将光标移至行首，这样保证进度条始终在同一行输出，即在一行不断刷新的效果；{:^3.0f}，输出格式为居中，占3位，小数点后0位，浮点型数，对应输出的数为c；{}，对应输出的数为a；{}，对应输出的数为b；{:.2f}，输出有两位小数的浮点数，对应输出的数为dur；end=''，用来保证不换行，不加这句默认换行。
    time.sleep(0.1)     # 在输出下一个百分之几的进度前，停止0.1秒
print("\n"+"执行结果".center(scale//2,'-'))

