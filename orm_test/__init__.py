# @Author: u14e
# @Time  : 2019/3/18 9:27
# @description: https://speakerdeck.com/lig/your-own-orm-in-python-how-and-why


class Field(object):
    def __get__(self, instance, type=None):
        return instance._data[self._name]

    def __set__(self, instance, value):
        instance._data[self._name] = value


class ModelMeta(type):
    def __new__(cls, clsname, bases, attrs):
        new_cls = super(ModelMeta, cls).__new__(cls, clsname, bases, attrs)
        for field_name, field in attrs.items():
            # print(field_name, field)
            # if isinstance(field, Relation):
            #     setattr(field._rel_model_class, field._reverse_name, ReverseRelation(new_cls, field_name))
            # else:
            if isinstance(field, Field):
                field._name = field_name
        attrs['_data'] = {}.fromkeys(attrs.keys())
        return new_cls


class Model(object, metaclass=ModelMeta):
    pass


class CharField(Field):
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(instance, self._name, str, value)
        super(CharField, self).__set__(instance, value)


class IntField(Field):
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(instance, self._name, int, value)
        super(IntField, self).__set__(instance, value)


# class Relation(Field):
#     def __init__(self, rel_model_class, reverse_name):
#         self._rel_model_class = rel_model_class
#         self._reverse_name = reverse_name
#
#     def __set__(self, instance, value):
#         if not isinstance(value, self._rel_model_class):
#             raise TypeError(instance, self._name, self._rel_model_class, value)
#         super(Relation, self).__set__(instance, value)
#
#
# class ReverseRelation(object):
#     def __init__(self, origin_model, field_name):
#         self._origin_model = origin_model
#         self._field_name = field_name
#
#     def __get__(self, instance, type=None):
#         return self._origin_model.S.filter(self._field_name=instance)
