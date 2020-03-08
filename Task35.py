from functools import reduce

print([i if i % 2 == 0 else 1 for i in range(100, 1001)])
print(reduce(lambda result, val: result * val, [i if i % 2 == 0 else 1 for i in range(100, 1001)]))
