import random


class Cell:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self, value=FREE_CELL):
        self.value = value

    def __bool__(self):
        """возвращает True, если клетка свободна (value = 0) и False - в противном случае"""
        return True if self.value == 0 else False


class TicTacToe:
    def __getitem__(self, item):
        self.__indx_validator(item)
        r, c = item
        return self.pole[r][c]

    def __setitem__(self, key, value):
        self.__indx_validator(key)
        self.__value_validator(value)
        r, c = key
        self.pole[r][c] = Cell(value)

    def __bool__(self):
        """возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном случае."""
        for i in self.pole:
            for j in i:
                if j.value == 0:
                    return True
        return False

    def init(self):
        """инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);"""
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]

    def show(self):
        """отображение текущего состояния игрового поля (как именно - на свое усмотрение);"""
        ttt_dict = {
            0: '-',
            1: 'X',
            2: 'O'
        }
        for i in self.pole:
            for j in i:
                print(ttt_dict[j.value], end=' ')
            print()

    def human_go(self):
        """реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);"""
        # indx = input('Введите координаты клетки: ')
        # indx = list(map(int, indx.split(' ')))
        # self.__indx_validator(indx)
        res = self.__get_free_cells()
        if res:
            indx = random.sample(res, 1)
            self.__setitem__(*indx, Cell.HUMAN_X)


    def computer_go(self):
        """реализация хода компьютера (ставит случайным образом нолик в свободную клетку)."""
        res = self.__get_free_cells()
        if res:
            indx = random.sample(res, 1)
            self.__setitem__(*indx, Cell.COMPUTER_O)


    def is_human_win(self):
        """возвращает True, если победил человек, иначе - False;"""
        ...

    def is_computer_win(self):
        """возвращает True, если победил компьютер, иначе - False;"""
        ...

    def is_draw(self):
        """возвращает True, если ничья, иначе - False."""
        ...

    def __indx_validator(self, indx):
        if all(list(map(lambda x: type(x) == int, indx))):
            r, c = indx
            if not (0 <= r < 3 and 0 <= c < 3):
                raise IndexError('некорректно указанные индексы')
        else:
            raise IndexError('некорректно указанные индексы')

    def __value_validator(self, value):
        if not value in (Cell.HUMAN_X, Cell.COMPUTER_O):
            raise ValueError('некорректно указанно значение для клетки')

    def __get_free_cells(self):
        res = []
        for r in range(len(self.pole)):
            for c in range(len(self.pole[r])):
                if self.pole[r][c].value == 0:
                    res.append([r, c])
        return res

    def __get_result_matrix(self):
        res = []
        for i in range(3):
            res.append(self.pole[i][:])
            ...


game = TicTacToe()
game.init()
step = 0
while bool(game):
    game.human_go()
    step += 1
    game.computer_go()
    step += 1
game.show()

# Тесты:
# cell = Cell()
# assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
# assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
# cell.value = 1
# assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"
#
# assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"
#
# game = TicTacToe()
# assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
# assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
# game[1, 1] = TicTacToe.HUMAN_X
# assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"
#
# game[0, 0] = TicTacToe.COMPUTER_O
# assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"
#
# game.init()
# assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"
#
# try:
#     game[3, 0] = 4
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"
#
# game.init()
# assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"
#
# game[0, 0] = TicTacToe.HUMAN_X
# game[1, 1] = TicTacToe.HUMAN_X
# game[2, 2] = TicTacToe.HUMAN_X
# assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
#
# game.init()
# game[0, 0] = TicTacToe.COMPUTER_O
# game[1, 0] = TicTacToe.COMPUTER_O
# game[2, 0] = TicTacToe.COMPUTER_O
# assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
