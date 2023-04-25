from src.item import Item


# тест __repr__
def test_item_repr(total_cost):
    assert total_cost.__repr__() == 'Item(name=Смартфон, price=10000, quantity=20)'


# тест инциализации
def test_item_init(total_cost):
    assert total_cost.name == 'Смартфон'
    assert total_cost.price == 10000
    assert total_cost.quantity == 20


# тест метода calculate_total_price цена без скидки
def test_item_calculate_total_price(total_cost):
    assert total_cost.calculate_total_price() == 200000


# тест метода apply_discount цена со скидкой
def test_item_apply_discount(total_cost):
    assert total_cost.apply_discount() == 11500


def test_item_sale_apply_discount(total_cost):
    Item.pay_rate = 0.8
    assert total_cost.apply_discount() == 8000

#тест метода name
def test_item_name(total_cost_1):
    assert total_cost_1.name == 'Телефон'
    total_cost_1.name = 'Смартфон'
    assert total_cost_1.name == 'Смартфон'

#тест метода instantiate_from_csv
def test_item_instantiate_from_csv(total_cost_1):
    total_cost_1.instantiate_from_csv()
    assert len(Item.all) == 5

#тест метода tring_to_number
def test_item_string_to_number(total_cost_1):
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


