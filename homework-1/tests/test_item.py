from src.item import Item


# тест __repr__
def test_item_repr(total_cost):
    assert total_cost.__repr__() == 'Item(product=Смартфон, price=10000, quantity=20)'


# тест инциализации
def test_item_init(total_cost):
    assert Item.all == ['Смартфон', 10000, 20, 'Смартфон', 10000, 20]
    assert total_cost.produkt == 'Смартфон'
    assert total_cost.price == 10000
    assert total_cost.quantity == 20


# тест метода calculate_total_price цена без скидки
def test_calculate_total_price(total_cost):
    assert total_cost.calculate_total_price() == 200000


# тест метода apply_discount цена со скидкой
def test_apply_discount(total_cost):
    assert total_cost.apply_discount() == 11500


def test_sale_apply_discount(total_cost):
    Item.pay_rate = 0.8
    assert total_cost.apply_discount() == 8000
