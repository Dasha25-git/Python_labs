from src.lab09.group import Group
from src.lab08.models import Student

g = Group("src/lab09/students.csv")

g.add(Student("Петров Пётр", "2002-05-05", "Группа 2", 4.17))
print(g.list())