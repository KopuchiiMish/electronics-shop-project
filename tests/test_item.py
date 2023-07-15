"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.item import InstantiateCSVError
from unittest.mock import patch, mock_open
import pytest


@pytest.fixture()
def item1():
    return Item("Смартфон", 10000, 20)


def test_repr():
    item1 = Item('Смартфон', 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1.name = 'Смартфон'
    assert str(item1.name) == 'Смартфон'


def test_calculate_total_price(item1):
    item1.calculate_total_price()
    assert item1.price * item1.quantity == 200000


@pytest.fixture()
def item2():
    return Item("Ноутбук", 20000, 5)


def test_calculate_total_price(item2):
    item2.price = 20000
    item2.quantity = 5
    assert item2.price * item2.quantity == 100000

    # устанавливаем новый уровень цен и применяем скидки


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_setter_getter():
    name = "Смартфон"
    item1 = Item(name, 10000, 20)
    assert item1.name == name
    item1.name = "Ноутбук"
    assert item1.name != name


def test_instantiate_from_csv():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(path="")

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(path='src/w_items.csv')


def test_string_to_number():
    assert Item.string_to_number("2") == 2
    assert Item.string_to_number("2.0") == 2
    assert Item.string_to_number("2.4") == 2
