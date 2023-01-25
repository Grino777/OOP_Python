class Test:
    def __init__(self, descr):
        self.descr = self.validator(descr)


    def validator(self, descr):
        if 10 <= len(descr) <= 10000:
            return descr
        else:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        self.descr = super().__init__(descr)
        self.ans_digit = ans_digit  # верный числовой ответ на тест
        self.max_error_digit = max_error_digit

    def __setattr__(self, key, value):
        if key == 'descr':
            self.__dict__[key] = value
        else:
            if type(value) not in (int, float):
                raise ValueError('недопустимые значения аргументов теста')
            if key == 'max_error_digit':
                if value < 0:
                    raise ValueError('недопустимые значения аргументов теста')
            self.__dict__[key] = value

    def run(self):
        ans = float(input())
        min = self.ans_digit - self.max_error_digit
        max = self.ans_digit + self.max_error_digit
        if min <= ans <= max:
            return True
        else:
            return False


descr, ans = map(str.strip, input().split('|'))
try:
    testAnsDigit = TestAnsDigit(descr, float(ans))
    print(testAnsDigit.run())
except Exception as e:
    print(e)

# try:
#     test = Test('descr')
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError при вызове инициализатора класса Test с неверным набором аргументов"
#
# try:
#     test = Test('descr ghgfhgjg ghjghjg')
#     test.run()
# except NotImplementedError:
#     assert True
# else:
#     assert False
#
# assert issubclass(TestAnsDigit, Test)
#
# t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1)
# t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, 0.5)
#
# try:
#     t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, -0.5)
# except ValueError:
#     assert True
# else:
#     assert False
