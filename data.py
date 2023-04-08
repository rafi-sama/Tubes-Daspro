import csv

def load(file_name, variable):
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ";")
        variable = [row for row in reader]
    return variable