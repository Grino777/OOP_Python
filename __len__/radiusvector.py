"""
Объявите класс с именем RadiusVector для описания и работы с n-мерным вектором (у которого n координат).
Объекты этого класса должны создаваться командами:
    # создание 5-мерного радиус-вектора с нулевыми значениями координат (аргумент - целое число больше 1)
    vector = RadiusVector(5)  # координаты: 0, 0, 0, 0, 0

    # создание 4-мерного радиус-вектора с координатами: 1, -5, 3.4, 10 (координаты - любые целые или вещественные числа)
    vector = RadiusVector(1, -5, 3.4, 10)

То есть, при передаче одного значения, оно интерпретируется, как размерность нулевого радиус-вектора. Если же передается более одного числового аргумента, то они интерпретируются, как координаты радиус-вектора.

Класс RadiusVector должен содержать методы:

set_coords(coord_1, coord_2, ..., coord_N) - для изменения координат радиус-вектора;
get_coords() - для получения текущих координат радиус-вектора (в виде кортежа).
"""


class RadiusVector:
    def __init__(self, *args, **kwargs):
        self.points = self.check_coords(args)

    def check_coords(self, coords):
        """Проверка входящих координат"""
        point_dict = {}
        if len(coords) == 1:
            if coords[0] > 1:
                for num, _ in enumerate(range(coords[0]), start=1):
                    point_dict.update({num:0})
        else:
            for num, i in enumerate(coords, start=1):
                point_dict.update({num:i})
        return point_dict

    def set_coords(self, *args, **kwargs):
        new_coords = self.check_coords(args)
        self.points.update(new_coords)

    def get_coords(self):
        return tuple(self.points.values())

    def __len__(self):
        return len(self.points)

    def __abs__(self):
        return sum(i**2 for i in tuple(self.points.values()))**0.5


#Тесты:
vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
print(res_len)
print(res_abs)
print(vector3D.get_coords())