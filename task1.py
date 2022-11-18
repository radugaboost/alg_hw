## Сложность данного алгоритма O(n*m)
def countSquares(matrix):
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] > 0:
                # Если элемент матрицы больше нуля то пытаемся расширить квадрат путём нахождения минимального из левого, верхнего и диагонального соседа
                matrix[i][j] = 1+min(matrix[i][j-1],
                                        matrix[i-1][j-1], matrix[i-1][j])
    # После обхода матрицы, проходимся по всем её элементам и находим их сумму
    s = 0
    for el in matrix:
        s += sum(el)
    return s