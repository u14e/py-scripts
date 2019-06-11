# @Author: u14e
# @Time  : 2019/1/20 17:26
# @description:
import asyncio


async def count(num):
    print(f'start count {num}')
    await asyncio.sleep(1)
    # time.sleep(1)
    print(f'end count {num}')


async def main():
    await asyncio.gather(count(1), count(2), count(3))


if __name__ == '__main__':
    import time
    s = time.perf_counter()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    elapsed = time.perf_counter() - s
    print(f'{__file__} executed in {elapsed:0.2f} seconds.')
