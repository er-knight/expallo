import json
import math 
import random
import csv
import argparse

from typing import Dict

def expallo(roll_start: int, roll_end: int, n_experiments: int) -> Dict[int, int]:
    """ expallo means experiment allocator. """

    roll_list   = [roll_no for roll_no in range(roll_start, roll_end+1)]
    experiments = [i for i in range(1, n_experiments+1)] * math.ceil(len(roll_list)/n_experiments)

    random.shuffle(experiments)

    return dict(zip(roll_list, experiments))

def write_to_csv(data: Dict[int, int]) -> None:
    with open("data.csv", "w") as csv_file:
        header = ["Roll Number", "Experiment Number"]
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        for roll, exp in data.items():
            writer.writerow({"Roll Number": roll, "Experiment Number": exp})

def write_to_json(data: Dict[int, int]) -> None:
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("S", type=int, help="roll number starting")
    parser.add_argument("E", type=int, help="roll number ending")
    parser.add_argument("N", type=int, help="number of experiments")
    parser.add_argument("F", choices=["csv", "json"], help="format (csv or json)")

    args = parser.parse_args()

    data = expallo(args.S, args.E, args.N)

    if args.F == "json" : write_to_json(data)
    if args.F == "csv"  : write_to_csv(data)

    print(f"stored in data.{args.F}")