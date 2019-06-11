from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        """方便拆包 x, y = my_vector"""
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        # *self 依赖上面的 __iter__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


if __name__ == '__main__':
    my_vector = Vector2d(3, 4)
    print(repr(my_vector))
    print(str(my_vector))
