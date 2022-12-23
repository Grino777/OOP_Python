class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


# здесь объявляйте остальные классы

class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)

    def get(self, request):
        return f'url: {request["url"]}'

    def render_request(self, request, method):
        self.validator(request, method)
        return getattr(self, method.lower())(request)

    def validator(self, request, method):
        if isinstance(request, dict):
            if request.get('url', 0) != 0:
                if method in self.methods:
                    return getattr(self, method.lower())(request)
                else:
                    raise TypeError('данный запрос не может быть выполнен')
            else:
                raise TypeError('request не содержит обязательного ключа url')
        else:
            raise TypeError('request не является словарем')



d = DetailView()
html = d.render_request({'url': 'https://site.ru/home'}, 'GET')
print(html)