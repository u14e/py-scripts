# @Author: u14e
# @Time  : 2019/5/27 15:57
# @description:
import array
import random

# 生成一个有 1000 万个双精度浮点数的数组
floats = array.array('d', (random.random() for i in range(10**7)))
print(floats[-1])

# 存入二进制文件
with open('floats.bin', 'wb') as f:
    floats.tofile(f)

# 从二进制文件读取出来
floats2 = array.array('d')
with open('floats.bin', 'rb') as f:
    floats2.fromfile(f, 10**7)
print(floats2[-1])

print(floats == floats2)

if __name__ == '__main__':
    pass
