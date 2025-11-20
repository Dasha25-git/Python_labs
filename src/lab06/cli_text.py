import argparse
from pathlib import Path
from collections import Counter
import re


def main():
    #создаем объем, который будет разбирать аргументы командной строки
    parser = argparse.ArgumentParser(description="CLI-утилиты: cat и stats")
    subparsers = parser.add_subparsers(dest="command") #подкоманды 

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Текстовый файл")
    stats_parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Сколько слов показать (по умолчанию 5)",
    )

    args = parser.parse_args() #смотрим, что пользователь написал в командной строке

    if args.command is None:
        parser.error("Нужно указать подкоманду: cat или stats")

    if args.command == "cat":
        path = Path(args.input)
        if not path.exists():
            raise FileNotFoundError(path)

        text = path.read_text(encoding="utf-8") #читаем весь файл как одну строку 

        for i, line in enumerate(text.splitlines(), start=1): #splitlines() - разбивает текст на список строк 
            if args.n:
                print(f"{i}\t{line}")
            else:
                print(line)

    elif args.command == "stats":
        if args.top <= 0:
            parser.error("top должно быть положительным числом")

        path = Path(args.input)
        if not path.exists():
            raise FileNotFoundError(path)

        text = path.read_text(encoding="utf-8")
        if text.strip() == "":
            parser.error("Файл пустой")

        # простейший разбор слов
        words = re.findall(r"\w+", text.lower())
        counts = Counter(words)

        for word, count in counts.most_common(args.top):
            print(f"{word}\t{count}")


if __name__ == "__main__":
    main()