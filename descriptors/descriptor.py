class FloatValue:
    """Дескриптор класса"""

    def __set_name__(self, owner, name):
        self.name = '_' + name
        return self.name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.float_check(value):
            setattr(instance, self.name, value)
        else:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def float_check(self, value):
        return isinstance(value, float)


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value

class TableSheet:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]


table = TableSheet(5, 3)
print(table.cells)
n = 1.0
for i in range(5):
    for j in range(3):
        table.cells[i][j] = Cell(n)
        n += 1.0
#
for i in table.cells:
    print(i)

res = [int(x.value) for row in table.cells for x in row]
print(res)
