class Layer:
    def __init__(self):
        self.next_layer = None
        self.name = 'Layer'

    def __call__(self, *args, **kwargs):
        for i in NetworkIterator(self):
            if i.next_layer is None:
                i.next_layer = args[0]
        return self


class Input(Layer):
    """Формирование входного слоя сети"""
    def __init__(self, inputs):
        super().__init__()
        self.inputs = inputs
        self.name = 'Input'


class Dense(Layer):
    """Формирование полносвязного слоя сети"""
    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation
        self.name = 'Dense'


class NetworkIterator:
    """Отдельный класс NetworkIterator для итерирования (перебора) слоев сети циклом for"""

    def __init__(self, obj):
        self.iter_obj = obj

    def __call__(self, *args, **kwargs):
        self.iter_obj = args[0]
        return self

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_obj:
            res = self.iter_obj
            self.iter_obj = res.next_layer
        else:
            raise StopIteration
        return res


#Тесты:
nt = Input(12)
layer = nt(Dense(nt.inputs, 1024, 'relu'))
layer = layer(Dense(layer.inputs, 2048, 'relu'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

n = 0
for x in NetworkIterator(nt):
    assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
    n += 1

assert n == 4, "итератор перебрал неверное число слоев"
