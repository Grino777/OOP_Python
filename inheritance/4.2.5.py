class Protists:
    ...


class Plants(Protists):
    ...


class Animals(Protists):
    ...


class Mosses(Plants):
    ...


class Flowering(Plants):
    ...


class Worms(Animals):
    ...


class Mammals(Animals):
    ...


class Human(Mammals):
    ...


class Monkeys(Mammals):
    ...

class Monkey(Monkeys):
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old

class Person(Human):
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old

class Flower(Flowering):
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old

class Worm(Worms):
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old

lst_objs = [Monkey("мартышка", 30.4, 7), Monkey("шимпанзе", 24.6, 8),
            Person("Балакирев", 88, 34), Person("Верховный жрец", 67.5, 45),
            Flower("Тюльпан", 0.2, 1), Flower("Роза", 0.1, 2),
            Worm("червь", 0.01, 1), Worm("червь 2", 0.02, 1)]

lst_animals = [i for i in lst_objs if isinstance(i, Animals)]
lst_plants = [i for i in lst_objs if isinstance(i, Plants)]
lst_mammals  = [i for i in lst_objs if isinstance(i, Mammals)]


