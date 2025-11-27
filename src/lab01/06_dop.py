N = int(input("Введите количество участников:"))
count1 = 0
count2 = 0
for i in range(N):
    participant = input("Введите ФИО, возраст и формат обучения:")
    participant = participant.split()  # разбиваем строку по пробелам и создаем список
    format = participant[-1]  # достаем последний элемент в списке
    if format == "True":  # (True - восприн как строка)
        count1 += 1
    else:
        count2 += 1
print(count1, count2)
