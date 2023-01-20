class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self.__check_triangle()

    def __setattr__(self, key, value):
        self.__value_validator(value)
        self.__dict__[key] = value

    def __value_validator(self, x):
        try:
            if isinstance(x, (int, float)) and x > 0:
                return x
            else:
                raise TypeError('стороны треугольника должны быть положительными числами')
        except:
            raise TypeError('стороны треугольника должны быть положительными числами')

    def __check_triangle(self):
        a, b, c = self._a, self._b, self._c
        if not (a < b + c and b < a + c and c < a + b):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

lst_tr = []

for i in input_data:
    try:
        lst_tr.append(Triangle(*i))
    except:
        pass