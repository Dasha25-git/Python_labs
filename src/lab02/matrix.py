# Функция, меняющая строки и столбцы матрицы местами
def transpose(mat):
    # Если список пустой, то нам нечего возвращать - возвращаем пустой список
    if mat == []:
        return []
    # Проверяем, что все строки одинаковой длины
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            raise ValueError("Рваная матрица")
    # Транспонирование
    result = []
    for j in range(row_len):  # Пробегаемся по столбцам
        new_row = []
        for i in range(len(mat)):  # Пробегаемся по строкам
            new_row.append(mat[i][j])
        result.append(new_row)
    return result


# Сумма по каждой строке
def row_sums(mat):
    if mat == []:
        return []
    # Проверим , что матрица прямоугольная
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            raise ValueError("Рваная матрица")
    # Суммируем по строкам
    sums = []
    for row in mat:
        sums.append(sum(row))
    return sums


# Сумма по столбцам
def col_sums(mat):
    if mat == []:
        return []
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            raise ValueError("Рваная матрица")
    # Суммируем по столбцам
    sums = [0] * row_len  # Создаем список, где столько 0, сколько стб в матрице
    for row in mat:
        for j in range(row_len):
            sums[j] += row[j]
    return sums


# Тест-кейсы

# Тест для transpose
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
# print(transpose([[1,2],[3]]))

# Тест для row_sums
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([[1,2],[3]]))

# Тест для col_sums
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
# print(col_sums([[1,2],[3]]))
