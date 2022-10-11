class Product:
    """Класс для создания экз. класс Product, с проверкой типа входящих данных,
    генерацией уникального id и запретом на его удаление."""

    check_dict = {'id': (int,),
                  'name': (str,),
                  'weight': (int, float),
                  'price': (int, float),
                  'count': 0
                  }  # Словарь для проверки данных входящих типов и генерации ID товара

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = self.check_dict['count']

    def __new__(cls, *args, **kwargs):
        cls.check_dict['count'] += 1
        return super().__new__(cls)

    def __delattr__(self, item):
        """Проверка на удаляемый атрибут"""
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, item)

    def __setattr__(self, key, value):
        """Проверка входящих типов данных"""
        if type(value) in self.check_dict[key]:
            if key in ('price', 'weight'):
                if value >= 0:
                    object.__setattr__(self, key, value)
                else:
                    raise TypeError("Неверный тип присваиваемых данных.")
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __repr__(self):
        return f'{self.__dict__}'


class Shop:
    """Класс для создания экз. класс Shop, с возможностью добавления и удаления товаров"""
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


s = Shop('DNS')
p1 = Product('Mouse', 1, 2000)
p2 = Product('Keyboard', 1, 1000)
s.add_product(p1)
s.add_product(p2)
print(s.goods)
