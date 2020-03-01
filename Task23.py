def func(arg1, arg2, arg3):
    t = [arg1, arg2, arg3]
    try:
        t.remove(min(t))
        return sum(t)
    except ValueError:
        print("Error! Not correct value, try again")
        return 0

arg4 = input("Enter arg1: ")
arg5 = input("Enter arg2: ")
arg6 = input("Enter arg3: ")
if arg4.isdigit():
    arg4 = int(arg4)
if arg5.isdigit():
    arg5 = int(arg5)
if arg6.isdigit():
    arg6 = int(arg6)
result = func(arg4, arg5, arg6)
if result != 0:
    print(f"Result {result}")
