with open("text_task42.txt") as efile:
    i = 0
    for line in efile:
        i += 1
        print(f"There are  {len(line.split())} words in line")
    print(f"Total lines in file {i}")
