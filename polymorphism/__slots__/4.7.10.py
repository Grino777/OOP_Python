class Note:
    ton_value = (-1, 0, 1)
    note_name = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name':
            if value in self.note_name:
                self.__dict__[key] = value
            else:
                self.get_raise()
        if key == '_ton':
            if value in self.ton_value:
                self.__dict__[key] = value
            else:
                self.get_raise()

    @staticmethod
    def get_raise():
        raise ValueError('недопустимое значение аргумента')


class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    __address = None

    def __new__(cls, *args, **kwargs):
        if cls.__address is None:
            cls.__address = super().__new__(cls)
            return cls.__address
        else:
            return cls.__address

    def __init__(self):
        self._do = Note('до', 0)
        self._re = Note("ре", 0)
        self._mi = Note("ми", 0)
        self._fa = Note("фа", 0)
        self._solt = Note("соль", 0)
        self._la = Note("ля", 0)
        self._si = Note("си", 0)

    def __getitem__(self, item):
        if 0 <= item <= 6:
            return getattr(self, self.__slots__[item])
        else:
            raise IndexError('недопустимый индекс')


n = Notes()
n[0]._ton = 1
print(n[0].__dict__)
