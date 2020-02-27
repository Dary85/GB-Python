revenue = float(input("Enter revenue: "))
cost = float(input("Enter cost: "))
fresult = revenue - cost
if fresult > 0:
    print("Your income is: %.2f" % fresult)
    if revenue > 0:
        print("Your margin is: %.2f" % (fresult / revenue))
    else:
        print("Error to calc margin")

    employee = int(input("Enter Employee qty: "))

    if employee > 0:
        print("Rate 'income per employee' %.2f" % (fresult / employee))
    else:
        print("Error to calc rate 'income per employee'")

else:
    print("Your loss is: %.2f" % fresult)
