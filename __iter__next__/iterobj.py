class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def __getitem__(self, item):
        if self.validator(item):
            return list(self.__dict__.values())[item]

    def __setitem__(self, key, value):
        if self.validator(key):
            per = list(self.__dict__.keys())[key]
            self.fio = value

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        if self.start < len(self.__dict__) - 1:
            res = list(self.__dict__.values())[self.start]
            self.start += 1
        else:
            raise StopIteration
        return res


    def validator(self, indx):
        if 0 <= indx <= 4:
            return True
        else:
            raise IndexError('неверный индекс')


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = '123'
print(pers.__dict__)
