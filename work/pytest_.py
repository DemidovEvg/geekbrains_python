#test_ or end with _test.py
import pytest
# run: pytest work\pytest_.py

#############################################
def capital_case(x):
    if isinstance(x, str):
        return x.capitalize()
    else:
        raise TypeError('Please provide a string argument')
    

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
##############################################
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 100 and value > 0:
            self._age = value + 10
        else:
            raise ValueError

@pytest.fixture
def bob(name = 'Bob', age = 33):
    return Person(name, age)

def test_create_bob(bob):
    assert isinstance(bob.name, str) and bob.age > 0 and bob.age < 100

def test_create_wrong_age():
    with pytest.raises(ValueError):
        Person('', 150)
##############################################
@pytest.mark.parametrize("age_in, age_out", [
    (10, 20),
    (30, 40),
    (89, 99),
])
def test_multi_age(age_in, age_out):
    person = Person('test', age_in)
    assert person.age == age_out
##############################################
@pytest.fixture
def bob(name = 'Bob', age = 33):
    return Person(name, age)

@pytest.mark.parametrize("age_in, age_out", [
    (10, 20),
    (30, 40),
    (89, 99),
])
def test_multi_age(bob, age_in, age_out):
    bob.age = age_in
    assert bob.age == age_out



