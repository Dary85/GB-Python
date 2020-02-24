seconds = int(input("Enter qty of seconds: "))
h = seconds // 3600
m = (seconds - h * 3600) // 60
s = (seconds - h * 3600 - m * 60)
if h < 10:
    hprint = str(0) + str(h)
else:
    hprint = str(h)
if m < 10:
    mprint = str(0) + str(m)
else:
    mprint = str(m)
if s < 10:
    sprint = str(0) + str(s)
else:
    sprint = str(s)

print(f"{hprint}:{mprint}:{sprint}")
