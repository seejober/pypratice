#!/usr/bin/env python3
import re

pattern = r"hello"
text = "hello world"

match = re.match(pattern, text)
if match:
    print("匹配成功:", match.group())
else:
    print("匹配失败")

pattern = r"world"
text = "hello world"

match = re.search(pattern, text)
if match:
    print("匹配成功:", match.group())
else:
    print("匹配失败")

pattern = r"\d+"
text = "There are 3 apples and 5 oranges."

matches = re.findall(pattern, text)
print("找到的数字:", matches)

pattern = r"apple"
text = "I have an apple."

new_text = re.sub(pattern, "banana", text)
print("替换后的文本:", new_text)

pattern = r"cat"
text = "The cat is on the mat."

match = re.search(pattern, text)
if match:
    print("匹配成功:", match.group())

pattern = r"\d+"
text = "The price is 100 dollars."

match = re.search(pattern, text)
if match:
    print("匹配成功:", match.group())

pattern = r"[aeiou]"
text = "Hello World!"

matches = re.findall(pattern, text)
print("找到的元音字母:", matches)

pattern = r"(ab)+"
text = "ababab"

match = re.search(pattern, text)
if match:
    print("匹配成功:", match.group())

pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email = "example@example.com"

if re.match(pattern, email):
    print("有效的电子邮件地址")
else:
    print("无效的电子邮件地址")

pattern = r"\d{3}-\d{3}-\d{4}"
text = "My phone number is 123-456-7890."

match = re.search(pattern, text)
if match:
    print("找到的电话号码:", match.group())

text = "Contact: admin@example.com, support@test.org"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(emails)  # 输出: ['admin@example.com', 'support@test.org']

date_str = "Today is 05-15-2023"
new_str = re.sub(r'(\d{2})-(\d{2})-(\d{4})', r'\3年\1月\2日', date_str)
print(new_str)  # 输出: "Today is 2023年05月15日"

pattern = re.compile(r'''
    ^(?P<username>\w+)  # 用户名
    :(?P<password>\S+)  # 密码
    @(?P<domain>\w+\.\w+)  # 域名
$''', re.VERBOSE)

m = pattern.match("john:pass123@example.com")
if m:
    print(m.groupdict())  # 输出: {'username': 'john', 'password': 'pass123', 'domain': 'example.com'}

text = "Apple1Banana2Cherry3Date"
parts = re.split(r'\d+', text)
print(parts)  # 输出: ['Apple', 'Banana', 'Cherry', 'Date']









