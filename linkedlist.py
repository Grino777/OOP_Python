class LinkedList:
    head = None  # ссылка на первый объект связного списка (если список пустой, то head = None);
    tail = None  # ссылка на последний объект связного списка (если список пустой, то tail = None).

    @classmethod
    def add_obj(cls, obj):
        """ Добавление нового объекта obj класса ObjList в конец связного списка;"""
        if cls.head is None:
            cls.head = obj
        else:
            next = cls.head
            while True:
                if next.__next is None:
                    setattr(next, '__next', obj)
                else:
                    next = next.__next

    def remove_obj(self):
        """ Удаление последнего объекта из связного списка;"""
        del self

    def get_data(self):
        """ Получение списка из строк локального свойства __data всех объектов связного списка."""
        pass


class ObjList:
    """ Создавать объекты класса ObjList предполагается командой:
    ob = ObjList("данные 1") """

    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        """ Изменение приватного свойства __next на значение obj;"""
        self.__next = obj

    def set_prev(self, obj):
        """ Изменение приватного свойства __prev на значение obj;"""
        self.__prev = obj

    def get_next(self):
        """  Получение значения приватного свойства __next;"""
        return self.__next

    def get_prev(self):
        """ Получение значения приватного свойства __prev;"""
        return self.__prev

    def set_data(self, data):
        """ Изменение приватного свойства __data на значение data;"""
        self.__data = data

    def get_data(self):
        """ Получение значения приватного свойства __data."""
        return self.__data

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
# res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']

