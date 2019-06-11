def clip(text, max_len=80):
    """在max_len前面或后面的第一个空格处截断文本"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after

    if end is None: # 没找到空格
        end = len(text)

    return text[:end].rstrip()


# 注解中最常用的类型是类（如 str 或 int）和字符串（如 'int > 0'）
# 注解不会做任何处理，只是存储在函数的 __annotations__ 属性
def clip_with_anno(text:str, max_len:'int > 0'=80) -> str:
    """在max_len前面或后面的第一个空格处截断文本"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after

    if end is None:  # 没找到空格
        end = len(text)

    return text[:end].rstrip()


def inspect_clip():
    print(clip.__defaults__)
    print(clip.__code__)
    print(clip.__code__.co_varnames)
    print(clip.__code__.co_argcount)


def sig_clip():
    """
    param.kind：
        POSITIONAL_OR_KEYWORD 可以通过定位参数和关键字参数传入的形参
        VAR_POSITIONAL 定位参数元组
        VAR_KEYWORD 关键字参数字典
        KEYWORD_ONLY 仅限关键字参数
        POSITIONAL_ONLY 　仅限定位参数；目前，Python 声明函数的句法不支持，但是有些使 用 C 语言实现且不接受关键字参数的函数（如 divmod）支持
    """
    from inspect import signature
    sig = signature(clip)
    print(str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)


if __name__ == '__main__':
    inspect_clip()
    # sig_clip()

    #
    # print(clip_with_anno.__annotations__)
