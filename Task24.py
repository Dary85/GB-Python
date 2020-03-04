def func1(base, rate):
    return 1 / (base ** abs(rate))


def func2(base, rate):
    i = 2
    val = base
    while i <= abs(rate):
        val *= base
        i += 1
    return 1 / val


while True:
    base = input("Enter real number: ")
    rate = input("Enter rate: ")
    try:

        if int(rate)>0:
            print(f"POW {pow(float(base),int(rate))}")
        else:
            print(f"** {func1(float(base), int(rate))}")
            print(f"-- {func2(float(base), int(rate))}")
        break
    except ValueError:
        print("Error: input only numbers!")
