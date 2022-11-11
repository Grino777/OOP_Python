import numpy as np

class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step_v, self.step_h = step
        self.size_v, self.size_h = size

    def __call__(self, *args, **kwargs):
        matrix = args[0] #Сама матрица
        if self.check_matrix(matrix): #Проверка матрицы на соответствие содержащихся значений
            for i in range(0, len(matrix), self.step_v): #Берем строки матрицы с шагом по вертикали
                # print(matrix[i:i+self.step_v])
                parts = matrix[i:i+self.step_v] #Полчуенные строки матрицы присваиваем в переменную
                return self.split_parts(parts)


    def split_list(self, m_list:list):
        res = []
        if len(m_list) >= self.step_h:
            ...

    def split_parts(self, parts:list=[]): #Принимает список с разным количеством подспиков. Например: [[1, 2, 3, 4], [5, 6, 7, 8]]
        if len(parts) == self.step_h:
            res = [[] for i in range(len(parts))]
            for i in parts:
                self.split_list(i)


    @staticmethod
    def check_matrix(matrix):
        lm = len(matrix)
        for i in matrix:
            if len(i) == lm and all(type(j) in (int, float) for j in i if type(j)):
                continue
            else:
                raise ValueError("Неверный формат для первого параметра matrix.")
        return True

mp = MaxPooling(step=(2, 2), size=(2,2))

# matrix = [[5, 0, 88, 2, 7,  65],
#           [1, 33, 7, 45, 0,  1],
#           [54, 8, 2, 38, 22, 7],
#           [73, 23, 6, 1, 15, 0],
#           [4, 12, 9, 1, 76,  6],
#           [0, 15, 10, 8, 11, 78],]
#
# matrix = [[1, 5, 2],
#           [7, 0, 1],
#           [4, 10, 3]]

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 8, 7, 6],
          [5, 4, 3, 2]]

res = mp(matrix)

# res = mp([[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 8, 7, 6],
#           [5, 4, 3, 2]])    # [[6, 8], [9, 7]]

print(res)