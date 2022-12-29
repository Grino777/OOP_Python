#Решение через дескриптор
# class AnimalDescriptor:
#     def __set_name__(self, owner, name):
#         self.name = '__' + name
#         return self.name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         setattr(instance, self.name, value)


class Animal:
    # name = AnimalDescriptor()
    # kind = AnimalDescriptor()
    # old = AnimalDescriptor()


    def __init__(self, name, kind, old):
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind):
        self.__kind = kind

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old




animals = [Animal('Васька', 'дворовый кот', 5), Animal('Рекс', 'немецкая овчарка', 8), Animal('Кеша', 'попугай', 3) ]
for i in animals:
    print(i.__dict__)
