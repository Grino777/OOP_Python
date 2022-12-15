class Cell:
    """Класс для ячейки таблицы"""
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class TableValues:
    """Класс таблицы"""
    def __init__(self, rows=0, cols=0, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = [[Cell(0) for _ in range(self.cols)] for _ in range(self.rows)]

    def __iter__(self):
        for row in self.table:
            yield (i.data for i in row)


    def __getitem__(self, item):
        self.__indx_validator(*item)
        r, c = item
        return self.table[r][c].data

    def __setitem__(self, key, value):
        self.__indx_validator(*key)
        self.__type_validator(type(value))
        r, c = key
        self.table[r][c] = Cell(value)

    def __indx_validator(self, row, col):
        """Проверка корректности индкса"""
        if not 0 <= row < self.rows and 0 <= col < self.cols:
            raise IndexError('неверный индекс')

    def __type_validator(self, value):
        """Проверка данных ячейки на заданный тип"""
        if not value is self.type_data:
            raise TypeError('неверный тип присваиваемых данных')


# table = TableValues(5, 3, int)
#
# table[4, 2] = 5
#
# for i in table:
#     for j in i:
#         print(j, end=' ')
#     print()

tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(
            value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"
