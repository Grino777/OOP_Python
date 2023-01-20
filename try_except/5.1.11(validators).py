class Validator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, *args, **kwargs):
        value = args[0]
        if self.min_value <= value <= self.max_value:
            return value
        else:
            raise ValueError('значение не прошло валидацию')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    def __call__(self, *args, **kwargs):
        if type(args[0]) == float:
            return super().__call__(*args, **kwargs)
        else:
            raise ValueError('значение не прошло валидацию')


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    def __call__(self, *args, **kwargs):
        if type(args[0]) == int:
            return super().__call__(*args, **kwargs)
        else:
            raise ValueError('значение не прошло валидацию')


def is_valid(lst, validators):
    result = []
    for i in lst:
        for v in validators:
            try:
                result.append(v(i))
            except:
                pass
    return result


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)

lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]

print(lst_out)

#Лучшее решение:
# class Validator:
#     def __init__(self, *args):
#         self.min_value, self.max_value = args
#
#     def __call__(self, *args, **kwargs):
#         if not (type(args[0]) == self.type and self.min_value <= args[0] <= self.max_value):
#             raise ValueError('значение не прошло валидацию')
#
#
# class FloatValidator(Validator):
#     type = float
#
#
# class IntegerValidator(Validator):
#     type = int
#
#
# def is_valid(lst, validators):
#     new_list = []
#     for i in lst:
#         for j in validators:
#             try:
#                 j(i)
#                 new_list.append(i)
#             except:
#                 pass
#     return new_list