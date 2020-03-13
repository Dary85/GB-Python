from random import randint

nl = [str(randint(1, 100)) for i in range(50)]
with open("text_task45.txt", 'w') as nfile:
    nfile.write(' '.join(nl))
with open("text_task45.txt") as efile:
    el = list(map(int, efile.read().split()))
print(f"Summery :{sum(el)}")
