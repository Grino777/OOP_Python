class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

a, b = input().split()

try:
    res = list(map(int, (a, b)))
    res = Point(*res)
except ValueError:
    try:
        res = list(map(float, (a, b)))
        res = Point(*res)
    except ValueError:
        res = Point()
finally:
    print(f"Point: x = {res._x}, y = {res._y}")