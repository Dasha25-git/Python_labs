from __future__ import annotations
from pathlib import Path
import sys

# Добавляем в sys.path путь к src, чтобы можно было импортировать lab04
SRC_DIR = Path(__file__).resolve().parents[1]
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from lab04.io_txt_csv import read_text, write_csv


def main() -> None:
    # Определяем путь к корню проекта и к папке с данными
    project_root = SRC_DIR.parent
    data_dir = project_root / "data" / "lab04"

    #  Проверка функции read_text
    print("Тест 1. Чтение текста")
    text = read_text(data_dir / "input.txt")  # читаем содержимое файла
    print("Тип результата:", type(text))  # выводим тип результата
    print("Длина текста:", len(text))  # длина считанного текста
    print("Первые 100 символов текста:")  # покажем кусочек текста
    print(text[:100])  # выводим первые 100 символов

    # Проверка функции write_csv
    print("Тест 2. Запись CSV")

    # Пример данных для записи
    rows = [("word", 3), ("test", 5), ("python", 2)]

    # Заголовки CSV
    header = ("word", "count")

    # Путь, куда сохраним файл
    output_path = data_dir / "check.csv"

    # Записываем CSV
    write_csv(rows, output_path, header=header)

    # Выводим сообщение об успешном создании
    print(f"Файл {output_path} успешно создан!")


if __name__ == "__main__":
    main()
