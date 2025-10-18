#!/usr/bin/env python3

import datetime

#获取当前日期和时间
current_datetime = datetime.datetime.now()
print(current_datetime)

# 获取当前日期
current_date = datetime.date.today()
print(current_date)

# 格式化日期
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # 输出：2023-07-17 15:30:45

from datetime import date
now = date.today()
print(now)

datetime.date(2023, 7, 17)

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

birthday = date(1964, 7, 31)
age = now - birthday   # 计算两个日期之间的时间差
print(age.days)












