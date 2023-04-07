# File: main.py
import commands

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan


# Kodingan chat gpt

# gak ngerti gw cooo ini jg gk work sih codenya

import argparse
from data import load

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Load a CSV file into a variable.')
    parser.add_argument(r'C:\Users\Qk\Documents\College\02. Programming Fundamentals\Assignment\Python\Big Project\Tubes-Daspro\file\candi.csv', type=str, help='the name of the CSV file to load')
    parser.add_argument('pembuat', type=str, help='the name of the variable to assign the CSV data to')
    args = parser.parse_args()

    load(args.file_name, args.variable)

load("file/user.csv", users)
load("file/candi.csv", candi)
load("file/bahan_bangunan.csv", bahan_bangunan)

# while True:
#   masukan = input(">>> ")
#   commands.run(masukan)

print(users)