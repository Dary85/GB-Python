def fibo_gen(val=16):
    a = 1
    for i in range(1, val + 1):
        a *= i
        yield a
        if i > 14:
            break


for i in fibo_gen(20):
    print(i)
