import sys; sys.path.insert(0, "src")
from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx

json_to_csv("data/out/people.json", "data/out/people_from_json.csv")
csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
csv_to_xlsx("data/samples/cities.csv", "data/out/cities.xlsx")