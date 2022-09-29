class ObjList: #Второе решение
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def set_data(self, data):
        self.__data = data

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def add_obj(self, obj):
        if self.head:
            temp = obj
            temp.set_prev(self.tail)
            self.tail.set_next(temp)
            self.tail = temp
        else:
            self.head = obj
            self.tail = obj

    def remove_obj(self):
        if self.tail.get_prev():
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        else:
            self.tail = None
            self.head = None

    def get_data(self):
        result = []
        obj = self.head
        while obj:
            result.append(obj.get_data())
            obj = obj.get_next()
        return result

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
lst.add_obj(ObjList("данные 4"))

start = lst.head
print(start)

while start != None:
    print(start.get_next())
    start = start.get_next()

# class LinkedList: # Первое
#
#     def __init__(self):
#         self.head = None  # ссылка на первый объект связного списка (если список пустой, то head = None);
#         self.tail = None  # ссылка на последний объект связного списка (если список пустой, то tail = None).
#
#     def add_obj(self, obj):
#         """ Добавление нового объекта obj класса ObjList в конец связного списка;"""
#         if self.head is None: #Проверяем является ли связный список пустым и если да, то записываем первый элемент списка
#             self.head = obj
#             self.tail = obj
#         else:
#             this_object = self.tail #Выбираем последний объект в связном списке
#             setattr(this_object, '_ObjList__next', obj) #Устанавливаем ссылку на следующий объект
#             next_object = this_object._ObjList__next #Записываем следующий(последний) объект в переменную
#             setattr(next_object, '_ObjList__prev', this_object) #Указываем ссылку на предыдущий объект
#             self.tail = next_object #Перезаписываем последний объект связного списка
#
#     def remove_obj(self):
#         """ Удаление последнего объекта из связного списка;"""
#         if self.tail == self.head:
#             self.tail = None
#             self.head = None
#         else:
#             last_obj = self.tail
#             prev_obj = last_obj._ObjList__prev
#             setattr(prev_obj, '_ObjList__next', None)
#             self.tail = prev_obj
#
#
#     def get_data(self):
#         """ Получение списка из строк локального свойства __data всех объектов связного списка."""
#
#         start = self.head
#         data_list = list()
#         while start != None:
#             data_list.append(str(start._ObjList__data))
#             start = start._ObjList__next
#
#         return data_list
#
#
# class ObjList:
#     """ Создавать объекты класса ObjList предполагается командой:
#     ob = ObjList("данные 1") """
#
#     NUM = 0
#
#     def __new__(cls, *args, **kwargs):
#         cls.NUM += 1
#         return super().__new__(cls)
#
#     def __init__(self, data):
#         self.num = self.NUM
#         self.__next = None
#         self.__prev = None
#         self.__data = data
#
#     def __repr__(self):
#         return f'Объект класса ObjList - {self.num}'
#
#     def set_next(self, obj):
#         """ Изменение приватного свойства __next на значение obj;"""
#         self.__next = obj
#
#     def set_prev(self, obj):
#         """ Изменение приватного свойства __prev на значение obj;"""
#         self.__prev = obj
#
#     def get_next(self):
#         """  Получение значения приватного свойства __next;"""
#         return self.__next
#
#     def get_prev(self):
#         """ Получение значения приватного свойства __prev;"""
#         return self.__prev
#
#     def set_data(self, data):
#         """ Изменение приватного свойства __data на значение data;"""
#         self.__data = data
#
#     def get_data(self):
#         """ Получение значения приватного свойства __data."""
#         return self.__data
#
#
# lst = LinkedList()
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# lst.add_obj(ObjList("данные 4"))
#
#
# while True: #Проверка элементов связного списка
#     if start._ObjList__next is None:
#         print(f"{start}, следующий - None, предыдущий - {start._ObjList__prev}")
#         break
#     else:
#         print(f'{start}, cледующий - {start._ObjList__next}, предыдущий - {start._ObjList__prev}')
#     start = start._ObjList__next

