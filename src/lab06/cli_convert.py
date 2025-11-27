import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры JSON/CSV/XLSX")
    sub = parser.add_subparsers(dest="cmd")

    # json2csv
    p1 = sub.add_parser("json2csv", help="JSON -> CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV")

    # csv2json
    p2 = sub.add_parser("csv2json", help="CSV -> JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON")

    # csv2xlsx
    p3 = sub.add_parser("csv2xlsx", help="CSV -> XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX")

    args = parser.parse_args()

    if args.cmd is None:
        parser.error("Нужно указать подкоманду: json2csv, csv2json или csv2xlsx")

    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.cmd == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError:
        raise
    except ValueError as e:
        parser.error(str(e))


if __name__ == "__main__":
    main()
