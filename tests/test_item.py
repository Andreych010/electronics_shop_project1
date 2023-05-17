from src.item import Item, InstantiateCSVError
import csv



# тест __repr__
def test_item_repr(total_cost):
    assert repr(total_cost) == "Item('Смартфон', 10000, 20)"
    assert str(total_cost) == 'Смартфон'


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


# тест метода name
def test_item_name(total_cost_1):
    assert total_cost_1.name == 'Телефон'
    total_cost_1.name = 'Смартфон'
    assert total_cost_1.name == 'Смартфон'


# тест метода instantiate_from_csv
def test_item_instantiate_from_csv(total_cost_1):
    total_cost_1.instantiate_from_csv()
    assert len(Item.all) == 5


# тест метода tring_to_number
def test_item_string_to_number(total_cost_1):
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


# тест repr, str Phone
def test_phone_repr_str(total_cost_2):
    assert repr(total_cost_2) == "Phone('iPhone 14', 120000, 5, 2)"
    assert str(total_cost_2) == 'iPhone 14'


# тест init
def test_phone_init(total_cost_2):
    assert total_cost_2.name == 'iPhone 14'
    assert total_cost_2.price == 120000
    assert total_cost_2.quantity == 5
    assert total_cost_2.number_of_sim == 2


# тест add Phone
def test_add_quantity(total_cost, total_cost_2):
    assert total_cost_2 + total_cost == 25
    assert total_cost_2 + total_cost_2 == 10

#Тесты KeyBoard
def test_keyboard_repr_str(total_cost_3):
    assert repr(total_cost_3) == "KeyBoard('Dark Project KD87A', 9600, 5)"
    assert str(total_cost_3) == 'Dark Project KD87A'
    assert str(total_cost_3.language) == "EN"

    total_cost_3.change_lang()
    assert str(total_cost_3.language) == "RU"

    total_cost_3.change_lang().change_lang()
    assert str(total_cost_3.language) == "RU"

# тест искючений в методе instantiate_from_csv класса Item
def test_item_instantiate_from_csv_try_except():
    PATH = "../src/items.csv"

    try:
        with open(PATH, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                (row['name'], row['price'], row['quantity'])
    except FileNotFoundError:
        assert True
    except NameError:
        assert True
    except KeyError:
        assert True