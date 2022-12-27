class Tuple(tuple):
    def __init__(self, lst):
        if self.__check_iter(lst):
            super().__init__()

    def __add__(self, other):
        if self.__check_iter(other):
            res = tuple(self) + tuple(other)
            return Tuple(res)

    @staticmethod
    def __check_iter(lst):
        try:
            iter_obj = iter(lst)
        except TypeError:
            iter_obj = None
        return iter_obj

t = Tuple([1, 2, 3])
t = t + 'Python'
print(t)