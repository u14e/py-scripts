def tag(name, *content, cls=None, **attrs):
    """生成一个或多个html标签"""
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' {}="{}"'.format(attr, value)
                           for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<{name}{attr}>{c}</{name}>'.format(
            name=name,
            attr=attr_str,
            c=c
        ) for c in content)
    else:
        return '<{name}{attr} />'.format(name=name,
                                         attr=attr_str)


def sig_tag():
    import inspect
    sig = inspect.signature(tag)
    my_tag = dict(name='img',
                  title='Sunset',
                  src='sunset.jpg',
                  cls='framed')
    # 任意个参数绑定到签名中的形参上
    # 使用这个方法在真正调用函数前验证参数
    bound_args = sig.bind(**my_tag)
    print(bound_args)
    for name, value in bound_args.arguments.items():
        print(name, '=', value)


def sig_tag_valid():
    """使用签名的bind方法验证函数参数"""
    import inspect
    sig = inspect.signature(tag)
    my_tag = dict(
        # name='img',
        title='Sunset',
        src='sunset.jpg',
        cls='framed'
    )
    try:
        sig.bind(**my_tag)
    except TypeError as e:
        print(e)


def index(name, password, **kwargs):
    pass


def sig_index():
    import inspect
    sig = inspect.signature(index)
    form = dict(
        # name='u14e',
        password='123456',
        foo='bar'
    )
    try:
        sig.bind(**form)
    except TypeError as e:
        print(e)
    else:
        print('+valid success')


if __name__ == '__main__':
    # sig_tag()
    # sig_tag_valid()
    sig_index()

    print(tag('br'))
    print(tag('p', 'hello'))
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', id=3))
    print(tag('p', 'hello', cls='main', id=3))