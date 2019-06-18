# @Author: u14e
# @Time  : 2019/3/18 0:33
# @description: 元类
# @links:
#   - http://blog.jobbole.com/21351/
#   - https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python


def test_1():
    class ObjectCreator(object):
        pass
    my_object = ObjectCreator()
    print(my_object)
    print(ObjectCreator)    # ObjectCreator(类) 也是一个对象


def test_2():
    """动态创建类"""
    def choose_class(name):
        if name == 'foo':
            class Foo(object):
                pass
            return Foo
        else:
            class Bar(object):
                pass
            return Bar

    my_class = choose_class('foo')
    print(my_class)     # 函数返回的是类，不是实例
    print(my_class())   # 可以通过这个类创建实例


def test_3():
    """
    使用 type 动态的创建类
    type(类名,
        由父类组成的元组(针对继承的情况，可以为空)
        ，包含属性的字典(名称和值))
    """
    # class Foo(object):
    #     bar = True
    Foo = type('Foo', (), {'bar': True})
    print(Foo)
    print(Foo())
    print(Foo().bar)

    # class FooChild(Foo):
    #     pass
    def echo_bar(self):
        print(self.bar)
    FooChild = type('FooChild', (Foo, ), {'echo_bar': echo_bar})
    print(FooChild)
    print(FooChild.bar)
    print(hasattr(Foo, 'echo_bar'))
    print(hasattr(FooChild, 'echo_bar'))
    my_foo = FooChild()
    my_foo.echo_bar()


def test_4():
    """
    type就是Python在背后用来创建所有类的元类
    (str 是用来创建字符串对象的类，而 int 是用来创建整数对象的类, type 就是创建这些类的元类类)
    """
    age = 35
    print(age.__class__)
    print(age.__class__.__class__)

    name = 'u14e'
    print(name.__class__)
    print(name.__class__.__class__)

    def foo(): pass
    print(foo.__class__)
    print(foo.__class__.__class__)

    class Bar(object): pass
    b = Bar()
    print(b.__class__)
    print(b.__class__.__class__)


def test_5():
    """
    使用 metaclass:
        Foo中有 metaclass 这个关键词参数吗？
        如果是，Python会在内存中通过 metaclass 创建一个名字为Foo的类对象（我说的是类对象，请紧跟我的思路）。
        如果Python没有找到 metaclass ，它会继续在 Bar（父类）中寻找 metaclass，并尝试做和前面同样的操作。
        如果Python在任何父类中都找不到 metaclass，它就会在模块层次中去寻找 __metaclass__，并尝试做同样的操作。
        如果还是找不到 metaclass, Python就会用内置的 type 来创建这个类对象。
    """
    class Bar(object, metaclass=UpperAttrMetaclass):
        pass

    class Foo(Bar):
        name = 'u14e'

    print(hasattr(Foo, 'name')) # False
    print(hasattr(Foo, 'NAME')) # True


class UpperAttrMetaclass(type):
    """将所有的类的属性修改为大写形式"""
    def __new__(cls, clsname, bases, dct):
        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)

# 带参数的自定义元类
# class Foo(object, metaclass=UpperAttrMetaclass, kwarg1=1):
#     pass
#
# class Thing(type):
#     def __new__(cls, clsname, bases, dct, kwargs1=default):
#         pass

# 元类所做的:
# 1. 拦截类的创建
# 2. 修改类
# 3. 返回修改之后的类


def run():
    # test_1()
    # test_2()
    # test_3()
    # test_4()
    test_5()


if __name__ == '__main__':
    run()
