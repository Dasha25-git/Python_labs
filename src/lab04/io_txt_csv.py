from __future__ import annotations
from pathlib import Path
import csv
from typing import Iterable, Sequence, Optional, Tuple

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)                              # создаём объект пути
    # читаем содержимое файла в строку, используя указанную кодировку
    return p.read_text(encoding=encoding)

def write_csv(
    rows: list[tuple[str, int]] | list[tuple[str, str]], #список строк таблицы 
    path: str | Path, #путь, куда сохраняем csv-файл
    header: tuple[str, str] = ("word", "count"), #заголовки столбцов (1 строка csv)
    encoding: str = "utf-8",
) -> None:
    p = Path(path) #путь преобраз. в объект 

    # Преобразуем переданные данные в список
    rows = list(rows)

    # Проверяем, что все строки одинаковой длины
    if rows:  # если список не пустой
        row_len = len(rows[0])  # длина первой строки
        for r in rows:
            if len(r) != row_len:
                raise ValueError("Все строки должны быть одинаковой длины!")

    # Открываем файл для записи
    with p.open("w", newline="", encoding=encoding) as f:
        w = csv.writer(f)  # создаём writer для CSV

        # если есть header — записываем его
        if header is not None:
            w.writerow(header)

        # записываем все строки по очереди
        for r in rows:
            w.writerow(r)

def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    parent = p.parent                          # получаем родительскую папку
    parent.mkdir(parents=True, exist_ok=True)  # создаём, если нет

if __name__ == "__main__":
    # Мини-тест (создаёт io_txt_csv_demo.csv рядом)
    demo_csv = Path(__file__).resolve().with_name("io_txt_csv_demo.csv")
    write_csv([("hello", 2), ("world", 3)], demo_csv)
    print(f"CSV записан: {demo_csv}")






