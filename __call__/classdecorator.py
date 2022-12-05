'''Необходимо объявить класс-декоратор с именем Handler, который можно было бы применять к функциям следующим образом:

@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"
    '''

class Handler:
    def __init__(self, methods=('GET',)):
        '''аргумент methods декоратора Handler содержит список разрешенных запросов для обработки'''
        self.methods = methods

    def __call__(self, func):
        def wrapper(request: dict, *args, **kwargs):
            method = request.get('method', 'GET')
            if method in self.methods:
                if method == 'GET':
                    return self.get(func, request, *args, *kwargs)
                elif method == 'POST':
                    return self.post(func, request, *args, *kwargs)
            else:
                return None
        return wrapper

    def get(self, func, request, *args, **kwargs):
        '''Метод для get-запросов'''
        response = func(request)
        return f'GET: {response}'

    def post(self, func, request, *args, **kwargs):
        '''Метод для post-запросов'''
        response = func(request)
        return f'POST: {response}'


# Тесты:
assert hasattr(Handler, 'get') and hasattr(Handler, 'post'), "класс Handler должен содержать методы get и post"

@Handler(methods=('GET', 'POST'))
def contact2(request):
    return "контакты"

assert contact2({"method": "POST"}) == "POST: контакты", "декорированная функция вернула неверные данные"
assert contact2({"method": "GET"}) == "GET: контакты", "декорированная функция вернула неверные данные"
assert contact2({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
print(contact2({}))
assert contact2({}) == "GET: контакты", "декорированная функция вернула неверные данные при указании пустого словаря"

@Handler(methods=('POST'))
def index(request):
    return "index"

assert index({"method": "POST"}) == "POST: index", "декорированная функция вернула неверные данные"
assert index({"method": "GET"}) is None, "декорированная функция вернула неверные данные"
assert index({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
