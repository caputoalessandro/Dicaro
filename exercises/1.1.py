from res import RESOURCES_PATH
import csv


def get_defs():
    defs = {}
    defs.setdefault("courage", [])
    defs.setdefault("paper", [])
    defs.setdefault("apprehension", [])
    defs.setdefault("sharpener", [])

    defs_file = RESOURCES_PATH / "defs.csv"

    with open(defs_file) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            defs.get("courage").append(row[1])
            defs.get("paper").append(row[2])
            defs.get("apprehension").append(row[3])
            defs.get("sharpener").append(row[4])

    return defs


def similarity():
    defs = get_defs()
    print("we")


if __name__ == "__main__":
    similarity()