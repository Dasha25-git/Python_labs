def tuples(rec):
    # Проверяем что rec - кортеж
    if type(rec) != tuple: 
        raise TypeError("Запись должна быть кортежем")
    
    # Проверяем что в кортеже 3 элемента
    if len(rec) != 3:
        raise ValueError("Кортеж должен содержать 3 элемента")
    
    fio, group, gpa = rec 
    
    # Проверяем типы данных
    if type(fio) != str:
        raise TypeError("ФИО должно быть строкой")
    
    if type(group) != str:
        raise TypeError("Группа должна быть строкой")
    
    if type(gpa) != float and type(gpa) != int:
        raise TypeError("GPA должно быть числом")
    
    # Обработка ФИО
    # Убираем лишние пробелы
    fio = fio.strip()
    
    # Разбиваем ФИО на части
    parts = fio.split()
    
    # Убираем пустые строки
    clean_parts = []
    for part in parts:
        if part != "":
            clean_parts.append(part)
    
    # Проверяем что есть хотя бы фамилия и имя
    if len(clean_parts) < 2:
        raise ValueError("ФИО должно содержать фамилию и хотя бы одно имя")
    
    # Форматируем фамилию (первая буква заглавная)
    surname = clean_parts[0].capitalize()
    
    # Формируем инициалы
    initials = ""
    for i in range(1, len(clean_parts)):
        name = clean_parts[i]
        if len(name) > 0:
            initial = name[0].upper() + "."
            initials += initial
    
    # Объединяем фамилию и инициалы
    formatted_fio = surname + " " + initials
    
    # Обработка группы
    formatted_group = group.strip()
    if formatted_group == "":
        raise ValueError("Группа не может быть пустой")
    
    # Форматируем GPA
    formatted_gpa = f"{gpa:.2f}"
    
    # Собираем итоговую строку
    result = formatted_fio + ", гр. " + formatted_group + ", GPA " + formatted_gpa
    return result

# Тест-кейсы
print(tuples(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(tuples(("Петров Пётр", "IK80-12", 5.0)))
print(tuples(("Петров Пётр Петрович", "IK80-12", 5.0)))
print(tuples((" сидорова анна сергеевна ", "ABB-01", 3.999)))