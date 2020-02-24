n = int(input("Input value: "))
a = 0
while n > 0:
    i = n % 10
    n = n // 10
    if a < i:
        a = i
print("a %d" % a)
