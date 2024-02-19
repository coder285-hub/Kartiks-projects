import pytest
from jar import Jar

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

def test_str():
    jar = Jar(5)
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(8)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(4)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.deposit(-2)
    with pytest.raises(ValueError):
        jar.deposit(6)

def test_withdraw():
    jar = Jar(6)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)
    with pytest.raises(ValueError):
        jar.withdraw(-2)

def test_capacity():
    jar = Jar(10)
    assert jar.capacity == 10
    jar = Jar()
    assert jar.capacity == 12

def test_size():
    jar = Jar(7)
    assert jar.size == 0
    jar.deposit(3)
    assert jar.size == 3
    jar.withdraw(2)
    assert jar.size == 1
