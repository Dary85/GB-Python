def f(num1, num2):
    try:
        result = int(num1) / int(num2)
        return result
    except ValueError:
        print("Error detected! Try again!")
    return 0


while True:
    num3 = input("Input number 1: ")
    num4 = input("Input number 2: ")
    result = f(num3, num4)

    if result != 0:
        print(f"Result: {result:3.2f}")
    break
