from src.item import Item
from src.keyboard import Keyboard
import pytest


@pytest.fixture()
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_change_lang():
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
