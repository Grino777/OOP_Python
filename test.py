class Stack:
    top = None
    last = None

    def __repr__(self):
        return f'{self.top}'

    def push(self, obj):
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
        temp = self.top
        while True:
            if temp is None:
                return None
            elif temp.next == self.last:
                self.last = temp
                res = temp.next
                temp.next = None
                return res
            else:
                temp = temp.next

    def get_data(self):
        objs_data = []
        temp = self.top
        while temp:
            objs_data.append(temp.data)
            temp = temp.next
        return objs_data


class StackObj:
    def __init__(self, data: str):
        self.__data = data
        self.__next = None

    def __repr__(self):
        return f'{self.__data}'

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

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
print(res)
