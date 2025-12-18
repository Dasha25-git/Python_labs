import csv
from pathlib import Path
from src.lab08.models import Student


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        # если файла нет — создаём с заголовком
        if not self.path.exists():
            with open(self.path, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["fio", "birthdate", "group", "gpa"])

    def _read_all(self):
        # читаем все строки из CSV и возвращаем список словарей
        with open(self.path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)

    def list(self):
        # вернуть всех студентов как список объектов Student
        rows = self._read_all()
        return [
            Student(
                fio=r["fio"],
                birthdate=r["birthdate"],
                group=r["group"],
                gpa=float(r["gpa"])
            )
            for r in rows
        ]

    def add(self, student: Student):
        # добавить студента в CSV
        with open(self.path, "a", encoding="utf-8", newline="") as f: #
            writer = csv.writer(f)
            writer.writerow([
                student.fio,
                student.birthdate,
                student.group,
                student.gpa
            ])

    def find(self, substr: str):
        # поиск студентов по подстроке в ФИО
        rows = self._read_all()
        return [
            r for r in rows
            if substr.lower() in r["fio"].lower()
        ]

    def remove(self, fio: str):
        # удалить студента по ФИО
        rows = self._read_all()
        # оставляем только тех студентов, фио которых не совпадает 
        rows = [r for r in rows if r["fio"] != fio] 

        with open(self.path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["fio", "birthdate", "group", "gpa"]
            )
            writer.writeheader()
            writer.writerows(rows)

    def update(self, fio: str, **fields):
        # обновить поля студента по ФИО
        rows = self._read_all()

        for r in rows:
            if r["fio"] == fio:
                for key, value in fields.items():
                    if key in r:
                        r[key] = value

        with open(self.path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["fio", "birthdate", "group", "gpa"]
            )
            writer.writeheader()
            writer.writerows(rows)