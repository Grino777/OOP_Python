class StackObj:
    def __init__(self, data):
        self.data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class Stack:
    def __init__(self):
        self.top = None
        self._length = 0

    def __len__(self):
        return self._length

    def __getitem__(self, item):
        self.__indx_validator(item)
        for v, i in enumerate(self, start=0):
            if v == item:
                return i.data

    def __setitem__(self, key, value):
        self.__indx_validator(key)
        for v, i in enumerate(self):
            if v == key:
                i.data = value

    def __iter__(self):
        self.temp = self.top
        return self

    def __next__(self):
        if not self.temp is None:
            res = self.temp
            self.temp = self.temp.next
        else:
            raise StopIteration
        return res

    def push_back(self, obj):
        """Добавление нового объекта obj в конец стека"""
        if self.top is None:
            self.top = obj
        else:
            for v, i in enumerate(self, start=0):
                if v == self._length - 1:
                    i.next = obj
        self._length += 1

    def push_front(self, obj):
        """Добавление нового объекта obj в начало стека"""
        if self.top is None:
            self.top = obj
        else:
            obj.next = self.top
            self.top = obj
        self._length += 1

    def __indx_validator(self, indx):
        if indx >= len(self):
            raise IndexError('неверный индекс')


#Тесты:
st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))

assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[
           0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
