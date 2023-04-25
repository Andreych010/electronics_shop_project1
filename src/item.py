import csv

PATH = "../src/items.csv"


class Item:
    '''
Представляет товары в магазине
    '''
    pay_rate = 1.15
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
Создание экземпляра класса item.
:param name: Название товара.
:param price: Цена за единицу товара.
:param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        '''
Предоставляет текстовый образ объекта
        '''
        return f'Item(name={self.__name}, price={self.price}, quantity={self.quantity})'

    @property
    def name(self):
        '''
Читает приватные данные
        '''
        return self.__name

    @name.setter
    def name(self, new_name):
        '''
Проверяет, что длина наименования товара не больше 10 симвовов
        '''
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            print('Длина наименования товара превышает 10 символов')

    @classmethod
    def instantiate_from_csv(cls):
        '''
Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        '''
        cls.all = []
        with open(PATH, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(num):
        '''
Cтатический метод, возвращающий число из числа-строки
        '''
        return int(float(num))

    def calculate_total_price(self):
        """
Рассчитывает общую стоимость конкретного товара в магазине.
:return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        '''
Стоимость товара со скидкой
        '''
        self.price = int(self.price * self.pay_rate)
        return self.price
