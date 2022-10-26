class ObjList:
    def __init__(self, data=''):
        self.__data = data
        self.__next = None
        self.__prev = None

    @property
    def next(self):
        return getattr(self, '_ObjList__next')

    @next.setter
    def next(self, next):
        setattr(self, '_ObjList__next', next)

    @property
    def prev(self):
        return getattr(self, '_ObjList__prev')

    @prev.setter
    def prev(self, prev):
        setattr(self, '_ObjList__prev', prev)

    def __repr__(self):
        return f'{self.__data}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        """"""
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            temp = self.head
            while True:
                if temp.next is None:
                    setattr(temp, '_ObjList__next', obj)
                    obj.prev = temp
                    setattr(self, 'tail', obj)
                    break
                else:
                    temp = temp.next

    def get_head(self):
        return getattr(self, 'head')

    def remove_obj(self, indx):
        if not 0 <= indx <= len(self):
            raise ValueError('Количество элементов связного списка меньше чем полученный индекс')
        else:
            counter = 0
            temp = self.get_head()
            length = len(self)
            while True:
                if indx == counter:
                    if indx == 0:
                        self.head = temp.next
                        self.tail = self.head
                        break
                    elif indx == length-1:
                        setattr(temp.prev, '_ObjList__next', None)
                        setattr(self, 'tail', temp.prev)
                    else:
                        setattr(temp.prev, '_ObjList__next', temp.next)
                        setattr(temp.next, '_ObjList__prev', temp.prev)
                        break
                else:
                    temp = temp.next
                    counter += 1

    def __len__(self):
        if self.get_head is None:
            return 0
        else:
            temp: ObjList = self.get_head()
            length = 0
            while not temp is None:
                temp = temp.next
                length += 1
            return length

    def __call__(self, *args, **kwargs):
        indx = args[0]
        if indx > len(self):
            raise ValueError('Количество элементов связного списка меньше чем полученный индкс')
        else:
            counter = 0
            temp = self.get_head()
            while True:
                if indx == counter:
                    return getattr(temp, '_ObjList__data')
                else:
                    temp = temp.next
                    counter += 1

    # def get_all_objects(self):
    #     obj_list = []
    #     temp = self.get_head()
    #     while True:
    #         if temp.next is None:
    #             obj_list.append(temp)
    #             break
    #         else:
    #             obj_list.append(temp)
    #             temp = temp.next
    #     return obj_list


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
print(linked_lst.get_all_objects())
linked_lst.remove_obj(1)
print(linked_lst.get_all_objects())
