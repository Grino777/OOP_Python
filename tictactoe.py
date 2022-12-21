import random


class Cell:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self, value=0):
        self.value = value

    def __getitem__(self, item):
        return self.value

    def __bool__(self):
        """возвращает True, если клетка свободна (value = 0) и False - в противном случае"""
        return True if self.value == 0 else False


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]
        self.winner = None
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False
        self.__free_cells = self.__get_free_cells()

    def __getitem__(self, item):
        self.__indx_validator(item)
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.__indx_validator(key)
        self.__value_validator(value)
        r, c = key
        self.pole[r][c] = Cell(value)
        self.__check_result(value)

    def __bool__(self):
        """возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном случае."""
        if self.winner is None:
            return True
        else:
            return False

    def init(self):
        """инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);"""
        self.__init__()

    def show(self):
        """отображение текущего состояния игрового поля (как именно - на свое усмотрение);"""
        for i in self.pole:
            for j in i:
                print(j.value, end=' ')
            print()

    def human_go(self):
        """реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);"""
        if self.__free_cells and self.winner is None:
            indx = random.sample(self.__free_cells, 1)
            self.__free_cells.remove(*indx)
            self.__setitem__(*indx, Cell.HUMAN_X)
            self.__check_result(Cell.HUMAN_X)

    def computer_go(self):
        """реализация хода компьютера (ставит случайным образом нолик в свободную клетку)."""
        if self.__free_cells and self.winner is None:
            indx = random.sample(self.__free_cells, 1)
            self.__free_cells.remove(*indx)
            self.__setitem__(*indx, Cell.COMPUTER_O)
            self.__check_result(Cell.COMPUTER_O)

    def is_human_win(self):
        """возвращает True, если победил человек, иначе - False;"""
        return self.is_human_win

    def is_computer_win(self):
        """возвращает True, если победил компьютер, иначе - False;"""
        return self.is_computer_win

    def is_draw(self):
        """возвращает True, если ничья, иначе - False."""
        return self.is_draw

    def __indx_validator(self, indx):
        """Проверка индекса"""
        if all(list(map(lambda x: type(x) == int, indx))):
            r, c = indx
            if not (0 <= r < 3 and 0 <= c < 3):
                raise IndexError('некорректно указанные индексы')
        else:
            raise IndexError('некорректно указанные индексы')

    def __value_validator(self, value):
        """Проверка входящего значения"""
        if not value in (Cell.HUMAN_X, Cell.COMPUTER_O):
            raise ValueError('некорректно указанно значение для клетки')

    def __get_free_cells(self):
        """Получаем свободные для хода клетки"""
        res = []
        for r in range(len(self.pole)):
            for c in range(len(self.pole[r])):
                if self.pole[r][c].value == 0:
                    res.append([r, c])
        return res

    def __check_result(self, sign):
        """Прроверка на strike"""
        # Check row:
        if not self.winner:
            for i in self.pole:
                if len(set(map(lambda x: x.value, i))) == 1 and i[0].value == sign:
                    self.winner = True
                    if sign == 1:
                        self.is_human_win = True
                    else:
                        self.is_computer_win = True

        # Check col:
        if not self.winner:
            for i in range(3):
                res = []
                for j in range(3):
                    res.append(self.pole[j][i])
                if len(set(map(lambda x: x.value, res))) == 1 and res[0].value == sign:
                    self.winner = True
                    if sign == 1:
                        self.is_human_win = True
                    else:
                        self.is_computer_win = True

        if not self.winner:
            h = [self.pole[0][0], self.pole[1][1], self.pole[2][2]]
            v = [self.pole[-1][0], self.pole[-2][-1], self.pole[-3][-1]]

            for i in [h, v]:
                if len(set(map(lambda x: x.value, i))) == 1 and i[0].value == sign:
                    self.winner = True
                    if sign == 1:
                        self.is_human_win = True
                    else:
                        self.is_computer_win = True

        if not self.__free_cells and self.winner is None:
            self.is_draw = True
            self.winner = True


