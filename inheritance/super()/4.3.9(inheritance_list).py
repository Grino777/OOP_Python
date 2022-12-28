class SoftList(list):
    def __init__(self, *args):
        super().__init__(*args)

    def __getitem__(self, item):
        if not 0 <= abs(item) < len(self):
            return False
        else:
            return super().__getitem__(item)


sl = SoftList("python")
print(sl)
print(sl[0]) # 'p'
print(sl[-1])  # 'n'
print(sl[6])  # False
print(sl[-7])  # False
