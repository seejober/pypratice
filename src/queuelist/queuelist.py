#!/usr/bin/env python3

import queue

# 创建一个队列
q = queue.Queue()

# 向队列中添加元素
q.put(1)
q.put(2)
q.put(3)

# 从队列中获取元素
print(q.get())  # 输出: 1
print(q.get())  # 输出: 2
print(q.get())  # 输出: 3


# 创建一个 LIFO 队列
q = queue.LifoQueue()

# 向队列中添加元素
q.put(1)
q.put(2)
q.put(3)

# 从队列中获取元素
print(q.get())  # 输出: 3
print(q.get())  # 输出: 2
print(q.get())  # 输出: 1

# 创建一个优先级队列
q = queue.PriorityQueue()

# 向队列中添加元素，元素为元组 (优先级, 数据)
q.put((3, 'Low priority'))
q.put((1, 'High priority'))
q.put((2, 'Medium priority'))

# 从队列中获取元素
print(q.get())  # 输出: (1, 'High priority')
print(q.get())  # 输出: (2, 'Medium priority')
print(q.get())  # 输出: (3, 'Low priority')\

import threading
import time

# 创建一个队列
q = queue.Queue()

# 生产者线程
def producer():
    for i in range(5):
        print(f'生产 {i}')
        q.put(i)
        time.sleep(1)

# 消费者线程
def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f'消费 {item}')
        q.task_done()

# 启动生产者线程
producer_thread = threading.Thread(target=producer)
producer_thread.start()

# 启动消费者线程
consumer_thread = threading.Thread(target=consumer)
consumer_thread.start()

# 等待生产者线程完成
producer_thread.join()

# 等待队列中的所有任务完成
q.join()

# 发送结束信号
q.put(None)
consumer_thread.join()

pq = queue.PriorityQueue()
pq.put((1, "low"))
pq.put((0, "high"))
print(pq.get()[1])  # 输出: "high"

q = queue.Queue(maxsize=3)  # 容量为3的队列

def producer():
    for i in range(5):
        q.put(f"Task-{i}")
        print(f"Produced: Task-{i}")

def consumer():
    while True:
        item = q.get()
        print(f"Consumed: {item}")
        q.task_done()

threading.Thread(target=producer, daemon=True).start()
threading.Thread(target=consumer, daemon=True).start()
q.join()  # 等待所有任务完成

pq = queue.PriorityQueue()
pq.put((3, "Scan"))
pq.put((1, "Emergency"))
pq.put((2, "Log"))

while not pq.empty():
    print(pq.get()[1])  # 输出顺序: Emergency → Log → Scan