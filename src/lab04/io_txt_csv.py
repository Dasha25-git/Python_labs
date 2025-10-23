from io_txt_csv import read_text, write_csv
from pathlib import Path

# Проверка функции read_text 
print("Тест 1. Чтение текста ")
text = read_text("../data/lab04/input.txt")
print("Тип результата:", type(text))        
print("Длина текста:", len(text))        
print("Первые 100 символов текста:")
print(text[:100])                           # покажем кусочек текста

# Проверка функции write_csv 
print("Тест 2. Запись CSV ")

# Пример данных для записи
rows = [("word", 3), ("test", 5), ("python", 2)]

# Заголовки CSV
header = ("word", "count")

# Путь, куда сохраним файл
output_path = Path("../data/lab04/check.csv")

# Записываем CSV
write_csv(rows, output_path, header=header)

print(f"Файл {output_path} успешно создан!")



