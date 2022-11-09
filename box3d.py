class Box3D:
    def __init__(self, w=0, h=0, d=0):
        self.width = w
        self.height = h
        self.depth = d

    def __add__(self, other):
        return Box3D(*self.calculate('+', other))

    def __mul__(self, other):
        return Box3D(*self.calculate('*', other))

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        return Box3D(*self.calculate('-', other))

    def __floordiv__(self, other):
        return Box3D(*self.calculate('//', other))

    def __rfloordiv__(self, other):
        return self // other

    def __mod__(self, other):
        return Box3D(*self.calculate('%', other))

    def __rmod__(self, other):
        return self % other

    def get_coords_list(self):
        return [self.width, self.height, self.depth]

    def calculate(self, sign, obj2):
        math_dict = {
            '+': lambda args: args[0] + args[1],
            '-': lambda args: args[0] - args[1],
            '*': lambda args: args[0] * args[1],
            '//': lambda args: args[0] // args[1],
            '%': lambda args: args[0] % args[1],
        }

        obj_list1 = self.get_coords_list()
        math_func = math_dict.get(sign)
        res = []
        if type(obj2) is Box3D:
            obj_list2 = obj2.get_coords_list()
            for i in list(zip(obj_list1, obj_list2)):
                res.append(math_func(i))
            return res
        elif type(obj2) in (int, float):
            for i in obj_list1:
                res.append(eval(f'{i} {sign} {obj2}'))
            return res

#Лучшее решение:
# from operator import add, sub, mul, floordiv, mod
# class Box3D:
#
#     def __init__(self, *args):
#         self.args = args
#         self.width, self.height, self.depth = args
#         Box3D.__add__      = lambda self, other: Box3D(*map(add, self.args, other.args))
#         Box3D.__sub__      = lambda self, other: Box3D(*map(sub, self.args, other.args))
#         Box3D.__mul__      = lambda self, other: Box3D(*map(lambda x: mul(x, other), self.args))
#         Box3D.__floordiv__ = lambda self, other: Box3D(*map(lambda x: floordiv(x, other), self.args))
#         Box3D.__mod__      = lambda self, other: Box3D(*map(lambda x: mod(x, other), self.args))
#
#         Box3D.__radd__     = lambda self, other: Box3D(*map(add, self.args, other.args))
#         Box3D.__rsub__     = lambda self, other: Box3D(*map(sub, self.args, other.args))
#         Box3D.__rmul__     = lambda self, other: Box3D(*map(lambda x: mul(x, other), self.args))
#         Box3D.__rfloordiv__= lambda self, other: Box3D(*map(lambda x: floordiv(x, other), self.args))
#         Box3D.__rmod__     = lambda self, other: Box3D(*map(lambda x: mod(x, other), self.args))



box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
box = 3 * box2    # Box3D: width=6, height=12, depth=18
box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
box = box2 % 3    # Box3D: width=2, height=1, depth=0