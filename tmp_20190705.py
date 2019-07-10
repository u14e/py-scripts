# @Author: u14e
# @Time  : 2019/7/5 15:15
# @description:
def delete_dup(l1):
    map = {}
    l = []
    for i in l1[::]:
        if map.get(i) is None:
            map[i] = True
            l.append(i)
    return l

def revert_int(num):
    r = 0
    while num:
        r = r * 10 + num % 10
        num = num // 10
    return r

if __name__ == '__main__':
    print(delete_dup(['b','c','d','c','a','a']))
    print(revert_int(123))
