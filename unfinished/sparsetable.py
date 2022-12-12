#3.8_11
class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    """Вам необходимо описывать в программе очень большие и разреженные таблицы данных (с большим числом пропусков).
    Для этого предлагается объявить класс SparseTable, объекты которого создаются командой:
        -st = SparseTable()
    -При удалении/добавлении новой ячейки должны автоматически пересчитываться атрибуты rows, cols объекта класса SparseTable.
    -Если происходит попытка удалить несуществующую ячейку, то должно генерироваться исключение:
        raise IndexError('ячейка с указанными индексами не существует')
    -Хранить ячейки следует в словаре, ключами которого являются индексы (кортеж) i, j, а значениями - объекты класса Cell
    -Также с объектами класса SparseTable должны выполняться команды:
        res = st[i, j] # получение данных из таблицы по индексам (i, j)
        st[i, j] = value # запись новых данных по индексам (i, j)
    -При записи новых значений их следует менять в существующей ячейке или добавлять новую, если ячейка с индексами (i, j)
     отсутствует в таблице. (Не забывайте при этом пересчитывать атрибуты rows и cols)"""

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.data = {}

    def __getitem__(self, item):
        if self.__coord_validator(*item):
            res = self.data.get(item, 0)
            if isinstance(res, Cell):
                return res.value
            else:
                raise ValueError('данные по указанным индексам отсутствуют')

    def __setitem__(self, key, value):
        if self.__coord_validator(*key):
            if not self.data.get(key):
                self.data.update({key: Cell(value)})
                self.__calc_table()

    def add_data(self, row, col, data):
        """добавление данных data (объект класса Cell) в таблицу по индексам row, col (целые неотрицательные числа)"""
        if isinstance(data, Cell):
            self.data.update({(row, col): data})
            self.__calc_table()

    def remove_data(self, row, col):
        """удаление ячейки (объект класса Cell) с индексами (row, col)"""
        if self.data.get((row, col)):
            del self.data[(row, col)]
        else:
            raise IndexError('ячейка с указанными индексами не существует')


    def __coord_validator(self, row, col):
        if 0 <= row <= self.rows and 0 <= col <= self.cols:
            return True
        else:
            raise IndexError('ячейка с указанными индексами не существует')

    def __calc_table(self):
            self.rows = max(self.data, key=lambda x: x[0])[0] + 1
            self.cols = max(self.data, key=lambda x: x[1])[1] + 1

#Тесты
st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))

assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"
