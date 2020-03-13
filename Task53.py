class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.position = position
        self.name = name
        self.surname = surname
        self._income = {"wage": wage, "bonus": bonus}

    def get_parameters(self):
        print(f"Name {self.name}")


class Position(Worker):

    def get_full_name(self):
        try:
            return self.name.title() + " " + self.surname.title()
        except ValueError:
            print("Error detected!")
            return False

    def get_total_inome(self):
        try:
            return self._income["wage"] + self._income["bonus"]
        except ValueError:
            print("Error detected!")
            return 0


while True:
    val = input(
        "Enter employee data 'name', 'surname','position','wage', 'bonus' with space or press Enter to quit: ").split()
    if not val:
        break
    name, surname, pos, wage, bonus = map(str,val)
    try:
        p = Position(name, surname, pos, float(wage), float(bonus))
        print(f"Full name {p.get_full_name()}")
        print(f"Total income name {p.get_total_inome()}")
        print(f"Position {p.position}")
        print(f"Income content {p._income}")
    except ValueError:
        print("Data is not correct. Try again.")

