class StringDigit(str):
    def __init__(self, inp_string):
        if not inp_string.isdigit():
            raise ValueError("в строке должны быть только цифры")
        else:
            super().__init__()

    def __add__(self, other):
        if not other.isdigit():
            raise ValueError("в строке должны быть только цифры")
        else:
            return StringDigit(str(self) + str(other))

    def __radd__(self, other):
        if not other.isdigit():
            raise ValueError("в строке должны быть только цифры")
        else:
            return StringDigit(self.__class__.__add__(other, self))


sd = StringDigit("123")
assert str(sd) == "123", "неверно работает метод __str__ класса StringDigit"

try:
    sd2 = StringDigit("123a")
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

sd = sd + "345"
assert sd == "123345", "неверно отработал оператор +"

sd = "0" + sd
assert sd == "0123345", "неверно отработал оператор +"

try:
    sd = sd + "12d"
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"

try:
    sd = "12d" + sd
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"