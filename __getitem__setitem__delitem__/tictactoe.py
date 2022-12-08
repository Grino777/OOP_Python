class Cell:
    def __init__(self):
        self.is_free = True
        self._value = 0

    def __bool__(self):
        return self.is_free

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class TicTacToe:
    def __init__(self):
        self.clear()

    def __getitem__(self, item):
        item = self.__get_coords(item)
        if isinstance(item, Cell):
            return item.value
        else:
            return tuple(i.value for i in item)

    def __setitem__(self, key, value):
        if type(value) == int:
            self.pole[key[0]][key[1]].value = value
        else:
            for v, obj in zip(value, self.__get_coords(key)):
                obj.value = v
        return self

    def clear(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]

    def __get_coords(self, item):
        if list(filter(lambda x: type(x) == slice, item)):
            t_slice = list(filter(lambda x: type(x) == slice, item))
            coords = list(filter(lambda x: type(x) == int, item))
            if type(item[0]) == slice:
                return tuple(i[coords[0]] for i in self.pole)
            else:
                return tuple(self.pole[coords[0]][t_slice[0]])
        return self.pole[item[0]][item[1]] #.value

    @staticmethod
    def __coord_validator(coords):
        for i in coords:
            if type(i) == int and 0 <= i < 3:
                continue
            else:
                raise IndexError('неверный индекс клетки')

    def __value_validator(self, coords, value):
        cell = self.pole[coords[0]][coords[1]]
        if bool(cell):
            if value in (1, 2):
                cell.value = value
        else:
            raise ValueError('клетка уже занята')


g = TicTacToe()
g.clear()
# assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
# g[1, 1] = 1
# g[2, 1] = 2
# assert g[1, 1] == 1 and g[
#     2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"
#
# try:
#     res = g[3, 0]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"
#
# try:
#     g[3, 0] = 5
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

v1 = g[1, :]
print(tuple(v1))