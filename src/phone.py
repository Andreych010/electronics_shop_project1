from src.item import Item


class Phone(Item):
    '''
    подкласс класса item
    '''
    def __init__(self, name, price, quantity, number_of_sim):
        '''
        инициализация атрибутов базового класса Item,
        с атрибутом подкласса Phone
        number_of_sim = кол-во сим карт
        '''
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        '''
        Предоставляет текстовый образ объекта
        '''
        return f"{self.__class__.__name__}('{self.name}', {self.price}," \
               f" {self.quantity}, {self.__number_of_sim})"

    def __str__(self):
        '''
        Возвращает нименование товара
        '''
        return f'{self.name}'

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise (Exception("C объектами других классов запрещено сложение."))


