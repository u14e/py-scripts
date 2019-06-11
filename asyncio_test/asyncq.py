# @Author: u14e
# @Time  : 2019/1/20 18:55
# @description: 队列(生产消费模式)
import asyncio
import itertools as it
import os
import random
import time


async def makeitem(size: int = 5) -> str:
    """随机字符串"""
    return os.urandom(size).hex()


async def randint(a: int, b: int) -> int:
    return random.randint(a, b)


async def randsleep(a: int = 1, b: int = 5, caller=None) -> None:
    i = await randint(a, b)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


async def produce(name: int, q: asyncio.Queue) -> None:
    n = await randint(1, 5)
    for _ in it.repeat(None, n):  # Synchronous loop for each single producer
        await randsleep(caller=f"Producer {name}")
        i = await makeitem()
        t = time.perf_counter()
        await q.put((i, t))
        print(f"Producer {name} added <{i}> to queue.")


async def consume(name: int, q: asyncio.Queue) -> None:
    while True:
        await randsleep(caller=f"Consumer {name}")
        i, t = await q.get()
        now = time.perf_counter()
        print(f"Consumer {name} got element <{i}>"
              f" in {now-t:0.5f} seconds.")
        q.task_done()


async def main(nprod: int, ncon: int):
    q = asyncio.Queue()
    producers = [asyncio.ensure_future(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.ensure_future(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers)
    await q.join()  # Implicitly awaits consumers, too
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    import argparse
    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=5)
    parser.add_argument("-c", "--ncon", type=int, default=10)
    ns = parser.parse_args()
    start = time.perf_counter()

    asyncio.get_event_loop().run_until_complete((main(**ns.__dict__)))

    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")
