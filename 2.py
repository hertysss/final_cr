import json
import csv
from argparse import ArgumentParser



def write_data(data):
    with open("toys.json", 'w') as f:
        json.dump(data, f)


def get_data(param, smallest):
    with open('ships.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        data = []
        k = "name;year;length;load;crew;distance;engines"
        for dct in reader:
            d = {}
            for i, j in zip(k.split(";"), dct[k].split(";")):
                d[i] = j
            if int(d[param]) >= smallest:
                data.append(d)
        return data


def analyzed_data(data, key, smaller, accuracy):
    pass


parser = ArgumentParser()
parser.add_argument("--param", type=str)
parser.add_argument("--smallest", type=int, default=0)
args = parser.parse_args()
param, smallest = args.param, args.smallest
data = get_data(param, smallest)
print(data)
write_data(data)