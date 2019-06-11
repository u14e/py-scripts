from collections import namedtuple
import inspect
import promotions

Customer = namedtuple('Customer', ['name', 'fidelity'])


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# inspect.getmembers 获取对象(这里是模块)的属性
# promos = [fidelity_promo, bulk_item_promo, large_order_promo]
promos = [func for name, func in
          inspect.getmembers(promotions, inspect.isfunction)]


def best_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)


def best_run():
    print(Order(joe, long_order, best_promo))
    print(Order(joe, banana_cart, best_promo))
    print(Order(ann, cart, best_promo))


if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)

    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]

    banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apple', 10, 1.5)]

    long_order = [LineItem(str(item_code), 1, 1.0)
                  for item_code in range(10)]

    best_run()
