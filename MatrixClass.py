class Matrix:
    def __init__(self, value):
        self.value = value

    def __getitem__(self, item):
        return self.value[item]

    def __add__(self, other):
        dimension = len(self.value[0])
        result = [[(self.value[i][j] + other[i][j]) for j in range(dimension)] for i in range(dimension)]
        return result

    def __sub__(self, other):
        dimension = len(self.value[0])
        result = [[(self.value[i][j] - other[i][j]) for j in range(dimension)] for i in range(dimension)]
        return result

    def __mul__(self, other):
        dimension = len(self.value[0])
        if (type(other) == int) or (type(other) == float):
            return [[(self.value[i][j] * other) for j in range(dimension)] for i in range(dimension)]
        else:
            a = self.value
            b = other
            rows_a = len(a)
            cols_a = len(a[0])
            # rows_b = len(b)
            cols_b = len(b[0])
            c = [[0 for row in range(len(b[0]))] for col in range(len(a))]

            for i in range(rows_a):
                for j in range(cols_b):
                    for k in range(cols_a):
                        c[i][j] += a[i][k] * b[k][j]
            return c

    def determinant(self):
        def get_matrix_minor(m, i, j):
            return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

        def get_matrix_determinant(m):
            if len(m) == 2:
                return m[0][0] * m[1][1] - m[0][1] * m[1][0]

            Determinant = 0
            for c in range(len(m)):
                Determinant += ((-1) ** c) * m[0][c] * get_matrix_determinant(get_matrix_minor(m, 0, c))
            return Determinant

        return get_matrix_determinant(self.value)

    def transposing(self):
        return Matrix([[self.value[i][j] for i in range(len(self.value))] for j in range(len(self.value[0]))])


def input_single_matrix():
    try:
        size = int(input("Введите размерность матрицы: "))
        X = [[0] * size for i in range(size)]
        print("Построчно введите значения элементов матрицы через пробел (ввел строку, нажал Enter)")
        for i in range(size):
            tmp_input = list(map(int, input().split()))
            if len(tmp_input) == size:
                X[i] = tmp_input
            else:
                print("\nТы не справился, попробуй еще раз! \n")
                return False
    except ValueError:
        print("\n Ты не справился, попробуй еще раз! \n")
        return False
    return Matrix(X)
