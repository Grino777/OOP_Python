def input_int_numbers():
    try:
        print(*map(int, input().split()))
    except:
        raise TypeError('все числа должны быть целыми')


while True:
    try:
        input_int_numbers()
        break
    except TypeError:
        continue
