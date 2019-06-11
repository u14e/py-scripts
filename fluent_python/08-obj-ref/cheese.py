import weakref


class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


stock = weakref.WeakValueDictionary()
catelog = [Cheese('Red Leicester'), Cheese('Tilsit'),
           Cheese('Brie'), Cheese('Parmesan')]

for cheese in catelog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))
del catelog
# for 循环中的变量 cheese 是全局变量，除非显式删除，否则不会消失
print(sorted(stock.keys()))     # ['Parmesan']
del cheese
print(sorted(stock.keys()))     # []
