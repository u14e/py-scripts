# @Author: u14e
# @Time  : 2019/6/26 9:57
# @description:
class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        """使得类可散列"""
        return hash(self.x) ^ hash(self.y)


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.2)
    print(hash(v1), hash(v2))
    print(len(set([v1, v2])))

    # 查看所有实例属性(包括私有属性)
    print(v1.__dict__)