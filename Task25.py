def func(nlist):
    global result
    for i in nlist:
        if i.upper() == "Q":
            return (0, result)
        else:
            try:
                result += float(i)
            except ValueError:
                print(f"Type error {i}. Current result is {result}")
                return (1, result)
    return (2, result)


result = 0
while True:
    nlist = input("Enter numbers separated with space or Q to break: ").split()
    total = func(nlist)
    if total[0] == 2:
        print(f"Result {result}")
    elif total[0] == 0:
        print(f"Result {total[1]}")
        break
    else:
        break
