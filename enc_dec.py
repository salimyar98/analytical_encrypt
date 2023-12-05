from decimal import Decimal, ROUND_HALF_UP


def round_numbers(numbers: list[int]):  # Округление значений обратной матрицы
    rounded_numbers = [Decimal(str(num)).quantize(Decimal('1e-{0}'.format(0)), rounding=ROUND_HALF_UP) for num in numbers]
    return rounded_numbers


def multiply_matrix_vector(matrix: list[int], vector: list[int]):  # умножение матрицы на вектор
    result = [0, 0, 0]
    
    for i in range(3):
        for j in range(3):
            result[i] += matrix[i][j] * vector[j]

    return result


def inverse_matrix(matrix: list[int]):  # вычисление обратной матрицы

    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    determinant = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

    if determinant == 0:
        raise ValueError("Обратной матрицы не существует, так как определитель равен нулю")

    # Вычисляем матрицу алгебраических дополнений
    adj = [
        [(e * i - f * h), (c * h - b * i), (b * f - c * e)],
        [(f * g - d * i), (a * i - c * g), (c * d - a * f)],
        [(d * h - e * g), (b * g - a * h), (a * e - b * d)]
    ]

    # Находим обратную матрицу путем деления матрицы алгебраических дополнений на определитель
    inverse = [[adj[i][j] / determinant for j in range(3)] for i in range(3)]

    return inverse
