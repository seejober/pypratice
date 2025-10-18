#!/usr/bin/env python3
import os

# 获取当前工作目录
current_dir = os.getcwd()
print("当前工作目录:", current_dir)

# 列出目录下的文件
files = os.listdir(current_dir)
print("目录下的文件:", files)
import glob
print(glob.glob('*.py'))
import sys
print(sys.argv)
sys.stderr.write('Warning, log file not found starting a new one\n')

import re

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

print('tea for too'.replace('too', 'two'))
import math

print(math.cos(math.pi / 4))
print(math.log(1024, 2))
import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))   # sampling without replacement)
print(random.random())
print(random.randrange(6))

print("--------------------------------------------------------")
from urllib.request import urlopen
for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    if 'EST' in line or 'EDT' in line:  # look for Eastern Time
        print(line)



import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
    From: soothsayer@example.org

    Beware the Ides of March.
    """)
server.quit()



