from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return f'Базовый класс Model'


class ModelForm(Model):
    ID = 0

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.ID
        self.set_id()

    def get_pk(self):
        return self._id

    @classmethod
    def set_id(cls):
        cls.ID += 1

m = ModelForm('login', 'pass')
m1 = ModelForm('login', 'pass')
print(m.__dict__)
print(m1.__dict__)
