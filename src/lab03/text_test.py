import os
import sys

print(f"Текущая директория: {os.getcwd()}")
print(f"Файлы в директории: {os.listdir('.')}")
print(f"Python path: {sys.path}")

# Проверяем существование файла text.py
if os.path.exists('text.py'):
    print("Файл text.py существует")
else:
    print("Файл text.py НЕ существует!")

from text import normalize, tokenize, count_freq, top_n
print("Импорт завершен")

#Тест-кейсы
from text import normalize, tokenize, count_freq, top_n
print("=== normalize ===")
print(normalize("ПрИвЕт\nМир\t"))
print(normalize("ёжик, ёлка", yo2e=True))
print(normalize("Hello\n\nworld"))
print(normalize("  двойные  пробелы  "))

print("\n=== tokenize ===")
print(tokenize("привет мир"))
print(tokenize("hello,world!!"))
print(tokenize("no-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

print("\n=== count_freq + top_n ===")
tokens1 = ["a","b","a","c","b","a"]
freq1 = count_freq(tokens1)
# Выводим словарь, отсортированный по ключам
print(dict(sorted(freq1.items())))
print(top_n(freq1, 2))

tokens2 = ["bb","aa","bb","aa","cc"]
freq2 = count_freq(tokens2)
# Выводим словарь, отсортированный по ключам
print(dict(sorted(freq2.items())))
print(top_n(freq2, 2))
