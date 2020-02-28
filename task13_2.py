while True:

    month = int(input("Input № of month: "))
    dict_of_month = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer",
                     8: "summer", 9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}
    if 1 <= month <= 12:
        print(dict_of_month.get(month))
        break
    else:
        print("Error! Input number from 1 to 12")
