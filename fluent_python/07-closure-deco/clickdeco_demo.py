import time
import clock


@clock.clock('{name}({arg_str}) dt={elapsed:0.3f}s')
def snooze(seconds):
    time.sleep(seconds)


@clock.clock()
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    snooze(.123)
    factorial(6)
    print(factorial.__name__)
