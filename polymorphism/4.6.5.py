class Digit:
    def __init__(self, value):
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value

class Integer(Digit):
    def __init__(self, value):
        if type(value) != int:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class Float(Digit):
    def __init__(self, value):
        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class Positive(Digit):
    def __init__(self, value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class Negative(Digit):
    def __init__(self, value):
        if value >= 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super().__init__(value)

class FloatPositive (Float, Positive):
    def __init__(self, value):
        super().__init__(value)

pn1 = PrimeNumber(3)
pn2 = PrimeNumber(5)
pn3 = PrimeNumber(7)

fp1 = FloatPositive(1.4)
fp2 = FloatPositive(1.9)

digits = [pn1, pn2, pn3, fp1, fp2]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float  = list(filter(lambda x: isinstance(x, Float), digits))

print(lst_positive)
print(lst_float)

