class RenderDigit:
    def __call__(self, *args, **kwargs):
        try:
            return int(args[0])
        except ValueError:
            return None


class InputValues:
    def __init__(self, render):  # render - ссылка на функцию или объект для преобразования
        self.__render = render

    def __call__(self, func):  # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            is_digits = args[0].split()
            digits_list = []
            valid = RenderDigit()
            for i in is_digits:
                digits_list.append(valid(i))
            return digits_list

        return wrapper


@InputValues(render=RenderDigit)
def input_dg(string):
    return string


res = input_dg("1 -5.3 0.34 abc 45f -5")
print(res)

#Лучшее решение:
# class InputValues:
#     def __init__(self, render):
#         self.render = render
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             return list(map(self.render, func().split()))
#         return wrapper
#
#
# class RenderDigit:
#     def __call__(self, string):
#         if string[0] == '-' and string[1:].isdigit() or string.isdigit():
#             return int(string)
#
#
# @InputValues(RenderDigit())
# def input_dg():
#     return input()
#
#
# print(input_dg())
