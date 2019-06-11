# @Author: u14e
# @Time  : 2019/1/20 17:41
# @description:
import time


def count(num):
    print(f'start count {num}')
    time.sleep(1)
    print(f'end count {num}')


def main():
    for i in range(1, 4):
        count(i)


if __name__ == '__main__':
    import time
    s = time.perf_counter()

    main()

    elapsed = time.perf_counter() - s
    print(f'{__file__} executed in {elapsed:0.2f} seconds.')