class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free

    def __repr__(self):
        return f'{self.value}'

class TicTacToe:
    def __init__(self):
        self.clear()

    def __getitem__(self, item):
        ...

    def __setitem__(self, key, value):
        ...

    def clear(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]

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

game = TicTacToe()
print(game.pole)
