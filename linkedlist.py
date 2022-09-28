class LinkedList:

    def __init__(self, data):
        self.head = None #ссылка на первый объект связного списка (если список пустой, то head = None);
        self.tail = None #ссылка на последний объект связного списка (если список пустой, то tail = None).


    def add_obj(self, obj):
        """добавление нового объекта obj класса ObjList в конец связного списка;"""
        pass

    def remove_obj(self):
        """удаление последнего объекта из связного списка;"""
        pass

    def get_data(self):
        """получение списка из строк локального свойства __data всех объектов связного списка."""
        pass

class ObjList:
    """ Создавать объекты класса ObjList предполагается командой:
    ob = ObjList("данные 1") """
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        """Изменение приватного свойства __next на значение obj;"""
        pass
    def set_prev(self, obj):
        """Изменение приватного свойства __prev на значение obj;"""
        pass
    def get_next(self):
        """Получение значения приватного свойства __next;"""
        pass
    def get_prev(self):
        """Получение значения приватного свойства __prev;"""
        pass
    def set_data(self, data):
        """Изменение приватного свойства __data на значение data;"""
        pass
    def get_data(self):
        """Получение значения приватного свойства __data."""
        pass

# lst = LinkedList()
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']