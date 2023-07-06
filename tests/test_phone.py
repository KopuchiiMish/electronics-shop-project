from src.item import Item
from src.phone import Phone
import pytest

@pytest.fixture()
def phone1():
    return Item("iPhone 14", 120_000, 5, 2)

def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test_str():
    phone1.name = 'iPhone 14'
    assert str(phone1.name) == 'iPhone 14'
