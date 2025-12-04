from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class Student:
    # ФИО студента
    fio: str
    # Дата рождения в формате YYYY-MM-DD
    birthdate: str
    # Группа
    group: str
    # Средний балл от 0 до 5
    gpa: float

    def __post_init__(self) -> None:
        # Проверяем формат даты
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("birthdate должен быть в формате YYYY-MM-DD")
        # Проверяем диапазон gpa
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa должен быть в диапазоне от 0 до 5")

    def age(self) -> int:
        # Полные годы по дате рождения
        b = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        years = today.year - b.year
        # Если день рождения в этом году ещё не был, вычитаем год
        if (today.month, today.day) < (b.month, b.day):
            years -= 1
        return years

    def to_dict(self) -> dict:
        # Преобразуем объект в словарь (для JSON)
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Student":
        # Создаём объект Student из словаря
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=float(d["gpa"]),
        )

    def __str__(self) -> str:
        # Красивый вывод объекта
        return f"{self.fio} ({self.group}), gpa={self.gpa:.2f}"