class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def __call__(self, *args, **kwargs):
        return self.is_valid(*args, **kwargs)

    def is_valid(self, string):
        flag = True
        if self.chars:
            flag = False
            for i in self.chars:
                if i in string:
                    flag = True
                    break
        if not (self.min_length <= len(string) <= self.max_length and flag):
            raise ValueError('недопустимая строка')
        else:
            return string

class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator

    def form(self, request: dict):
        for i in ['password', 'login']:
            if not request.get(i):
                raise TypeError('в запросе отсутствует логин или пароль')
            else:
                self._login = self.login_validator(request.get('login'))
                self._password = self.password_validator(request.get('password'))

login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
# login, password = input().split()
login, password = 'sergey', 'balakirev!'
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
