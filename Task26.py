def int_func(str):
    return str.capitalize()


while True:
    lstr = input("Enter string: ").split()
    for i in lstr:
        print(int_func(i))
    a = input("Do you want to continue? y/n: ")
    if a != 'y':
        break
