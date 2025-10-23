import sys   
sys.path.append('C:\git-home\Python_labs\src')               
from pathlib import Path   
from lab03.text import normalize, tokenize  
from collections import Counter           
from io_txt_csv import read_text, write_csv, ensure_parent_dir 

def main():
    input_path = Path("C:/git-home/Python_labs/data/lab04/input.txt")    
    output_path = Path("C:/git-home/Python_labs/data/lab04/report.csv") 
    encoding = "utf-8"                     
    top_n = 5                             

    # Проверяем, существует ли входной файл
    if not input_path.exists():
        print(f"Ошибка: файл {input_path} не найден!")  
        sys.exit(1)                                     

    # Пробуем прочитать файл 
    try:
        text = read_text(input_path, encoding=encoding)  # читаем весь текст
    except UnicodeDecodeError:
        print("Ошибка кодировки! Попробуйте encoding='cp1251'")  
        sys.exit(1)

    # Проверяем, пустой ли файл
    if not text.strip():          # если только пробелы или пусто
        print("Файл пустой. Создаём пустой отчёт.")
        ensure_parent_dir(output_path)  # создаём папки
        write_csv([], output_path, header=("word", "count"))  # создаём пустой CSV
        return  

    # Нормализация и токенизация текста 
    tokens = tokenize(normalize(text))  # приводим к нижнему регистру и разбиваем на слова

    #  Подсчёт частот 
    freq = Counter(tokens)  # получаем словарь: слово -> количество

    # Сортировка слов: сначала по частоте, потом по слову 
    sorted_items = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

    # Сохраняем результат в CSV 
    ensure_parent_dir(output_path)  # создаём папку, если нет
    write_csv(sorted_items, output_path, header=("word", "count"))

    # Выводим короткую сводку в консоль 
    total = sum(freq.values())          # всего слов
    unique = len(freq)                  # уникальных слов
    top_words = sorted_items[:top_n]    # первые N слов

    print(f"Всего слов: {total}")
    print(f"Уникальных слов: {unique}")
    print(f"Топ-{top_n}:")
    for w, c in top_words:
        print(f"  {w}: {c}")
        
if __name__ == "__main__":
    main()