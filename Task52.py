class Road:
    def __init__(self, length=0, width=0):
        self._length = 10
        self._width = 20

    def calc_mass(self):
        return self._length * self._width*25*5


width,length = map(int, input( "Enter width and length with space: ").split())
calc = Road(width, length)
print(calc.calc_mass())
