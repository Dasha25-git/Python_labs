from models import Student
from serialize import students_to_json, students_from_json

# создаём пару студентов
s1 = Student("Дарья Коробцова", "2007-05-25", "SE-01", 4.9)
s2 = Student("Петров Петр", "2001-01-20", "SE-01", 3.8)

students = [s1, s2]

# сохраняем в файл
students_to_json(students, "students.json")

# читаем из файла
loaded = students_from_json("students.json")

for s in loaded:
    print(s, "| возраст:", s.age())