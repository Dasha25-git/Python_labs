# Функция для поиска макс и мин
def min_max(nums):
    # Если список пуст, то вернем ошибку
    if len(nums) == 0:
        raise ValueError("Список пустой")
    # Если список не пустой, ищем макс и мин значения
    min_num = min(nums)
    max_num = max(nums)
    return (min_num, max_num)  # Возвращаем кортеж


# Функция для сортировки уникальных значений
def unique_sorted(nums):
    # Преобразуем список в множество (set), т.к. в множестве нет дубликатов
    unique = set(nums)
    # Преобразовываем обратно в список
    unique = list(unique)
    # Сортировка
    unique.sort()
    return unique  # Возвращаем отсортированный список


# "Расплющивание" списка списков/кортежей в один список по строкам
def flatten(mat):
    result = []
    for row in mat:
        # Проверка: это список или кортеж
        if type(row) not in [list, tuple]:
            raise TypeError("Не является списком/кортежем")
        result += row
    return result


# Тест-кейсы

# Тест для min/max
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
# print(min_max([])) ВЫДАЁТ ОШИБКУ
print(min_max([1.5, 2, 2.0, -3.1]))

# Тест для unique_sorted
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

# Тест для flatten
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
# print(flatten([[1,2],"ab"])) ВЫДАЁТ ОШИБКУ
