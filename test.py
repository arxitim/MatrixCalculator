from MatrixClass import *

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
        if matrix:
            print(matrix.determinant())
        else:
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
        if matrix1:
            matrix2 = input_single_matrix()
            if matrix2:
                result = matrix1 + matrix2
                print('\n'.join(map(str, result)))
            else:
                continue
        else:
            continue

    if answer == 5:
        matrix1 = input_single_matrix()
        matrix2 = input_single_matrix()
        if (matrix1 or matrix2) == -1:
            continue
        result = matrix1 - matrix2
        print('\n'.join(map(str, result)))

    if answer == 6:
        rows1 = int(input("Введите кол-во строк для первой матрицы: "))
        columns1 = int(input("Введите кол-во столбцов для первой матрицы: "))
        matrix1 = list()
        print("Построчно введите значения элементов матрицы через пробел (ввел строку, нажал Enter)")
        for i in range(rows1):
            tmp_input = list(map(int, input().split()))
            if len(tmp_input) == columns1:
                matrix1.append(tmp_input)
            else:
                print("\nТы не справился, попробуй еще раз! \n")
                break

        rows2 = int(input("Введите кол-во строк для второй матрицы: "))
        columns2 = int(input("Введите кол-во столбцов для второй матрицы: "))
        if columns1 != rows2:
            print("Учи матчасть!")
            continue
        matrix2 = list()
        print("Построчно введите значения элементов матрицы через пробел (ввел строку, нажал Enter)")
        for i in range(rows2):
            tmp_input = list(map(int, input().split()))
            if len(tmp_input) == columns2:
                matrix2.append(tmp_input)
            else:
                print("\nТы не справился, попробуй еще раз! \n")
                break
        matrix1 = Matrix(matrix1)
        matrix2 = Matrix(matrix2)
        print(matrix1 * matrix2)

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


