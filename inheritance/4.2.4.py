class DictShop(dict):
    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            self.shop_dict = {}
        elif type(args[0]) is dict:
            for i in args[0]:
                self.__check_key(i)
            super().__init__(args[0])
        else:
            raise TypeError('аргумент должен быть словарем')

    def __setitem__(self, key, value):
        self.__check_key(key)
        self.shop_dict[key] = value.d

    @staticmethod
    def __check_key(key):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')


class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        self.d = {'name': self.name, 'price': self.price, 'weight': self.weight}


th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2
print(dict_things.__dict__)

for x in dict_things:
    print(x.name)

dict_things[1] = th_1 # исключение TypeError