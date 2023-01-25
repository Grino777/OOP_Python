def get_loss(w1, w2, w3, w4):
    try:
        res = w1 // w2
    except ZeroDivisionError:
        return "деление на ноль"
    else:
        res = 10 * res - 5 * w2 * w3 + w4
        return res

print(get_loss(2, 0, 3, 4))