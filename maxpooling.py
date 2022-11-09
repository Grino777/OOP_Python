class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, *args, **kwargs):
        if self.check_matrix(args[0]):
            return args[0]

    @staticmethod
    def check_matrix(matrix):
        lm = len(matrix)
        for i in matrix:
            if len(i) == lm and all(type(j) in (int, float) for j in i if type(j)):
                continue
            else:
                raise ValueError("Неверный формат для первого параметра matrix.")
        return matrix

mp = MaxPooling(step=(2, 2), size=(2,2))

res = mp([[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 8, 7, 6],
          [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
print(res)
