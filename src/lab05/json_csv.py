from pathlib import Path
import json
import csv


def json_to_csv(json_path: str, csv_path: str) -> None:

    # Проверяем расширения файлов: вход должен быть .json, выход .csv
    if Path(json_path).suffix.lower() != ".json":
        raise ValueError(f"Неверный тип файла: {json_path}")
    if Path(csv_path).suffix.lower() != ".csv":
        raise ValueError(f"Неверный тип файла: {csv_path}")

    jpath = Path(json_path)  # путь к исходному JSON
    cpath = Path(csv_path)  # путь к будущему CSV

    # Проверяем, что входной файл существует
    if not jpath.exists():
        raise FileNotFoundError(jpath)

    # Читаем JSON как текст и убеждаемся, что он не пустой
    raw = jpath.read_text(encoding="utf-8")
    if raw.strip() == "":  # если после удаления пробелов = пустая строка
        raise ValueError("Пустой JSON файл")

    try:
        data = json.loads(raw)  # ожидаем список словарей
    except json.JSONDecodeError:
        raise ValueError("Невалидный JSON")

    if not isinstance(data, list):
        raise ValueError("Ожидается список словарей")
    if data and not isinstance(data[0], dict):
        raise ValueError("Каждый элемент должен быть словарём")

    # Собираем все имена полей (ключи) и сортируем их по алфавиту — это заголовок CSV файла
    keys = set()  # здесь будем накапливать все ключи
    for item in data:  # проходим по каждому объекту из списка
        if not isinstance(item, dict):
            raise ValueError("Элемент списка не является словарём")
        keys.update(item.keys())  # добавляем ключи текущего словаря
    header = sorted(keys)  # итоговый заголовок — это отсортированные ключи

    # Пишем CSV: сначала заголовок, затем строки
    with cpath.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header)  # записываем словари как строки CSV
        w.writeheader()  # первая строка — имена колонок
        for row in data:  # перебираем все объекты из JSON
            # если какого-то ключа нет в объекте, ставим пустую строку
            w.writerow({k: row.get(k, "") for k in header})


def csv_to_json(csv_path: str, json_path: str) -> None:

    # Проверяем расширения файлов
    if Path(csv_path).suffix.lower() != ".csv":
        raise ValueError(f"Неверный тип файла: {csv_path}")
    if Path(json_path).suffix.lower() != ".json":
        raise ValueError(f"Неверный тип файла: {json_path}")

    cpath = Path(csv_path)  # путь к исходному CSV
    jpath = Path(json_path)  # путь к будущему JSON

    # Проверяем, что CSV существует
    if not cpath.exists():
        raise FileNotFoundError(cpath)

    # Проверяем, что CSV не пустой
    txt = cpath.read_text(encoding="utf-8")
    if txt.strip() == "":
        raise ValueError("Пустой CSV файл")

    with cpath.open("r", encoding="utf-8", newline="") as f:
        # пытаемся угадать разделитель по образцу первых символов
        sample = f.read(2048)
        f.seek(0)  # возвращаемся в начало файла после чтения образца
        try:
            dialect = csv.Sniffer().sniff(sample)  # попытка распознавания разделителя
        except Exception:
            dialect = csv.excel  # если не получилось — запятую (это по умолчанию)
        reader = csv.DictReader(f, dialect=dialect)  # первая строка — заголовок

        if reader.fieldnames is None:  # если заголовка не оказалось
            raise ValueError("В CSV отсутствует заголовок")

        # превращаем все строки в обычные словари (значения сохраняются как строки)
        rows = [dict(r) for r in reader]

    with jpath.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
