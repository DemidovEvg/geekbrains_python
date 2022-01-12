class Column:
    '''
    Represents a database column.

    This is used to create the underlying table in the database
    and to translate database types to Python types.
    '''
    def __init__(self, type):
        self.type = type

class Manager:
    '''
    Accessed via `YourModel.objects`. This is what constructs
    a `QuerySet` object in Django.
    '''
    def __init__(self, model):
        self.model = model

    def get(self, id):
        '''
        Pretend `YourModel.objects.get(id=123)` queries the database directly.
        '''
        # Create an instance of the model. We only keep track of the model class.
        instance = self.model()
        # Populate the instance's attributes with the result of the database query
        for name in self.model._columns:
            # Pretend we load the values from the database
            value = 123
            setattr(instance, name, value)
        # This would be done above if we actually queried the database
        instance.id = id
        # Finally return the instance of `self.model`
        return instance


class ModelBase(type):
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        # The `Manager` instance is made a class attribute
        new_cls.objects = Manager(new_cls)
        # Keep track of the columns for conveniece
        new_cls._columns = {}
        for name, attr in attrs.items():
            if isinstance(attr, Column):
                new_cls._columns[name] = attr
        # The class is now ready
        return new_cls


class Model(metaclass=ModelBase):
    '''
    Django's `Model` is more complex.
    This one only uses `ModelBase` as its metaclass so you can just inherit from it
    '''
    pass


class MyModel(Model):
    id = Column(int)
    column2 = Column(float)
    column3 = Column(str)


if __name__ == '__main__':
    print(MyModel._columns)
    instance = MyModel.objects.get(id=5)
    print(instance.column2)