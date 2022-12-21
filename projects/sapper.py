from random import sample
"""
Реализовать логику игры сапер.
"""

class Cell:
    def __init__(self, is_mine=False, number=0, is_open=False):
        self.__is_mine = is_mine  # булево значение True/False; True - в клетке находится мина, False - мина отсутствует
        self.__number = number  # число мин вокруг клетки (целое число от 0 до 8)
        self.__is_open = is_open  # флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.

    def __bool__(self):
        return self.is_open == True

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, is_mine):
        if type(is_mine) == bool:
            setattr(self, '_Cell__is_mine', is_mine)
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if 0 <= number <= 8:  # Сначала рассчиать количество мин в поле
            setattr(self, '_Cell__number', number)
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, is_open):
        if type(is_open) == bool:
            setattr(self, '_Cell_is_open', is_open)
        else:
            raise ValueError("недопустимое значение атрибута")


class GamePole:
    __address = None

    def __new__(cls, *args, **kwargs):
        if cls.__address is None:
            cls.__address = super().__new__(cls)
            return cls.__address
        else:
            return cls.__address

    def __init__(self, N=0, M=0, total_mines=0):
        self.n = N
        self.m = M
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for _ in range(self.m)] for _ in range(self.n)]
        # self.init_pole()

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        """Для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми)"""
        fields = [j for i in self.pole for j in i]
        for i in sample(fields, self.total_mines):
            setattr(i, '_Cell__is_mine', True)
        for i in range(self.n):
            for j in range(self.m):
                if not self.pole[i][j].is_mine:
                    self.check_mines(p.pole, i, j)

    def __cell_validator(self, i, j):
        """Проверка значений индекса клетки"""
        if 0 <= i < len(self.pole) and 0 <= j < len(self.pole[0]):
            return True
        else:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def open_cell(self, i, j):
        """В методе open_cell() необходимо проверять корректность индексов (i, j). Если индексы указаны некорректно,
            то генерируется исключение командой:
            raise IndexError('некорректные индексы i, j клетки игрового поля')"""
        if self.__cell_validator(i, j):
            cell = self.pole[i][j]
            if not cell.is_open:
                cell.is_open = True

    def show_pole(self):
        """Отображение поля в консоли"""
        game_pole = ''
        for i in self.pole:
            temp = ''
            for j in i:
                temp += 'X ' if j.is_mine else str(j.number) + ' '
            game_pole += temp + '\n'
        return game_pole

    def check_mines(self, pole, i, j):
        """Вычисляем количество мин в соседних полях"""
        for k in range(-1, 2):
            for l in range(-1, 2):
                ii, jj = k + i, l + j
                if ii < 0 or ii > self.n - 1 or jj < 0 or jj > self.m - 1:
                    continue
                if pole[ii][jj].is_mine:
                    self.pole[i][j].number += 1


# Тесты:
p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
    Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
print(p.show_pole())
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1

assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                continue
            if pole[ii][jj].is_mine:
                n += 1

    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, f'{i}-{j}'  # "неверно подсчитано число мин вокруг клетки"
