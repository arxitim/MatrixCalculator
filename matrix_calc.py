class Matrix:
    def __init__(self, value):
        self.value = value

    def __getitem__(self, item):
        return self.value[item]

    def __add__(self, other):
        dimension = len(self.value[0])
        result = [[(self.value[i][j] + other[i][j]) for j in range(dimension) ] for i in range(dimension)]
        return result

    def __sub__(self, other):
        dimension = len(self.value[0])
        result = [[(self.value[i][j] - other[i][j]) for j in range(dimension)] for i in range(dimension)]
        return result

    def __mul__(self, other):
        dimension = len(self.value[0])
        if (type(other) == int) or (type(other) == float):
            return [[(self.value[i][j] * other) for j in range(dimension) ] for i in range(dimension)]
        else:
            return [[sum(self.value[i][k]*other[k][j] for k in range(dimension))
                         for j in range(dimension)]
                         for i in range(dimension)]

    def determinant(self):
        def getMatrixMinor(m, i, j):
            return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

        def getMatrixDeternminant(m):
            if len(m) == 2:
                return m[0][0] * m[1][1] - m[0][1] * m[1][0]

            determinant = 0
            for c in range(len(m)):
                determinant += ((-1) ** c) * m[0][c] * getMatrixDeternminant(getMatrixMinor(m, 0, c))
            return determinant

        return getMatrixDeternminant(self.value)

    def transposing(self):
        return Matrix([[self.value[i][j] for i in range(len(self.value)) ] for j in range(len(self.value[0]))])


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
                break
    except ValueError:
        print("\n Ты не справился, попробуй еще раз! \n")
        return -1
    return Matrix(X)

while True:
    print("""\nХэй, чем займемся сегодня, Ферб?
1) Найдем детерминант матрицы
2) Найдем матрицу, обратную данной
3) Транспонируем матрицу
4) Сложим две матрицы
5) Вычтем из одной матрицы другую
6) Умножим матрицу на матрицу
7) Умножим матрицу на число
8) Поделим одну матрицу на другую
9) Ничем""")
    answer = int(input("Ответ: "))

    if answer == 1:
        matrix = input_single_matrix()
        if matrix == -1:
            continue
        print(matrix.determinant())
        continue

    if answer == 2:
        matrix = input_single_matrix()
        if matrix == -1:
            continue
        if matrix.determinant() == 0:
            print('ОБРАТНОЙ МАТРИЦЫ НЕ СУЩЕСТВУЕТ')
            continue
        result = matrix.transposing() * (1 / matrix.determinant())
        print('\n'.join(map(str, result)))


    if answer == 3:
        matrix = input_single_matrix()
        if matrix == -1:
            continue
        print('\n'.join(map(str, matrix.transposing())))

    if answer == 4:
        matrix1 = input_single_matrix()
        matrix2 = input_single_matrix()
        result = matrix1 + matrix2
        print('\n'.join(map(str, result)))

    if answer == 5:
        matrix1 = input_single_matrix()
        matrix2 = input_single_matrix()
        if (matrix1 or matrix2) == -1:
            continue
        result = matrix1 - matrix2
        print('\n'.join(map(str, result)))

    if answer == 6:
        matrix1 = input_single_matrix()
        matrix2 = input_single_matrix()
        if (matrix1 or matrix2) == -1:
            continue
        result = matrix1 * matrix2
        print('\n'.join(map(str, result)))


    if answer == 7:
        matrix = input_single_matrix()
        if matrix == -1:
            continue
        multiplier = int(input("Введите число, на которое хотите умножить вашу матрицу: "))
        result = matrix * multiplier
        print('\n'.join(map(str, result)))

    if answer == 8:
        matrix1 = input_single_matrix()
        matrix2 = input_single_matrix()
        if (matrix1 or matrix2) == -1:
            continue
        if matrix2.determinant() == 0:
            print('ОБРАТНОЙ МАТРИЦЫ ДЛЯ ВТОРОЙ МАТРИЦЫ НЕ СУЩЕСТВУЕТ, ДЕЛЕНИЕ НЕВОЗМОЖНО')
            continue
        else:
            matrix2_reverse = matrix2.transposing() * (1 / matrix2.determinant())
            result = matrix1 * matrix2_reverse
        print('\n'.join(map(str, result)))

