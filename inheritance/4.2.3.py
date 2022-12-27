class ListInteger(list):
    def __init__(self, lst):
        for i in lst:
            self.check_values(i)
        super().__init__(lst)

    def __setitem__(self, key, value):
        self.check_values(value)
        super().__setitem__(key, value)

    def append(self, digit) -> None:
        self.check_values(digit)
        super().append(digit)

    @staticmethod
    def check_values(x):
        if not type(x) is int:
            raise TypeError('можно передавать только целочисленные значения')


