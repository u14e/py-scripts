from collections import namedtuple


def tuple_unpack():
    """
    元组拆包
    """
    a, b = (1, 2)
    print(a, b)

    a, b, *rest = range(5)
    print(a, b, rest)

    *head, c, d = range(5)
    print(head, c, d)


def namedtuple_test():
    """命名元组"""
    # 创建类
    City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])
    # 创建实例
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    # 获取属性
    print(tokyo.name)

    # 获取所有字段名称
    print(tokyo._fields)    # ('name', 'country', 'population', 'coordinates')
    # 返回有序字典, 用于友好显示
    print(tokyo._asdict())

    # 创建实例
    tokyo_data = ('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    tokyo = City._make(tokyo_data)   # 等同 City(*tokyo_data)


def slice_test():
    """切片"""
    invoice = """
0.....6................................40........52...55........ 
1909  Pimoroni PiBrella                    $17.50    3    $52.50 
1489  6mm Tactile Switch x20                $4.95    2     $9.90 
1510  Panavise Jr. - PV-201                $28.00    1    $28.00 
1601  PiTFT Mini Kit 320x240               $34.95    1    $34.9
    """
    # 给切片命名
    sku = slice(0, 6)
    description = slice(6, 40)

    line_items = invoice.split('\n')[2:]
    for item in line_items:
        print(item[sku], item[description])


def opt_test():
    """序列的 * 操作符"""
    board = [['_'] * 3 for _ in range(3)]
    board[1][2] = 'X'
    print(board)
    # 等同于
    # board = []
    # for i in range(3):
    #     row = ['_'] * 3
    #     board.append(row)

    weird_board = [['_'] * 3] * 3
    weird_board[1][2] = '0'
    print(weird_board)
    # 等同于
    # row = ['_'] * 3
    # board = []
    # for i in range(3):
    #     board.append(row)


def self_opt_test():
    """
    序列的自增操作符:
        对不可变序列进行重复拼接操作的话，效率会很低，
        因为每次都有一个新对象，而解释器需要把原来对象中的元素先复制到新的对象里，然后再追加新的元素
        (str 例外, CPython 在 str 初始化内存的时候，为它留出了额外的可扩展空间)
    """
    l = [1, 2, 3]
    print(id(l), l)
    l *= 2
    print(id(l), l)

    t = (1, 2, 3)
    print(id(t), t)
    t *= 2
    print(id(t), t)


if __name__ == "__main__":
    # tuple_unpack()
    # namedtuple_test()
    # slice_test()
    # opt_test()
    self_opt_test()
