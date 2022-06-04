import csv

with open("pets.csv", "r") as f:
    # creates a CSV reader
    r = csv.reader(f)
    for line in r:
        print(line)

with open("pets-with-headers.csv", "r") as f:
    # creates a CSV reader
    r = csv.DictReader(f)
    for line in r:
        print(line)

with open("demo.csv", "a") as f:
    # creates a CSV reader
    r = csv.DictWriter(f, fieldnames=["species", "name", "age"])
    r.writerow({"species": "?", "name": "X", "age": -1})
