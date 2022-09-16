class SingletonFive:
    __count = 0
    __address = None

    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__address = super().__new__(cls)
            cls.__count += 1
            return cls.__address
        return cls.__address

    def __init__(self, name):
        self.name = name

objs = [SingletonFive(str(n)) for n in range(10)]

for n, i in enumerate(objs):
    if id(i) == id(objs[5]):
        print(f'{n} - {id(i)} - True')
    else:
        print(f'{n} - {id(i)}')