#Мое решение:
import time
#
#
# class ObjList:
#     def __init__(self, data=''):
#         self.__data = data
#         self.__next = None
#         self.__prev = None
#
#     @property
#     def next(self):
#         return getattr(self, '_ObjList__next')
#
#     @next.setter
#     def next(self, next):
#         setattr(self, '_ObjList__next', next)
#
#     @property
#     def prev(self):
#         return getattr(self, '_ObjList__prev')
#
#     @prev.setter
#     def prev(self, prev):
#         setattr(self, '_ObjList__prev', prev)
#
#     def __repr__(self):
#         return f'{self.__data}'
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def add_obj(self, obj):
#         """"""
#         if self.head is None:
#             self.head = obj
#             self.tail = obj
#         else:
#             temp = self.head
#             while True:
#                 if temp.next is None:
#                     setattr(temp, '_ObjList__next', obj)
#                     obj.prev = temp
#                     setattr(self, 'tail', obj)
#                     break
#                 else:
#                     temp = temp.next
#
#     def get_head(self):
#         return getattr(self, 'head')
#
#     def remove_obj(self, indx):
#         if not 0 <= indx <= len(self):
#             raise ValueError('Количество элементов связного списка меньше чем полученный индекс')
#         else:
#             counter = 0
#             temp = self.get_head()
#             length = len(self)
#             while True:
#                 if indx == counter:
#                     if indx == 0:
#                         self.head = temp.next
#                         self.tail = self.head
#                         break
#                     elif indx == length-1:
#                         setattr(temp.prev, '_ObjList__next', None)
#                         setattr(self, 'tail', temp.prev)
#                         break
#                     else:
#                         setattr(temp.prev, '_ObjList__next', temp.next)
#                         setattr(temp.next, '_ObjList__prev', temp.prev)
#                         break
#                 else:
#                     temp = temp.next
#                     counter += 1
#
#     def __len__(self):
#         if self.get_head is None:
#             return 0
#         else:
#             temp: ObjList = self.get_head()
#             length = 0
#             while temp is not None:
#                 temp = temp.next
#                 length += 1
#             return length
#
#     def __call__(self, *args, **kwargs):
#         indx = args[0]
#         if indx > len(self):
#             raise ValueError('Количество элементов связного списка меньше чем полученный индкс')
#         else:
#             counter = 0
#             temp = self.get_head()
#             while True:
#                 if indx == counter:
#                     return getattr(temp, '_ObjList__data')
#                 else:
#                     temp = temp.next
#                     counter += 1
#
#     def get_all_objects(self):
#         obj_list = []
#         temp = self.get_head()
#         while True:
#             if temp.next is None:
#                 obj_list.append(temp)
#                 break
#             else:
#                 obj_list.append(temp)
#                 temp = temp.next
#         return obj_list

# Лучшее решение:
class Desc:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if not self.head:
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx):
        c = 0
        tmp = self.head
        while c != indx:
            c += 1
            tmp = tmp.next

        if tmp.next and tmp.prev:
            tmp.next.prev = tmp.prev
            tmp.prev = tmp.next

        elif tmp == self.head == self.tail:
            self.head = self.tail = None

        elif tmp == self.head:
            tmp.next.prev = None
            self.head = tmp.next

        elif tmp == self.tail:
            tmp.prev.next = None
            self.tail = tmp.prev

    def __len__(self):
        c = 1 if self.head else 0
        tmp = self.head
        while tmp.next:
            c += 1
            tmp = tmp.next
        return c

    def __call__(self, indx):
        c = 0
        tmp = self.head
        while c != indx:
            c += 1
            tmp = tmp.next
        return tmp.data


class ObjList:
    data = Desc()
    prev = Desc()
    next = Desc()

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

#Тесты:
st = time.time()
ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"
et = time.time()
print(et-st)

