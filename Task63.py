class Cell:
    def __init__(self, qty=0):
        try:
            if qty < 0:
                print("Wrong parameter")
                self.qty = 0
            else:
                self.qty = qty
        except ValueError:
            print("Wrong parameter")
            self.qty = 0

    def __str__(self):
        return str(self.qty)

    def __add__(self, other):
        return Cell(self.qty + other.qty)

    def __sub__(self, other):
        if self.qty >= other.qty:
            return Cell(self.qty - other.qty)
        else:
            print("Not possible to calc")
            return 0

    def __truediv__(self, other):
        return Cell(round(self.qty / other.qty))

    def __mul__(self, other):
        return Cell(self.qty * other.qty)

    def make_oder(self, ob, count):
        qty = int(ob.qty)
        for i in range(ob.qty // count) if ob.qty % count == 0 else range(ob.qty // count + 1):
            print(''.join("*" for i in range(min(qty, count))))
            qty -= min(qty, count)


ob1 = Cell(25)
ob2 = Cell(11)
print(ob1 + ob2)
print(ob1 - ob2)
print(ob1 * ob2)
print(ob1 / ob2)

ob1.make_oder(ob1, 10)
