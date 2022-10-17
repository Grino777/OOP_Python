'''Необходимо объявить класс-декоратор с именем HandlerGET, который будет имитировать обработку GET-запросов
     на стороне сервера. Для этого сам класс HandlerGET нужно оформить так,
      чтобы его можно было применять к любой функции как декоратор'''

class HandlerGET:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        return self.get(self.__func, args[0])

    def get(self, func, request, *args, **kwargs):
        if request.get('method') == 'GET' or request.get('method') is None:
            resp_func = self.__func(request)
            return f'GET: {resp_func}'
        return None


@HandlerGET
def index(request):
    return "главная страница сайта"


res = index({"method": "GET"})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
res = index({"method": "POST"})
print(res)
assert res is None, "декорированная функция вернула неверные данные"
res = index({"method": "POST2"})
print(res)
assert res is None, "декорированная функция вернула неверные данные"

res = index({})
print(res)
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
