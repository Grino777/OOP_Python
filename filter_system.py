import time

class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.filters = [None, None, None]

    def add_filter(self, slot_num, filter):
        check_dict = {
            1: isinstance(filter, Mechanical) and self.filters[slot_num - 1] is None,
            2: isinstance(filter, Aragon) and self.filters[slot_num - 1] is None,
            3: isinstance(filter, Calcium) and self.filters[slot_num - 1] is None,
        }
        if check_dict[slot_num]:
            self.filters[slot_num - 1] = filter
        else:
            print('Установка неозможна')

    def remove_filter(self, slot_num):
        self.filters[slot_num - 1] = None
        print(f'Фильтр из {slot_num} слота удален')

    def get_filters(self):
        return (*self.filters,)

    def water_on(self):
        """Метод water_on() должен возвращать значение True при выполнении следующих условий:
            - все три фильтра установлены в слотах;
            - все фильтры работают в пределах срока службы (значение (time.time() - date) должно быть в пределах [0; MAX_DATE_FILTER])"""
        for filter in self.filters:
            if filter and 0 <= (time.time() - filter.date) <= float(self.MAX_DATE_FILTER):
                continue
            else:
                return False
        return True


class Mechanical:
    def __init__(self, date: int):
        self.date = date
        print(f'Создан объект - {self}')

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, date: int):
        self.date = date

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, date: int):
        self.date = date

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            object.__setattr__(self, key, value)


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
print(w)
# f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
# my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
# my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно

