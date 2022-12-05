import random


# Объявите класс RandomPassword для генерации случайных паролей. Объекты этого класса должны создаваться командой:
# rnd = RandomPassword(psw_chars, min_length, max_length)
# Непосредственная генерация одного пароля должна выполняться командой: psw = rnd()

class RandomPassword:
    def __init__(self, psw_chars, min_lenght, max_lenght):
        self.psw_chars = psw_chars  # строка из разрешенных в пароле символов
        self.min_lenght = min_lenght  # минимальная длина генерируемых паролей.
        self.max_lenght = max_lenght  # максимальная длина генерируемых паролей

    def __call__(self, *args, **kwargs):
        pass_lenght = random.randrange(self.min_lenght, self.max_lenght)
        password = [random.choice(self.psw_chars) for i in range(pass_lenght)]
        return ''.join(password)


# список lst_pass из трех сгенерированных паролей объектом rnd класса RandomPassword, созданного с параметрами:
# min_length = 5
# max_length = 20
# psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword('qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*', 5, 20)

lst_pass = [rnd() for _ in range(3)]
print(lst_pass)
