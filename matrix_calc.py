class Matrix:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return other + self.value

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return other * self.value

    def __truediv__(self, other):
        return self.value // other

    def proverk1(self):
        self.value += 1

    def proverk2(self):
        self.proverk1()
        return self.value



A = Matrix(6)
print(A + 3)
print(A * 3)
print(A / 2)
print(A - 2)
print(A.proverk2())
