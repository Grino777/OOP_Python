from operator import add, sub


class Vector:
    def __init__(self, *args, **kwargs):
        self.check_values(args)
        self.coords = args

    def __len__(self):
        return len(self.coords)

    def __add__(self, other):
        if len(self) == len(other):
            res = tuple(map(add, self.coords, other.coords))
            if VectorInt(*res):
                return VectorInt(*res)
            else:
                return Vector(*res)

    def check_values(self, coords):
        for i in coords:
            if not isinstance(i, (int, float)):
                raise ValueError
        return coords



class VectorInt(Vector):
    def __init__(self, *args, **kwargs):
        super().__init__(args)

    def check_values(self, coords):
        for i in coords:
            if not isinstance(i, int):
                raise ValueError('координаты должны быть целыми числами')


# Тесты:
v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2
print(v)

# assert (v1 + v2).get_coords() == (
# 4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
# assert (v1 - v2).get_coords() == (
# -2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"
#
# v = VectorInt(1, 2, 3, 4)
# assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"
#
# try:
#     v = VectorInt(1, 2, 3.4, 4)
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"
#
# v1 = VectorInt(1, 2, 3, 4)
# v2 = VectorInt(4, 2, 3, 4)
# v3 = Vector(1.0, 2, 3, 4)
#
# v = v1 + v2
# assert type(
#     v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
# v = v1 + v3
# assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
