# @Author: u14e
# @Time  : 2019/6/27 10:17
# @description: https://www.liaoxuefeng.com/wiki/1016959663602400/1048430311230688
import asyncio

async def hello():
    print('Hello World')
    await asyncio.sleep(1)
    print('Hello again')

def run():
    # 获取事件循环
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    # 执行协程(并发)
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    run()