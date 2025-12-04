import json
from models import Student

def students_to_json(students: list[Student], path: str) -> None:
    # Список объектов Student -> список словарей
    data = [s.to_dict() for s in students]
    # Записываем JSON в файл
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path: str) -> list[Student]:
    # Читаем JSON из файла
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Список словарей -> список объектов Student
    return [Student.from_dict(d) for d in data]