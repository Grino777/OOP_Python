from operator import add, sub


class Matrix:
    def __init__(self, *args):
        if len(args) == 1:
            self.matrix = self.__check_matrix(args[0])
        else:
            self.rows = args[0]
            self.cols = args[1]
            self.fill_value = self.__check_fill_value(args[2])
            self.matrix = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]

    def __add__(self, other):
        res = self.__matrix_arithmetic(other, '+')
        return res

    def __sub__(self, other):
        res = self.__matrix_arithmetic(other, '-')
        return res

    def __getitem__(self, item):
        self.__check_index(*item)
        r, c = item
        return self.matrix[r][c]

    def __setitem__(self, key, value):
        self.__check_index(*key)
        self.__chek_value(value)
        r, c = key
        self.matrix[r][c] = value

    def __matrix_arithmetic(self, other, sign):
        a_dict = {'+': add,
                  '-': sub}
        if isinstance(other, Matrix):
            self.__matrix_size_check(other)
            res_matrix = [[0 for _ in range(len(self.matrix[i]))] for i in range(len(self.matrix))]
            for row in range(len(self.matrix)):
                for col in range(len(self.matrix[0])):
                    res_matrix[row][col] = a_dict[sign](self.matrix[row][col], other.matrix[row][col])
            return Matrix(res_matrix)
        elif isinstance(other, (int, float)):
            res_matrix = [[0 for _ in range(len(self.matrix[i]))] for i in range(len(self.matrix))]
            for row in range(len(res_matrix)):
                for col in range(len(res_matrix[row])):
                    res_matrix[row][col] = a_dict[sign](self.matrix[row][col], other)
            return Matrix(res_matrix)

    def __matrix_size_check(self, other):
        m1 = [len(self.matrix), 0]
        m1[1] = max(list(map(lambda x: len(x), self.matrix)))
        m2 = [len(other.matrix), 0]
        m2[1] = max(list(map(lambda x: len(x), other.matrix)))
        if not m1 == m2:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __chek_value(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')

    def __check_index(self, x, y):
        if not all(map(lambda x: type(x) == int, [x, y])):
            raise IndexError('недопустимые значения индексов')
        if not (0 <= x < len(self.matrix) and 0 <= y < len(self.matrix[0])):
            raise IndexError('недопустимые значения индексов')

    @staticmethod
    def __check_fill_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
        else:
            return value

    def __check_matrix(self, matrix):
        check_matrix = []
        len_row = len(matrix[0])
        for i in matrix:
            check_1 = True if len(i) == matrix[0] or len(i) == len_row else False
            check_matrix.append(all(map(lambda x: type(x) in (int, float), i)))
            check_matrix.append(check_1)
        if all(check_matrix):
            return matrix
        else:
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')


# Тесты:
list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix['0', 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"
