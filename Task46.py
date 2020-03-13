sdict = {}
with open("text_task46.txt", 'r', 1, 'utf8') as efile:
    for line in efile:
        a = line.split()
        i = 1
        sum = 0
        while i <= 3:  # читаем слова после наименования предмета
            try:
                sum += int(a[i][:a[i].index("(")])
            except ValueError:
                sum += 0
            i += 1
        sdict.setdefault(a[0][:a[0].index(':')], sum)
print(sdict)
