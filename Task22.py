def user_data(name, surname, birthyear, residence, email, phone):
    print(f"Name: {name} Surname: {surname} Birthyear: {birthyear} Residence {residence} E-mail:{email} Phone: {phone}")


while True:
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    birthyear = input("Enter your year of birth:")
    residence = input("Enter your city of residence: ")
    email = input("Enter your e-mail: ")
    phone = input("Enter your phone: ")
    user_data(name, surname, birthyear, residence, email, phone)
    a = input("To continue press 'enter' to stop press Q: ").upper()
    if a == 'Q':
        break
