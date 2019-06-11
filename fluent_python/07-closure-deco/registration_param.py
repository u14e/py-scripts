registry = set()


# register 装饰器工厂函数
def register(active=True):
    # decorate 装饰器
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')


if __name__ == '__main__':
    print('running main()')
    print('registry ->', registry)
