from typing import ParamSpecArgs
from unittest.mock import MagicMock

class ProductionClass:
    def method(self):
        return 1

thing = ProductionClass()
thing.method = MagicMock(return_value=3)
result = thing.method(3, 4, 5, key='value')

thing.method.assert_called_with(3, 4, 5, key='value')



from unittest.mock import patch
import module


@patch('module.ClassName2')
@patch('module.ClassName1')
def test(MockClass1, MockClass2):
    module.ClassName1()
    module.ClassName2()
    assert MockClass1 is module.ClassName1
    assert MockClass2 is module.ClassName2
    assert MockClass1.called
    assert MockClass2.called

test()

class A:
    pass

class B:
    ParamSpecArgs

@patch('__main__.A', new_callable=B)
def test2(normal_arg, MockClass):
    print(normal_arg, MockClass)

test2()

with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
    thing = ProductionClass()
    result = thing.method(1, 2, 3)
    pass

mock_method.assert_called_once_with(1, 2, 3)