class Matrix:
    def __init__(self, value):
        self.value = value

    def __getitem__(self, item):
        return self.value[item]

    def __add__(self, other):
        for i in range(len(self.value)):
            for j in range(len(self.value[0])):
                C[i][j] = (self.value[i][j] + other[i][j])
        return C

    def __sub__(self, other):
        for i in range(len(self.value)):
            for j in range(len(self.value[0])):
                C[i][j] = (self.value[i][j] - other[i][j])
        return C

    def __mul__(self, other):
        return other * self.value

    def __truediv__(self, other):
        return self.value // other



A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x, y = map(int, input("Введите размерность матрицы: ").split())
C = [[0] * y for i in range(x)]
print(list(C))

C = A + B
print('\n'.join(map(str, C)))

