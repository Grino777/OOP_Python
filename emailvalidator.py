import random
from string import ascii_lowercase, digits, ascii_uppercase


class EmailValidator:
    def __new__(cls, *args, **kwargs):
        """Запрет на создание экземпляров класса"""
        return None

    @classmethod
    def get_random_email(cls) -> str:
        """Метод класса для создания рандомного email-адреса"""
        email_name = cls.get_random_name()
        email_domain = '@gmail.com'
        return f'{email_name}{email_domain}'

    @classmethod
    def check_email(cls, email: str) -> bool:
        """Проверка emal-адреса на соответсвие заданным параметрам"""
        if isinstance(email, int): #Является ли email числом, а не строкой
            return False
        elif '@' not in email: #Проверка наличия '@' в email
            return  False
        else:
            valid_char = str(ascii_lowercase + digits + '._@' + ascii_uppercase) #Валидные символы
            test_0 = cls.__is_email_str(email) #Проверка приватным методом на входящую строку
            test_1 = set(email).issubset(valid_char) #Проверка на соответстви входящего значения валидным символам
            test_2 = len(email.split('@')[0]) <= 100 and len(email.split('@')[1]) <= 50 # Проверка на длинну имени и домена
            test_3 = True if '.' in email.split('@')[1] else False #Проверка наличия точки в домене
            dot_chk = True #Флаг
            for i in range(len(email)): #Проверка на две подряд идущие точки в email
                try:
                    if email[i] == '.' and email[i + 1] == '.':
                        dot_chk = False
                        break
                except:
                    pass
            return all([test_0, test_1, test_2, test_3, dot_chk])

    @staticmethod
    def __is_email_str(email) -> bool:
        """Проверка на соответствие типа входящих данных"""
        return isinstance(email, str)

    @classmethod
    def get_random_name(cls) -> str:
        """Собираем рандомный email_name"""
        valid_chars = str(ascii_lowercase + digits + '._' + ascii_uppercase) #Валидные символы
        random_digit = random.randrange(1, 49) #Длина
        while True:
            email_name = [random.choice(valid_chars) for _ in range(random_digit)]
            if email_name.count('.') <= 1:
                return ''.join(email_name)

#Немного тестов
assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaa") == True
assert EmailValidator.check_email("i.like.this.course@my.stepik.domen.org") == True
assert EmailValidator.check_email('name.surname@mail.com') == True
assert EmailValidator.check_email(1342) == False
assert EmailValidator.check_email('a+a@m.c') == False
assert EmailValidator.check_email('aabda..kkk@m.c') == False
assert EmailValidator.check_email('aaaa@bbb..cc') == False
assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaaa") == False
assert EmailValidator.check_email(f"{'a' * 101}@{'b' * 45}.aaaa") == False
assert EmailValidator.check_email(f"{'a'}@{'b' * 45}aaaa") == False
assert EmailValidator.check_email('name.surnamemail.com') == False
assert EmailValidator.check_email('name@mail') == False
