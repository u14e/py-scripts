# @Author: u14e
# @Time  : 2019/2/25 11:43
# @description: 从一个集合中获得最大或者最小的 N 个元素列表
import heapq


def run():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    # N = 1 时
    print(max(nums))

    # N 相对比较小 时
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    # N 的大小和集合大小接近时(N == len(nums))
    result_left = sorted(nums)[:10]     # 前十个
    result_right = sorted(nums)[-10:]   # 后十个
    print(result_left)
    print(result_right)


if __name__ == '__main__':
    run()
