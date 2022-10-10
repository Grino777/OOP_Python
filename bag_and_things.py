#Решение с дескрипторами:
class CheckWieght:
    """Дескриптор для отображения и изменения веса предметов"""

    def __set_name__(self, owner, name):
        self.name = '_' + name
        return self.name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (int, float):
            setattr(instance, self.name, value)


class CheckName:
    """Дескриптор для отображения и изменения имени предметов"""

    def __set_name__(self, owner, name):
        self.name = '_' + name
        return self.name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == str:
            setattr(instance, self.name, value)


class Thing:
    name = CheckName()  # Дескриптор
    weight = CheckWieght()  # Дескриптор

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight  # максимальный суммарный вес вещей, который выдерживает рюкзак (целое число)
        self.__things = []  # список вещей в рюкзаке

    def things(self):
        """Для доступа к локальному приватному атрибуту"""
        return self.__things

    def add_thing(self, thing):
        """Добавление нового предмета в рюкзак
         (добавление возможно, если суммарный вес (max_weight) не будет превышен,
          иначе добавление не происходит)"""

        if self.get_total_weight() + thing.weight <= self.max_weight:
            self.things().append(thing)

    def remove_thing(self, indx):
        """Удаляем предмета из рюкзака по индексу"""
        self.things().pop(indx)

    def get_total_weight(self):
        """Получаем суммарный вес предметов в рюкзаке"""
        total_weight = 0
        for i in self.__things:
            total_weight += i.weight
        return total_weight

#Решение без дескрипторов:
# class Bag:
#     def __init__(self, max_weight):
#         self.max_weight = max_weight
#         self.__current_weight = 0
#         self.__things = list()
#
#     @property
#     def things(self):
#         return self.__things
#
#     def add_thing(self, thing):
#         if self.max_weight - self.__current_weight - thing.weight >= 0:
#             self.__things.append(thing)
#             self.__current_weight += thing.weight
#
#     def remove_thing(self, indx):
#         thing = self.__things.pop(indx)
#         self.__current_weight -= thing.weight
#
#     def get_total_weight(self):
#         return self.__current_weight
#
#
# class Thing:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight

bag = Bag(200)
item1 = Thing('sword', 80)
item2 = Thing('bow', 40)
bag.add_thing(item1)
bag.add_thing(item2)
bag.remove_thing(1)
print(bag.things())

print(bag.get_total_weight())
