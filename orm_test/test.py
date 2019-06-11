# @Author: u14e
# @Time  : 2019/3/18 10:24
# @description:
from orm_test import Model, CharField, IntField


def run():
    class Author(Model):
        name = CharField()

    # class Book(Model):
    #     title = CharField()
    #     year = IntField()
        # author = Relation(Author, 'books')

    u14e = Author(name='u14e')
    # book = Book(title='A title', year=1996, author=u14e)

    print(u14e)


if __name__ == '__main__':
    run()
