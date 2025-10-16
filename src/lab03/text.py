# Подключаем модуль для работы с регулярными выражениями
import re

def normalize(text, *, casefold=True, yo2e=True):

    # Сохраняем исходный текст в переменную result
    result = text
    
    # Делаем все буквы маленькими 
    if casefold: # casefold() - это способ сделать буквы маленькими для любых языков
        result = result.casefold()
    
    # Меняем букву Ё на Е 
    if yo2e:  
        result = result.replace('ё', 'е')
        result = result.replace('Ё', 'Е')
        
    # Убираем невидимые символы
    control_chars = ['\t', '\n', '\r']
    # Проходим по каждому плохому символу в списке
    for char in control_chars:
        result = result.replace(char, ' ')
    
    # Убираем лишние пробелы
    while '  ' in result:
        result = result.replace('  ', ' ')
    # Убираем пробелы в начале и конце текста, если они есть
    result = result.strip()
    
    # Возвращаем очищенный текст
    return result



def tokenize(text):

    # Создаем правило поиска для наших слов:
    # \w+ - находит одно или больше букв/цифр/подчеркиваний
    # (?:-\w+)* - позволяет внутри слова иметь дефис и продолжение

    pattern = r'\w+(?:-\w+)*'
    
    # Используем наше правило для поиска всех слов в тексте
    tokens = re.findall(pattern, text) # findall - "найти все совпадения"
    
    # Возвращаем список найденных слов
    return tokens



def count_freq(tokens):

    freq_dict = {} 
    
    for token in tokens:
        if token in freq_dict:
            # Если слово уже есть в таблице, увеличиваем счетчик на 1
            freq_dict[token] += 1
        else:
            # Если слова еще нет в таблице, добавляем его и ставим счетчик 1
            freq_dict[token] = 1
    
    return freq_dict



def top_n(freq, n=5):
    # Превращаем словарь в список кортежей
    items = list(freq.items())
    
    # Сортировка пузырьком
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][1] < items[j][1]:
                # Если текущее слово встречается реже следующего, меняем их местами
                items[i], items[j] = items[j], items[i]

            elif items[i][1] == items[j][1]:
                # Если частоты одинаковые, сортируем по алфавиту
                if items[i][0] > items[j][0]:
                    # Если текущее слово идет позже в алфавите, меняем местами
                    items[i], items[j] = items[j], items[i]
    
    # Возвращаем первые N=5 элементов - самые частые слова
    return items[:n]



