# File: main.py
from run import *
import commands.f13_load as data

import os
os.system("cls")

from my_class import *

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
TabUser = [] # Matriks data user
TabCandi = [] # Matriks data candi
TabBahan = [] # Data bahan bangunan

trash = [[]]

# Mengisi users, candi, dan bahan_bangunan menggunakan file
TabUser = data.load(r"file\user.csv", "user") # Matrix data user
TabCandi = data.load(r"file\candi.csv", "candi") # Matrix data user
TabBahan = data.load(r"file\bahan_bangunan.csv", "bahan") # Matrix data user

active_user = [0,0] # Untuk menentukan apakah ada user yang sedang login atau tidak

# Menerima masukan
# running = [1]
# while running[0] != 0:

#     command = input(">>> ")

#     users,\
#     candi,\
#     bahan_bagunanrun\
#           = run\
#                 (command,\
#                 users,\
#                 candi,\
#                 bahan_bangunan,\
#                 active_user,\
#                 running,\
#                 trash)

#     print("\n", end="")

print("TabUser:")
for element in TabUser:
    print(element)

print("\nTabBahan:")
for element in TabBahan:
    print(element)

print("\nTabCandi:")
for element in TabCandi:
    print(element)
