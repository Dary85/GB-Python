import random

my_list = [random.randint(1, 100) for i in range(20)]
print(my_list)
final_list = []
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        final_list.append(my_list[i])
print(final_list)
