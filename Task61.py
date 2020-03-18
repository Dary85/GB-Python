class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        nstr = ""
        for a in self.matrix:
            nstr += ' '.join(str(a[i]) for i in range(len(a)))
            nstr += '\n'
        return nstr

    def __add__(self, other):
        l = []
        for i in range(len(self.matrix)):
            c = []
            for a in range(len(self.matrix[i])):
                c.append(self.matrix[i][a] + other.matrix[i][a])
            l.append(c)
        return Matrix(l)


o1 = Matrix([[1, 2, 3, 4, 5], [1, 2, 3, 4, 1], [0, 0, 0, 0, 0], [1, 2, 3, 4, 5], [0, 0, 0, 0, 0]])
o2 = Matrix([[1, 2, 3, 4, 5], [1, 2, 3, 4, 1], [0, 0, 3, 0, 1], [1, 2, 1, 1, 1], [0, 0, 3, 4, 5]])
print(o1)
print(o1 + o2)
