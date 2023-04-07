# Kodingan Chat GPT

import csv

def load(file_name, variable):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            
load(r"C:\Users\Qk\Documents\College\02. Programming Fundamentals\Assignment\Python\Big Project\Tubes-Daspro\file\candi.csv", "pembuat")