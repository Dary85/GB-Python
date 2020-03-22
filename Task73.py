class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


l = list()
while True:
    a = input("Input value or q to exit ")
    try:
        if a == "q":
            print(l)
            break
        if a.isdigit():
            l.append(a)
        else:
            raise OwnError("Input digits!")
    except OwnError as err:
        print(err.txt)
