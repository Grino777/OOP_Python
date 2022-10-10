class PriceValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name
        return name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == int and 0 <= value <= 10000:
            setattr(instance, self.name, value)

class StringValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name
        return self.name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == str and 2 <= len(value) <= 50:
            setattr(instance, self.name, value)

class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.__dict__}'

class SuperShop:
    def __init__(self, name, goods=[]):
        self.name = name
        self.goods = goods

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

pr = Product('Mo', 4999)
shop = SuperShop('xxx')
shop.add_product(pr)
print(shop.__dict__)