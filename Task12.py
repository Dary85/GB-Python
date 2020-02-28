my_list = list(input("Enter list: "))
print(my_list)
list_len = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1
first_list = my_list[:list_len:2]
second_list = my_list[1:list_len:2]
third_list = []
i = 0
a = 0
for i in range(len(first_list)):
    third_list.insert(i + a, second_list[i])
    third_list.insert(i + a + 1, first_list[i])
    a = i + 1
third_list.insert(len(my_list), my_list[len(my_list) - 1])
print(third_list)
