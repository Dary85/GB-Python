class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def all_data(cls, datavalue):
        return list(map(int, datavalue.split("-")))

    @staticmethod
    def validate(whattocheck, part):
        if whattocheck == "month":
            print("correct month") if part >= 1 and part <= 12 else print("not correct month")
        elif whattocheck == "day":
            print("correct day") if part >= 1 and part <= 31 else print("not correct day")
        elif whattocheck == "year":
            print("correct year") if part >= 1000 else print("not correct year")


datevalue = input("Input date dd-mm-yy ")
ob = Data(datevalue)
res = Data.all_data(ob.data)
print(f"day {res[0]} month {res[1]} year {res[2]}")
ob.validate("day", res[0])
ob.validate("month", res[1])
ob.validate("year", res[2])
