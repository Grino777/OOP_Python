# Задание
"""В нейронных сетях использую операцию под названием Max Pooling. Суть ее состоит в сканировании прямоугольной таблицы
 чисел (матрицы) окном определенного размера (обычно, 2x2 элемента) и выбора наибольшего значения в пределах этого окна:

Или, если окна выходят за пределы матрицы, то они пропускаются (игнорируются):

Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем MaxPooling, объекты которого создаются командой:
    mp = MaxPooling(step=(2, 2), size=(2,2))
где step - шаг смещения окна по горизонтали и вертикали; size - размер окна по горизонтали и вертикали.

Параметры step и size по умолчанию должны принимать кортеж со значениями (2, 2).

Для выполнения операции Max Pooling используется команда:

res = mp(matrix)
где matrix - прямоугольная таблица чисел; res - ссылка на результат обработки таблицы matrix (должна создаваться новая таблица чисел.

Прямоугольную таблицу чисел следует описывать вложенными списками. Если при сканировании таблицы часть окна выходит за ее пределы, то эти данные отбрасывать (не учитывать все окно).

Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение, то должно генерироваться исключение командой:

raise ValueError("Неверный формат для первого параметра matrix.")
Пример использования класса (эти строчки в программе писать не нужно):

mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]"""


# Мое решение:
class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step_v, self.step_h = step
        self.size_v, self.size_h = size

    def __call__(self, *args, **kwargs):
        """При вызове класса с аргументом в виде матрицы, в временную пременную temp попадают строки(срезы)
        матрицы с размером 'квадрата' по вертикали.
        Затем они передаются в функцию self.split_parts"""
        matrix = args[0]
        if self.check_matrix(matrix):
            start_v = 0
            res = []
            while True:
                if len(matrix[start_v:start_v + self.size_v]) == self.size_v:
                    temp = matrix[start_v:start_v + self.step_v]
                    res.append(self.split_parts(temp))
                    start_v += self.step_v
                else:
                    break
            return res

    def split_parts(self, lines: list):
        """'Разбивает' каждую входящую строку(срез) матрицы на подсписки в соответствии с размером 'квадрата'
        и его шага.
        Затем передает эти данные в функцию self.__get_max_in_line для вычисления максимального значения в 'квадрате'"""

        res = []
        for i in lines:
            start_h = 0
            temp = []
            while start_h <= len(i):
                if len(i[start_h:start_h + self.size_h]) == self.size_h:
                    temp.append(i[start_h:start_h + self.size_h])
                    start_h += self.step_h
                else:
                    break
            res.append(temp)
        res = list(zip(*res))
        max_digits = []
        for i in res:
            max_digits.append(self.__get_max_in_line(i))
        return max_digits

    def __get_max_in_line(self, line: tuple):
        """Метод для вычисления максимального значения в 'квадрате' матрицы."""
        res = []
        for i in line:
            res.extend(i)
        return max(res)

    @staticmethod
    def check_matrix(matrix):
        """Проверка матрицы на 'квадратность' и соответствие ее данныех типам int, float. """
        lm = len(matrix)
        for i in matrix:
            if len(i) == lm and all(type(j) in (int, float) for j in i if type(j)):
                continue
            else:
                raise ValueError("Неверный формат для первого параметра matrix.")
        return True


# Тесты:
mp = MaxPooling(step=(2, 2), size=(2, 2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2, 2))
m3 = [[1, 12, 14, 12],
      [5, 10, 0, -5],
      [0, 1, 2, 300],
      [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"

# Лучшее решение:
# class MaxPooling:
#     def __init__(self, step: tuple = (2, 2), size: tuple = (2, 2)) -> None:
#         self.step = step
#         self.size = size
#
#     def validateMatrix(self, matrix: list) -> None:
#         rowLength = len(matrix[0])
#         if all(len(row) == rowLength for row in matrix):
#             if all(type(i) in (int, float) for row in matrix for i in row):
#                 return
#         raise ValueError("Неверный формат для первого параметра matrix.")
#
#     def __call__(self, matrix: list) -> list:
#         self.validateMatrix(matrix)
#
#         rangeI = range(self.size[1], len(matrix) + 1, self.step[1])
#         rangeJ = range(self.size[0], len(matrix[0]) + 1, self.step[0])
#
#         return [[max(matrix[y][x]
#                      for y in range(i - self.size[1], i)
#                      for x in range(j - self.size[0], j)
#                      ) for j in rangeJ]
#                 for i in rangeI]
