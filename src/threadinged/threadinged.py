#! /usr/bin/env python3

import threading

class MyThread(threading.Thread):
    def run(self):
        print("线程开始执行")
        # 在这里编写线程要执行的代码
        print("线程执行结束")

# 创建线程实例
thread = MyThread()
# 启动线程
thread.start()
# 等待线程执行完毕
thread.join()
print("主线程结束")

def my_function():
    print("线程开始执行")
    # 在这里编写线程要执行的代码
    print("线程执行结束")

# 创建线程实例
thread = threading.Thread(target=my_function)
# 启动线程
thread.start()
# 等待线程执行完毕
thread.join()
print("主线程结束")

# 创建一个锁对象
lock = threading.Lock()

def my_function():
    with lock:
        print("线程开始执行")
        # 在这里编写线程要执行的代码
        print("线程执行结束")

# 创建线程实例
thread1 = threading.Thread(target=my_function)
thread2 = threading.Thread(target=my_function)
# 启动线程
thread1.start()
thread2.start()
# 等待线程执行完毕
thread1.join()
thread2.join()
print("主线程结束")

import queue

def worker(q):
    while not q.empty():
        item = q.get()
        print(f"处理项目: {item}")
        q.task_done()

# 创建一个队列并填充数据
q = queue.Queue()
for i in range(10):
    q.put(i)

# 创建线程实例
thread1 = threading.Thread(target=worker, args=(q,))
thread2 = threading.Thread(target=worker, args=(q,))
# 启动线程
thread1.start()
thread2.start()
# 等待队列中的所有项目被处理完毕
q.join()
print("所有项目处理完毕")


def worker(num):
    print(f"Worker {num} started")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

lock = threading.Lock()
count = 0

def increment():
    global count
    with lock:  # 自动获取和释放锁
        count += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(count)  # 输出: 10


event = threading.Event()

def waiter():
    print("Waiting for event...")
    event.wait()
    print("Event triggered!")

t = threading.Thread(target=waiter)
t.start()

# 主线程触发事件
threading.Event().wait(2.0)  # 模拟延迟
event.set()
t.join()

import random
from threading import Condition

queue = []
cond = Condition()
MAX_ITEMS = 5

def producer():
    for _ in range(10):
        with cond:
            while len(queue) >= MAX_ITEMS:
                cond.wait()
            item = random.randint(1, 100)
            queue.append(item)
            print(f"Produced {item}")
            cond.notify()

def consumer():
    for _ in range(10):
        with cond:
            while not queue:
                cond.wait()
            item = queue.pop(0)
            print(f"Consumed {item}")
            cond.notify()

threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()


