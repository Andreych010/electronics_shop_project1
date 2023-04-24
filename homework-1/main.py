from src.item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)  # экземпляры класса Item
    item2 = Item("Ноутбук", 20000, 5)

    print(f'Общая стоимость {item1.product} в магазинах: {item1.calculate_total_price()}')  # Обая стоимость товаров 200000
    print(f'Общая стоимость {item2.product} в магазинах: {item2.calculate_total_price()}')  # 100000

    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount()

    print(f'Стоимость {item1.product} со скидкой в {Item.pay_rate}: {item1.price} ')  # Стоимость товара со скидкой 8000.0
    print(f'Стоимость {item2.product} ,без скидки: {item2.price}')  # Стоимость товара без скидки 20000
    print(f'Общее наличие Товаров на складе: {Item.all}')  # Сохданные экземпляры класса Item
