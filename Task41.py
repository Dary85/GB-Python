a = []
while True:
    value = input("Input string or press 'Enter ' to quit: ")
    if not value:
        break
    a.append(value)
with open("text_task41.txt", "w") as nfile:
    nfile.write('\n'.join(a))
