"""Реализовать  односвязный список с добавлением объектов в стек изъятием последнго элемента из стека"""

class Stack:
    top = None
    last = None

    def push(self, obj) -> None:
        """Добавляет объект в стек"""
        if self.top is None:
            self.top = obj
            self.last = obj

        else:
            temp = self.top
            while True:
                if not temp.next:
                    temp.next = obj
                    self.last = obj
                    break
                else:
                    temp = temp.next

    def pop(self):
        """Изъятие последнего объекта стека с последующим удалением из стека"""
        temp = self.top
        while True:
            if temp == self.last:
                self.top = None
                self.last = None
                return temp
            elif temp.next == self.last:
                self.last = temp
                res = temp.next
                temp.next = None
                return res
            else:
                temp = temp.next

    def get_data(self) -> list:
        """Получить все данные объектов стека"""
        objs_data = []
        temp = self.top
        while temp:
            objs_data.append(temp.lst_math)
            temp = temp.next
        return objs_data


class StackObj:
    def __init__(self, data: str):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if type(next) == StackObj or next is None:
            self.__next = next


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

#Тесты

# st = Stack()
# # st.push(StackObj("obj1"))
# # st.push(StackObj("obj2"))
# # st.push(StackObj("obj3"))
# # st.pop()
# res = st.get_data()    # ['obj1', 'obj2']
# print(res)

# s = Stack()
# top = StackObj("obj_1")
# s.push(top)
# s.push(StackObj("obj_2"))
# s.push(StackObj("obj_3"))
# s.pop()
#
# res = s.get_data()
# assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
# assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"
#
# h = s.top
# while h:
#     res = h.data
#     h = h.next

# s = Stack()
# top = StackObj("obj_1")
# s.push(top)
# s.pop()
# assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

# n = 0
# h = s.top
# while h:
#     h = h.next
#     n += 1
#
# assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"
#
# s = Stack()
# top = StackObj("name_1")
# s.push(top)
# obj = s.pop()
# assert obj == top, "метод pop() должен возвращать удаляемый объект"
