def class_log(lst):
    def wrapper(*args, **kwargs):
        methods = {k: v for k, v in args[0].__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(args[0], k, decorator_method(v))
        return args[0]

    def decorator_method(func):
        def wrapper_two(*args, **kwargs):
            lst.append(func.__name__)
            return func(*args, **kwargs)

        return wrapper_two

    return wrapper


vector_log = []  # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
print()
print(vector_log)
