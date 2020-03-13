ls = []
with open("text_task43.txt", 'r', 1, 'utf8') as efile:
    for line in efile:
        a = line.split()
        if len(a) >= 3:  # проверим на соответствие формата
            try:
                if int(a[2]) < 20:
                    print(f"Surname: {a[0]} salary {a[2]}")
                ls.append(int(a[2]))
            except ValueError:
                print("Smth wrong")
print(f"AVG salary: {sum(ls) / len(ls):.2f}")
