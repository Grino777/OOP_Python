class Validator:
    def __call__(self, *args, **kwargs):
        return self._is_valid(*args)

    def _is_valid(self, data) -> bool:
        return True


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data) -> bool:
        if isinstance(data, int):
            if self.min_value <= data <= self.max_value:
                return super()._is_valid(data)
        raise ValueError('данные не прошли валидацию')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data) -> bool:
        if isinstance(data, float):
            if self.min_value <= data <= self.max_value:
                return super()._is_valid(data)
        raise ValueError('данные не прошли валидацию')

i_v = IntegerValidator(-10, 10)
f_v = FloatValidator(-1, 1)
print(f_v(0))

