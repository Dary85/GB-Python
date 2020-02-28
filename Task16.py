a = list()
i = 0
result_dict = {"name": list(), "price": list(), "quantity": list(), "unit": list()}
while True:
    answer = input("Do you want to add new position y/n: ")
    if answer != "y":
        break
    name = input("Enter position name: ")
    price = float(input("Enter position price: "))
    qty = float(input("Enter position quantity: "))
    unit = input("Enter position unit: ")
    i = i + 1
    a.append((i, dict(name=name, price=price, quantity=qty, unit=unit)))

for item in a:
    result_dict["name"].append(item[1].get("name"))
    result_dict["price"].append(item[1].get("price"))
    result_dict["quantity"].append(item[1].get("quantity"))
    result_dict["unit"].append(item[1].get("unit"))
print(result_dict)
