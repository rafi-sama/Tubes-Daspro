# Kodingan Chat GPT

import csv

def load(file_name, variable):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    globals()[variable] = data