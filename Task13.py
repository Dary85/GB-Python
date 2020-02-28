month = int(input("Input № of month: "))
list_of_month = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

if month in list_of_month[:3:1]:
    print("winter")
elif month in list_of_month[3:6:1]:
    print("spring")
elif month in list_of_month[6:9:1]:
    print("summer")
elif month in list_of_month[9:12:1]:
    print("autumn")
else:
    print("Error! Please input number from 1 to 12")
