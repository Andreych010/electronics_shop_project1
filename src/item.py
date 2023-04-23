class Item:
    '''
Представляет товары в магазине
    '''
    pay_rate = 1.15
    all = []

    def __init__(self, product, price, quantity):
        self.produkt = product
        self.price = price
        self.quantity = quantity
        self.produkt = f'{product}'

        Item.all += self.produkt, self.price, self.quantity

    def __repr__(self):
        return f'Item(product={self.produkt}, price={self.price}, quantity={self.quantity})'

    def calculate_total_price(self):
        '''
    Стоимость товара без скидки
        '''
        return self.price * self.quantity

    def apply_discount(self):
        '''
    Стоимость товара со скидкой
        '''
        self.price = int(self.price * self.pay_rate)
        return self.price
