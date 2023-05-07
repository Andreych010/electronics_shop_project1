from src.item import Item


class MixinKey:
    '''
    Реалезует хранение и изменение раскладки клавиатуры
    '''
    __language = 'EN'

    def __init__(self):
        self.__language = self.__language

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__language}')"

    def __str__(self):
        return f"{self.__language}"

    @property
    def language(self):
        return self.__language

    # @language.setter
    # def language(self,new_language):
    #     self.__language = new_language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self.__language
        elif self.__language == 'RU':
            self.__language = 'EN'
            return self


class KeyBoard(Item, MixinKey):
    '''
    Класс KeyBoard для товара “клавиатура”
    '''

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"
