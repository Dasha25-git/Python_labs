from __future__ import annotations
from pathlib import Path
import sys
from collections import Counter

# Добавляем путь к папке src, чтобы можно было импортировать модули lab03 и lab04
SRC_DIR = Path(__file__).resolve().parents[1]
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

# Импортируем функции из прошлых лаб
from lab03.text import normalize, tokenize  
from lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir

def main() -> None:
    # Определяем пути к входным и выходным файлам
    project_root = SRC_DIR.parent
    data_dir = project_root / "data" / "lab04"

    input_path = data_dir / "input.txt"         # входной файл с текстом
    output_path = data_dir / "report.csv"       # файл для итогового отчёта
    encoding = "utf-8"                          # кодировка файла
    top_n = 5                                   # сколько слов показать в топе

    #  Проверяем, существует ли входной файл 
    if not input_path.exists():
        print(f"Ошибка: файл {input_path} не найден!")
        sys.exit(1)

    #  Пробуем прочитать файл 
    try:
        text = read_text(input_path, encoding=encoding)    # читаем весь текст
    except UnicodeDecodeError:
        print("Ошибка кодировки! Попробуйте encoding='cp1251'")
        sys.exit(1)

    #  Проверяем, не пустой ли файл 
    if not text.strip():                    # если только пробелы или пусто
        print("Файл пустой. Создаём пустой отчёт.")
        ensure_parent_dir(output_path)      # создаём папку, если её нет
        write_csv([], output_path, header=("word", "count"))  # создаём пустой CSV
        return

    #  Нормализация текста 
    tokens = tokenize(normalize(text))      # приводим к нижнему регистру и разбиваем на слова

    #  Подсчёт частот 
    freq = Counter(tokens)                  # получаем словарь: {слово: количество}

    #  Сортировка слов: сначала по частоте, потом по алфавиту
    sorted_items = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

    #  Сохраняем результат в CSV 
    ensure_parent_dir(output_path)          # создаём папку, если нет
    write_csv(sorted_items, output_path, header=("word", "count"))

    # Выводим результат в консоль
    total = sum(freq.values())              # всего слов
    unique = len(freq)                      # уникальных слов
    top_words = sorted_items[:top_n]        # первые N слов

    print(f"Всего слов: {total}")
    print(f"Уникальных слов: {unique}")
    print(f"Топ-{top_n}:")
    for w, c in top_words:
        print(f"  {w}: {c}")

if __name__ == "__main__":
    main()