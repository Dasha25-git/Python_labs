import csv
import json
from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from lab05.json_csv import json_to_csv, csv_to_json

# Позитивный тест


def test_json_to_csv_roundtrip(tmp_path: Path):
    # Автоматически создаём папку для теста и временные файлы в ней:
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"

    # Список словарей - тестовые данные
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]

    # Запись json
    src.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    json_to_csv(str(src), str(dst))  # Вызываем функцию

    with dst.open(encoding="utf-8", newline="") as f:  # Открываем файл
        rows = list(
            csv.DictReader(f)
        )  # Возвращаем по строке словарь и оборачиваем в список

    assert len(rows) == len(data)  # assert - проверка
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    rows = [
        {"name": "Alice", "age": "22"},
        {"name": "Bob", "age": "25"},
    ]

    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    csv_to_json(str(src), str(dst))

    data = json.loads(dst.read_text(encoding="utf-8"))

    assert len(data) == len(rows)
    assert {"name", "age"} <= set(data[0].keys())


# Негативный тест (ищет ошибку)
def test_json_to_csv_empty_file(tmp_path: Path):
    src = tmp_path / "empty.json"
    dst = tmp_path / "out.csv"

    # Записываем в файл пустую строку
    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_empty_file(tmp_path: Path):
    src = tmp_path / "empty.csv"
    dst = tmp_path / "out.json"

    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))


# Проверка на несуществующий файл
def test_json_to_csv_file_not_found(tmp_path: Path):
    src = tmp_path / "no_such_file.json"
    dst = tmp_path / "out.csv"

    with pytest.raises(FileNotFoundError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_file_not_found(tmp_path: Path):
    src = tmp_path / "no_such_file.csv"
    dst = tmp_path / "out.json"

    with pytest.raises(FileNotFoundError):
        csv_to_json(str(src), str(dst))
