import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)

print(wref)     # 弱引用实例
print(wref())   # 返回被引用的对象(即 {0, 1})

a_set = {2, 3, 4}   # {0, 1}的引用数减少(为0)

print(wref())
print(wref() is None)
