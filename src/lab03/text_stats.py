import sys
from text import normalize, tokenize, count_freq, top_n


def main():
    input_text = sys.stdin.read()

    if not input_text.strip():
        print("Ошибка: не введен текст")
        return

    normalized_text = normalize(input_text)
    tokens = tokenize(normalized_text)
    frequencies = count_freq(tokens)
    top_words = top_n(frequencies, n=5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(frequencies)}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