# Тесты:
cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

#Лучшее решение:
# from random import randint
#
#
# class TicTacToe:
#     FREE_CELL = 0  # свободная клетка
#     HUMAN_X = 1  # крестик (игрок - человек)
#     COMPUTER_O = 2 # нолик (игрок - компьютер)
#
#     def __init__(self, space='_', human='X', computer='O'):
#         self.d = {self.FREE_CELL: space,
#                   self.HUMAN_X: human,
#                   self.COMPUTER_O: computer}
#
#     def find_strike(self, who):  # 1 - human, 2 - computer
#         rows = any(all(self[row, i].value == who for i in [0, 1, 2]) for row in [0, 1, 2])
#         cols = any(all(self[i, col].value == who for i in [0, 1, 2]) for col in [0, 1, 2])
#         diag1 = all(self[i, i].value == who for i in [0, 1, 2])
#         diag2 = all(self[2-i, i].value == who for i in [0, 1, 2])
#
#         return any([rows, cols, diag1, diag2])
#
#     @property
#     def is_human_win(self):
#         return self.find_strike(self.HUMAN_X)
#
#     @property
#     def is_computer_win(self):
#         return self.find_strike(self.COMPUTER_O)
#
#     @property
#     def is_nobody_win(self):
#         return not (self.is_human_win or self.is_computer_win)
#
#     @property
#     def any_free_space(self):
#         for i in [0, 1, 2]:
#             for j in [0, 1, 2]:
#                 if self[i, j].is_free:
#                     return True
#         return False
#
#     @property
#     def is_draw(self):
#         return not self.any_free_space and self.is_nobody_win
#
#     def __bool__(self):
#         return self.any_free_space and self.is_nobody_win
#
#     def human_go(self):  # c защитой от дурака и различными комментариями
#         message = 'Пожалуйста введите координаты: '
#         while True:
#             try:
#                 x, y = map(int, input(message).split())
#                 self[x, y] = self.HUMAN_X
#                 break
#             except Warning:
#                 print('Клетка уже занята!')
#             except ValueError:
#                 print('Координаты - два целых числа!')
#             except IndexError:
#                 print('Клетки с данными координатами не существует!')
#             message = 'Повторите попытку: '
#
#     def computer_go(self):  # ИИ в разработке. пока рандом
#         x = randint(0, 2)
#         y = randint(0, 2)
#         while not self[x, y].is_free:
#             x = randint(0, 2)
#             y = randint(0, 2)
#         self[x, y] = self.COMPUTER_O
#
#     def show(self):  # console
#         for row in self.pole:
#             print(' '.join(self.d[row[col].value] for col in [0, 1, 2]))
#
#     def __getitem__(self, key):
#         return self.pole[key[0]][key[1]]
#
#     def __setitem__(self, item, value):
#         cell = self.pole[item[0]][item[1]]
#         if cell:
#             cell.value = value
#         else:
#             raise Warning('клетка уже занята')
#
#     def clear(self):
#         self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
#
#     def init(self):
#         self.clear()
#         self.step_game = 0
#
#     def start_console_game(self):
#         self.init()
#
#         while self:
#             if self.step_game % 2 == 0:
#                 self.human_go()
#             else:
#                 print('Ход компьютера: ')
#                 self.computer_go()
#             self.show()
#             self.step_game += 1
#
#         if self.is_human_win:
#             print("Поздравляем! Вы победили!")
#         elif self.is_computer_win:
#             print("Все получится, со временем")
#         else:
#             print("Ничья.")
#
#
# class Cell:
#     def __init__(self):
#         self.value = 0
#
#     @property
#     def is_free(self):
#         return not self.value
#
#     def __bool__(self):
#         return self.is_free
#
#
# game = TicTacToe()
# while input('Вы хотите играть? [д/н]: ').lower() in ('y', 'д'):
#     game.init()
#     game.start_console_game()