numbers = dict(One='Один', Two='Два', Three="Три", Four="Четыре")
nl = []
with open("text_task44.txt", 'r', 1, 'utf8') as efile:
    for line in efile:
        a = line.split()
        nl.append((numbers[a[0]] + " " + a[1] + " " + a[2]))
print(nl)
with open("new_text_task44.txt", 'w', 1, 'utf8') as nfile:
    nfile.write('\n'.join(nl))
