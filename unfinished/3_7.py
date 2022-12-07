class StackObj:
    def __init__(self, data=''):
        self.data = data
        self.next_obj = None

    def __repr__(self):
        return f'{self.data}'

    @property
    def next(self):
        return self.next_obj

    @next.setter
    def next(self, obj):
        setattr(self, 'next_obj', obj)


class Stack:
    def __init__(self):
        self.top = None

    def __getitem__(self, item):
        return self.check(item)

    def __setitem__(self, key, value):
        ...

    def push(self, obj):
        """push(self, obj) - добавление объекта класса StackObj в конец стека"""
        if self.top is None:
            self.top = obj
        else:
            temp = self.top
            while temp != None:
                if temp.next:
                    temp = temp.next
                else:
                    temp.next = obj
                    break

    def check(self, indx=None):
        counter = 0
        if not self.top is None:
            temp = self.top
            prev = None
            while True:
                if counter == indx:
                    return temp
                if temp == self.top and temp.next is None:
                    self.top = None
                    break
                elif temp.next is None:
                    setattr(prev, 'next_obj', None)
                    break
                else:
                    prev = temp
                    temp = temp.next
                    counter += 1
            return temp




    def pop(self):
        """извлечение последнего объекта с его удалением из стека"""
        return self.check()


#Тесты:
st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
print(st.pop())

# temp = st.top
# while not temp is None:
#     print(temp)
#     temp = temp.next

st[1] = StackObj("obj2-new")
assert st[0].data == "obj11" and st[
    1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

# obj = st.pop()
# assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"
#
# n = 0
# h = st.top
# while h:
#     assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
#     n += 1
#     h = h.next
#
# assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"