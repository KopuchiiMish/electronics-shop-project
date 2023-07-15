from src.item import Item
from src.phone import Phone
import pytest


def test_class_item_init(phone1):
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
    phone1.name = 'iPhone 14'
    assert str(phone1.name) == 'iPhone 14'


def test_number_of_sim(phone1):
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


@pytest.fixture()
def phone1():
    return Item("iPhone 14", 120_000, 5, 2)
