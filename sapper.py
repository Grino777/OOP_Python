import random as rnd


class GamePole:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.pole = [[Cell(coord=(i, j)) for j in range(n)] for i in range(n)]
        self.init()
        self.check_mines()

    def show(self):
        for i in self.pole:
            for j in i:
                if j.fl_open == False:
                    print('#', end='')
                if j.fl_open:
                    print(f'{j.around_mines} ', end='')
            print()

    def init(self):
        fields = [j for i in self.pole for j in i]
        for i in rnd.sample(fields, self.m):
            setattr(i, 'mine', True)

    def check_mines(self):
        neightbours = (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)
        for i in range(self.n):
            for j in range(self.n):
                for nb in neightbours:
                    try:
                        if 0 <= i + nb[0] <= self.n ** 2 and 0 <= j + nb[1] <= self.n ** 2:
                            if self.pole[i + nb[0]][j + nb[1]].mine:
                                self.pole[i][j].around_mines += 1
                    except:
                        continue


class Cell:
    def __init__(self, around_mines: int = 0, mine: bool = False, fl_open: bool = False, coord=()):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open
        self.coord = coord


pole_game = GamePole(10, 12)