user_str = input("Enter string: ")
str_list = user_str.split()
for i in range(len(str_list)):
    print(f"N {i+1}: {str_list[i].capitalize() if len(str_list[i]) <= 10 else str_list[i][:10].capitalize()}")
