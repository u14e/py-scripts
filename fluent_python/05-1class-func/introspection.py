def func_property():
    '''通过差集, 获取函数专有属性列表'''
    class C: pass
    obj = C()
    def func(): pass

    result = sorted(set(dir(func)) - set(dir(obj)))
    print(result)


if __name__ == "__main__":
    func_property()