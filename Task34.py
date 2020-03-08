import random
mylist = [random.randint(1,10) for i in range(20)]
newlist = []
for i in mylist:
    if mylist.count(i)==1:
        newlist.append(i)
print(mylist)
print(newlist)