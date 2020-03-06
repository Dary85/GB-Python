from sys import argv

print(argv)
scriptname, qtyhour, rate, bonus = argv
print((int(qtyhour) * int(rate) + int(bonus)))
