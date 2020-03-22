class Store:
    __rack = list()
    __department = list()

    def __init__(self, cells):
        try:
            self.cells = int(cells)
        except ValueError:
            print("Параметр может быть только числом")
            self.cells = 0

    def move_to_storage(self, ob, qty):
        print("Склад полон, ничео добавить нельзя") if len(self.__rack) >= self.cells else self.__rack.append(
            (ob.getstructure()["stock_number"], ob.getstructure(), qty))

    def move_to_department(self, stock_number, qty, departmentname):
        v = -1
        for i in self.__rack:

            if i[0] == stock_number:
                v = self.__rack.index(i)
                break

        if v > -1 and self.__rack[v][2] >= qty:
            self.__department.append({"department": departmentname, "object": self.__rack[v][1], "qty": qty})
            self.__rack.pop(v)
        else:
            print(f"Нет такого оборудования на складе {stock_number} или не достаточно на остатках")

    def __str__(self):
        return "There are in storage:\n" + '\n'.join(
            str(self.__rack[i]) for i in range(len(self.__rack))) + "\nThere are in department:\n" + '\n'.join(
            str(self.__department[a]) for a in range(len(self.__department)))


class Equipment:
    def __init__(self, brand, price, stock_number):
        self.brand = brand
        self.price = price
        self.stock_number = stock_number

    @property
    def info(self):
        print(f"Common information:\n /"
              f"-brand {self.brand}\n-price {self.price}\n-stock_number {self.stock_number}")


class Printer(Equipment):
    def __init__(self, brand, price, stock_number, page_number, colore):
        super().__init__(brand, price, stock_number)
        self.page_number = page_number
        self.color = colore

    def getstructure(self):
        return {"type": "printer", "stock_number": self.stock_number, "brand": self.brand, "price": self.price}

    @property
    def info(self):
        print(f"Common information:\n /"
              f"-brand {super().brand}\n-price {super().price}\n-stock_number {super().stock_number}\n /"
              f"Detail: \n-page number {self.page_number}\n-color {self.color}")


class Fax(Equipment):
    def __init__(self, brand, price, stock_number, size, weight):
        super().__init__(brand, price, stock_number)
        self.size = size
        self.weight = weight

    def getstructure(self):
        return {"type": "fax", "stock_number": self.stock_number, "brand": self.brand, "size": self.size}

    @property
    def info(self):
        print(f"Common information:\n /"
              f"-brand {super().brand}\n-price {super().price}\n-stock_number {super().stock_number}\n/"
              f"Detail: \n-size {self.size}\n-weight {self.weight}")


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


storage = Store(10)

Printer1 = Printer("HP", 200, 1, 200, "grey")
Printer2 = Printer("Canon", 250, 2, 300, "grey")
Printer3 = Printer("Brother", 300, 3, 500, "grey")
Fax1 = Fax("Panasonic", 300, 4, "303x30x40", 20)
Fax2 = Fax("Philips", 300, 5, "500x30x40", 20)

storage.move_to_storage(Printer1, 2)
storage.move_to_storage(Printer2, 1)
storage.move_to_storage(Printer3, 1)
storage.move_to_storage(Fax1, 3)
storage.move_to_storage(Fax2, 1)
while True:
    print(storage)
    qty = input("Input department, number of equipment and equipment stock number with space or press Enter to quit: ")
    if not qty:
        break

    datalist = qty.split()
    try:
        if datalist[1].isdigit():
            number = int(datalist[1])
        else:
            raise OwnError("Number of equipment should be the digit!")
        if datalist[2].isdigit():
            stock = int(datalist[2])
        else:
            raise OwnError("Stock number of equipment should be the digit!")
    except ValueError:
        print("Not correct value, try again")
    except OwnError as err:
        print(err)
    storage.move_to_department(stock, number, datalist[0])
