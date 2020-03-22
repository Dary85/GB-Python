class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.complex = (real_part, 1 if imaginary_part == 0 else imaginary_part)

    def __add__(self, other):
        return ComplexNumber(self.complex[0] + other.complex[0], self.complex[1] + other.complex[1])

    def __mul__(self, other):
        return ComplexNumber(self.complex[0] * other.complex[0] - self.complex[1] * other.complex[1],
                             self.complex[0] * other.complex[1] + self.complex[1] * other.complex[0])

    def __str__(self):
        return str(self.complex[0]) + ("+" if self.complex[1] > 0 else "-") + str(
            "" if self.complex[1] == 0 or abs(self.complex[1]) == 1 else self.complex[1]) + 'i'


c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(-1, 1)
print(c1)
print(c2)
print(c1 + c2)
print(c1 * c2)
