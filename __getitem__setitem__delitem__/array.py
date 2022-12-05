class Integer:
    def __init__(self, digit=0):
        self.digit = digit

    def __repr__(self):
        return f'{self.digit}'

    @property
    def value(self):
        return self.digit

    @value.setter
    def value(self, digit):
        if self.validator(digit):
            self.digit = digit

    def validator(self, digit):
        if isinstance(digit, int):
            return True
        else:
            raise ValueError('должно быть целое число')


class Array:
    def __init__(self, max_lenght, cell=Integer):
        self.max_lenght = max_lenght
        self.array = [cell(0) for _ in range(self.max_lenght)]

    def __getitem__(self, item):
        if self.validator(item):
            return self.array[item].digit

    def __setitem__(self, key, value):
        if self.validator(key):
            self.array[key].value = value

    def __str__(self):
        return ' '.join(list(map(str, self.array)))

    def validator(self, indx):
        if 0 <= indx < len(self.array):
            return True
        else:
            raise IndexError('неверный индекс для доступа к элементам массива')


a = Array(5)
a[0] = 0
print(a)
for i in a.array:
    print(id(i), i)
