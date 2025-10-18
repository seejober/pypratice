#! /usr/bin/env python3
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


async def main():
    await say_hello()


asyncio.run(main())

async def main():
    task = asyncio.create_task(say_hello())
    await task

async def main():
    future = asyncio.Future()
    await future

async def task1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 finished")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

async def long_task():
    await asyncio.sleep(10)
    print("Task finished")

async def main():
    try:
        await asyncio.wait_for(long_task(), timeout=5)
    except asyncio.TimeoutError:
        print("Task timed out")

asyncio.run(main())

async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(hello())  # Python 3.7+

async def fetch(url):
    print(f"Fetching {url}")
    await asyncio.sleep(2)
    return f"Data from {url}"

async def main():
    results = await asyncio.gather(
        fetch("url1.com"),
        fetch("url2.com")
    )
    print(results)

asyncio.run(main())


async def producer(queue):
    for i in range(5):
        await queue.put(i)
        await asyncio.sleep(0.1)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consumed {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(
        producer(queue),
        consumer(queue)
    )












