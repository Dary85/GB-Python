mylist = [i if i % 20 == 0 or i % 21 == 0 else 0 for i in range(20, 240)]
while mylist.count(0) > 0:
    mylist.pop(mylist.index(0))
print(mylist)
