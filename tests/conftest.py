import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def total_cost():
    return Item("Смартфон", 10000, 20)

@pytest.fixture
def total_cost_1():
    return Item('Телефон', 10000, 5)

@pytest.fixture
def total_cost_2():
    return Phone("iPhone 14", 120000, 5, 2)

