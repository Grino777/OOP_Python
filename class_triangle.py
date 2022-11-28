class TriangleDescriptor:
    """Дескриптор для класса Triangle"""
    def __set_name__(self, owner, name):
        self.name = '_' + name
        return self.name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator(value):
            setattr(instance, self.name, value)

    def validator(self, value):
        if isinstance(value, (int, float)):
            return value


class Triangle:
    a = TriangleDescriptor()
    b = TriangleDescriptor()
    c = TriangleDescriptor()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.check_triangle(self.a, self.b, self.c)

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = len(self) / 2
        s = ((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5)
        return s

    @staticmethod
    def check_triangle(a, b, c):
        if not (a < b + c and b < a + c and c < a + b):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

#Тесты:
tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"
