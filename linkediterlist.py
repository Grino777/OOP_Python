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
        self.length = 0

    def __len__(self):
        if self.top is None:
            return 0
        else:
            temp = self.top
            self.length = 1
            while temp.next != None:
                temp = temp.next
                self.length += 1

    def __getitem__(self, item):
        return self.__iter__(item)

    def __setitem__(self, key, value):
        ...

    def __iter__(self):
        self.temp = self.top
        return self

    def __next__(self):
        for i in range(self.length):
            if not self.temp is None:
                yield self.temp
                self.temp = self.temp.next
            else:
                raise StopIteration

    # def __iter__(self, indx=None):
    #     if isinstance(indx, int):
    #         temp = self.top
    #         for i in range(self.length + 1):
    #             if i == indx:
    #                 return temp
    #             else:
    #                 temp = temp.next
    #                 continue
    #     else:
    #         temp = self.top
    #         for i in range(self.length):
    #             yield temp
    #             temp = temp.next

    def push_back(self, obj):
        """Добавление нового объекта obj в конец стека"""

    def push_front(self, obj):
        """Добавление нового объекта obj в начало стека"""
        if self.top is None:
            self.top = obj
        else:
            obj.next = self.top
            self.top = obj



    # def __indx_validator(self, indx):
    #     if indx > len(self.length):
    #         raise IndexError('неверный индекс')

st = Stack()
st.push_front(StackObj('1'))
st.push_front(StackObj('2'))

for i in st:
    print(list(i))

# print(list(st[1]))

# st = Stack()
# st.push_back(StackObj("1"))
# st.push_front(StackObj("2"))
#
# assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"
#
# st[0] = "0"
# assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"
#
# for obj in st:
#     assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"
#
# try:
#     a = st[3]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"