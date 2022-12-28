class IteratorArrs:
    def __iter__(self):
        for item in self.__dict__.items():
            yield item


class SmartPhone(IteratorArrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory

phone = SmartPhone('Nokia', 123, 16)

for attr, value in phone:
    print(attr, value)