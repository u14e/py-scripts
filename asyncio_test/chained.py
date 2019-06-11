# @Author: u14e
# @Time  : 2019/1/20 18:26
# @description: 链式调用
import asyncio
import random
import time


async def randint(a: int, b: int) -> int:
    return random.randint(a, b)


async def part_a(n: int) -> str:
    i = await randint(0, 10)
    print(f"part_a({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-a"
    print(f"Returning part_a({n}) == {result}.")
    return result


async def part_b(n: int, arg: str) -> str:
    i = await randint(0, 10)
    print(f"part_b{n, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-b derived from {arg}"
    print(f"Returning part_b{n, arg} == {result}.")
    return result


async def chain(n: int) -> None:
    start = time.perf_counter()
    pa = await part_a(n)
    pb = await part_b(n, pa)
    end = time.perf_counter() - start
    print(f"-->Chained result{n} => {pb} (took {end:0.2f} seconds).")


async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))


if __name__ == "__main__":
    import sys
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(*args))

    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")
