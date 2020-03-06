from itertools import count
from sys import argv
from itertools import islice
from itertools import cycle

param1, param2 = argv
print([i for i in islice(count(int(param2)),20)])

mylist = [5,6,7,8]
print([i for i in islice(cycle(mylist),20)])


