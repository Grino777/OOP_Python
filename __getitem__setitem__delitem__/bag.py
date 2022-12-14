class Thing:
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight=0):
        self.max_weight = max_weight
        self.total_weight = 0
        self.bag = []

    def __getitem__(self, item):
        return self.bag[item]

    def __setitem__(self, key, value):
        if self.__validator(key):
            if isinstance(value, Thing):
                weight = self.total_weight - self.bag[key].weight + value.weight
                if weight <= self.max_weight:
                    self.total_weight = weight
                    self.bag[key] = value
                else:
                    raise ValueError('превышен суммарный вес предметов')

    def __delitem__(self, key):
        if self.__validator(key):
            self.total_weight -= self.bag[key].weight
            del self.bag[key]

    def __validator(self, indx):
        if isinstance(indx, int) and indx <= len(self.bag):
            return True
        else:
            raise IndexError('неверный индекс')

    def add_thing(self, thing):
        weight = self.total_weight + thing.weight
        if weight <= self.max_weight:
            self.total_weight = weight
            self.bag.append(thing)
        else:
            raise ValueError('превышен суммарный вес предметов')


b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[
    0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[
    1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"

#Лучшее решение:
# class Thing:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
# class Bag:
#     def __init__(self, max_weight):
#         self.max_weight = max_weight
#         self.__weight = 0
#         self.__things = []
#
#     def __check_weight(self, new_thing, replace_thing=Thing('', 0)):
#         if self.__weight - replace_thing.weight + new_thing.weight > self.max_weight:
#             raise ValueError('превышен суммарный вес предметов')
#
#     def __check_idx(self, idx):
#         if idx not in range(len(self.__things)):
#             raise IndexError('неверный индекс')
#
#     def add_thing(self, thing):
#         self.__check_weight(thing)
#         self.__things.append(thing)
#         self.__weight += thing.weight
#
#     def __getitem__(self, idx):
#         self.__check_idx(idx)
#         return self.__things[idx]
#
#     def __setitem__(self, idx, thing):
#         self.__check_idx(idx)
#         self.__check_weight(thing, self.__things[idx])
#         self.__things[idx] = thing
#         self.__weight += thing.weight
#
#     def __delitem__(self, idx):
#         self.__check_idx(idx)
#         thing = self.__things.pop(idx)
#         self.__weight -= thing.weight
