#!/usr/bin/env python3

from datetime import datetime

# 获取当前日期和时间
a = 3.1415926
print(f"a:%.2f" % a)

now = datetime.now()
print(f"当前时间: %.19s" % now)

# 创建特定的日期和时间
specific_time = datetime(2025, 4, 22, 15, 30, 0)
print("特定时间:", specific_time)

# 获取当前时间
now = datetime.now()

# 格式化输出
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("格式化时间:", formatted_time)

from datetime import timedelta,date
# 获取当前时间
now = datetime.now()

# 计算 10 天后的时间
future_time = now + timedelta(days=10)
print("10 天后的时间:", future_time)

# 创建两个日期
date1 = date(2025, 4, 22)
date2 = date(2025, 5, 1)

# 计算天数差
delta = date2 - date1
print("两个日期之间的天数差:", delta.days)

from datetime import datetime
# import pytz

# 获取当前时间并设置时区
# now = datetime.now(pytz.timezone('Asia/Shanghai'))
# print("上海当前时间:", now)

d1 = date(2023, 5, 15)
d2 = date(2023, 6, 1)
delta = d2 - d1  # 返回 timedelta 对象
print(delta.days)  # 输出: 17

now = datetime.now()
future = now + timedelta(days=3, hours=2)
print(future.strftime("%Y-%m-%d %H:%M"))

dt = datetime.strptime("2023-05-15 14:30", "%Y-%m-%d %H:%M")
print(dt.year)  # 输出: 2023