a = float(input("Enter first value(km): "))
b = float(input("Enter second value(km): "))
i = 1
while a <= b:
    a = a * 1.1
    print(f"day{i}: {a:.1f}")
    i = i + 1
print(f"on the {i}th day, the athlete achieved a result of  < {b} km")
