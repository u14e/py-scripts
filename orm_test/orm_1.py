# @Author: u14e
# @Time  : 2019/3/18 10:54
# @description:
#   https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000
#########################################
# Field
#########################################
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __getattr__(self, item):
        return ''

    def __str__(self):
        return '<{}:{}>'.format(self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class InterField(Field):
    def __init__(self, name):
        super(InterField, self).__init__(name, 'bigint')


#########################################
# Model
#########################################
class ModelMetaclass(type):
    def __new__(cls, clsname, bases, attrs):
        mappings = dict()
        for field_name, field in attrs.items():
            if isinstance(field, Field):
                mappings[field_name] = field
        for field_name in mappings.keys():
            attrs.pop(field_name)
        attrs['__mappings__'] = mappings    # 保存属性和列的映射关系
        attrs['__table__'] = clsname        # 假设表名和类名一直
        return type.__new__(cls, clsname, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('{} object has no attribute {}'.format(self.__class__.__name__,
                                                                        key))


def run():
    class User(Model):
        id = InterField('id')
        name = StringField('username')
        email = StringField('email')
        password = StringField('password')

    u = User(id=1, name='foo', email='46@qq.com', password='123456')
    # u.save()
    print(u)
    print(u.id)


if __name__ == '__main__':
    run()
