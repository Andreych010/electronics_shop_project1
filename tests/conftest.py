import pytest
from src.item import Item


@pytest.fixture
def total_cost():
    return Item("Смартфон", 10000, 20)

@pytest.fixture
def total_cost_1():
    return Item('Телефон', 10000, 5)
