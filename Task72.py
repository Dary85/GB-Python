class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = input("Введите делимое: ")
b = input("Введите делитель: ")
try:
    if float(b) != 0:
        print(float(a) / float(b))
    else:
        raise OwnError("На ноль делить нельзя")
except ValueError:
    print("Введите числа")
except OwnError as err:
    print(err)
