class Cell:
    def __init__(self):
        ...


class GamePole:
    __address = None

    def __new__(cls, *args, **kwargs):
        if cls.__address is None:
            cls.__address =  super().__new__(cls)
            return cls.__address
        else:
            return cls.__address

    def __init__(self, N, M, total_mines):
        self.n = N
        self.m = M
        self.total_mines = total_mines
        self.__pole_cells = ((Cell() for _ in range(self.n)) for _ in range(self.m))

    # def init_pole(self):
    #     ...

    def get_pole(self):
        return self.__pole_cells

g1 = GamePole(5, 5, 5)
print(g1.get_pole())
# for i in g1.get_pole():
#     print(i)
