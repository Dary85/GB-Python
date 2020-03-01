rating = [7, 5, 3, 3, 2]

print(f"Current structure: {rating}")
while True:
    ivalue = input("Do you want to add new value to structure y/n: ")
    if ivalue != "y":
        breaky
    i = int(input("Enter new value (positive integer) to structure: "))
    rating.insert(0, i)
    rating.sort()
    rating.reverse()
    print(f"Current structure: {rating}")
