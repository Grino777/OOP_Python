class IntegerValue:
    """дескриптор данных для работы с целыми числами"""

    def __set_name__(self, owner, name):
        self.name = '_' + name
        return self.name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator(value):
            setattr(instance, self.name, value)

    @staticmethod
    def validator(value):
        if isinstance(value, int):
            return True
        else:
            raise ValueError('возможны только целочисленные значения')


class CellInteger:
    """для операций с целыми числами"""
    value = IntegerValue()

    def __init__(self, value=0):
        self.value = value  # начальное значение ячейки (по умолчанию равно 0 и сохраняется в ячейке через дескриптор value)

    # def __repr__(self):
    #     return f'{self.start_value}'


class TableValues:
    """для работы с таблицей в целом
    table = TableValues(rows, cols, cell=CellInteger)"""

    def __init__(self, rows, cols, cell=CellInteger):
        if cell is None:
            raise ValueError('параметр cell не указан')
        else:
            self.rows = rows  # Число строк
            self.cols = cols  # Число столбцов
            self.cell = cell  # Ссылка на класс. Если параметр cell не указан, то генерировать исключение
            self.cells = [[cell() for i in range(self.cols)] for _ in range(self.rows)]

    def __getitem__(self, item):
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        obj = self.cells[key[0]][key[1]]
        obj.value = value


tb = TableValues(3, 2, cell=CellInteger)
tb[0, 0] = 1
assert tb[0, 0] == 1, "некорректно работает запись и/или считывание значения в ячейку таблицы по индексам"

try:
    tb[2, 1] = 1.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

for row in tb.cells:
    for x in row:
        assert isinstance(x, CellInteger), "коллекция cells должна содержать только объекты класса  CellInteger"

cell = CellInteger(10)
assert cell.value == 10, "дескриптор value вернул неверное значение"