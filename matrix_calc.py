class Matrix:
    def __init__(self, value):
        self.value = value

    def __getitem__(self, item):
        return self.value[item]

    def determinant(self):
        return 1

    def __add__(self, other):
        dimension = len(self.value[0])
        result = [[(self.value[i][j] + other[i][j]) for j in range(dimension) ] for i in range(dimension)]
        return result

    def __sub__(self, other):
        dimension = len(self.value[0])
        result = [[(self.value[i][j] + other[i][j]) for j in range(dimension)] for i in range(dimension)]
        return result


    def __mul__(self, other):
        return other * self.value

    def __truediv__(self, other):
        return self.value // other


while True:
    print("""Хэй, чем займемся сегодня, Ферб?
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
            continue
        X = Matrix(X)
        Y = Matrix([[1, 1], [1, 1]])
        print(X + Y)
