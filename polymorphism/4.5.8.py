from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):
    """Класс связного списка."""

    def __init__(self):
        self._top = None

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
        if self._top is None:
            self._top = obj
        else:
            temp: StackObj = self._top
            while True:
                if temp.get_next_obj():
                    temp = temp.get_next_obj()
                else:
                    # setattr(temp, '_StackObj_next', obj)
                    temp._next = obj
                    break

    def pop_back(self):
        """Удаление последнего объекта из односвязного списка."""
        temp = self._top
        prev = None
        if not temp.get_next_obj() is None:
            while not temp.get_next_obj() is None:
                prev = temp
                temp = temp.get_next_obj()
            prev._next = None
        else:
            self._top = None
        return temp

    def show(self):
        """Вывод списка всех элементов односвязного списка."""
        obj_list = []
        if self._top is None:
            return obj_list
        else:
            temp = self._top
            while True:
                if temp.get_next_obj():
                    obj_list.append(temp)
                    temp = temp.get_next_obj()
                else:
                    obj_list.append(temp)
                    break
        return obj_list


class StackObj(Stack):
    """Класс элеметов связного списка."""

    def __init__(self, data=''):
        """Инициализация элемента связного списка с _date."""
        self._data = data
        self._next = None

    def get_next_obj(self):
        """Получить следущий связный элемент списка"""
        return self._next

assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"

st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1

assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"
