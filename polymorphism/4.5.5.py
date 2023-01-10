class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    ID = 0

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self._id = self.ID
        self.plus_id()

    def get_id(self):
        return self._id

    @classmethod
    def plus_id(cls):
        cls.ID += 1


items = []

for i in range(5):
    items.append(ShopItem(f'name {i}', 300, 1000))

for i in items:
    print(i.get_id())
