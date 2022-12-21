class StackObj:
    """Класс элеметов связного списка."""

    def __init__(self, data=''):
        """Инициализация элемента связного списка с __date."""
        self.__data = data
        self.__next = None

    def get_next_obj(self):
        """Получить следущий связный элемент списка"""
        return self.__next


class Stack:
    """Класс связноо списка."""
    def __init__(self):
        self.top = None

    def __add__(self, other):
        """Добавление экз.класса StackObj в связный список."""
        if isinstance(other, StackObj):
            self.push_back(other)
            return self

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    def __mul__(self, other):
        """Добавление нескольких экз.класс StackObj в связный список."""
        if other:
            for i in other:
                self.push_back(StackObj(i))
            return self


    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        return self * other

    def push_back(self, obj):
        """Добавление объекта класса StackObj в конец односвязного списка."""
        if self.top is None:
            self.top = obj
        else:
            temp: StackObj = self.top
            while True:
                if temp.get_next_obj():
                    temp = temp.get_next_obj()
                else:
                    setattr(temp, '_StackObj__next', obj)
                    break

    def pop_back(self):
        """Удаление последнего объекта из односвязного списка."""
        temp = self.top
        prev = None
        if not temp.get_next_obj() is None:
            while not temp.get_next_obj() is None:
                prev = temp
                temp = temp.get_next_obj()
            setattr(prev, '_StackObj__next', None)
        else:
            self.top = None

    def show(self):
        """Вывод списка всех элементов односвязного списка."""
        obj_list = []
        if self.top is None:
            return obj_list
        else:
            temp = self.top
            while True:
                if temp.get_next_obj():
                    obj_list.append(temp)
                    temp = temp.get_next_obj()
                else:
                    obj_list.append(temp)
                    break
        return obj_list

#Тесты:
assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"