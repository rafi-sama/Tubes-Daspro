# File: main.py
from run import *
import commands.f13_load as data

import os
os.system("cls")

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan

# Mengisi users, candi, dan bahan_bangunan menggunakan file
users = data.load(r"file\user.csv") # Matrix data user
candi = data.load(r"file\candi.csv") # Matrix data user
bahan_bangunan = data.load(r"file\bahan_bangunan.csv") # Matrix data user

active_user = [0,0] # Untuk menentukan apakah ada user yang sedang login atau tidak

# Menerima masukan
running = True
while running:

    command = input(">>> ")

    running_dict = {'value': running}
    run(command,users,candi,bahan_bangunan,active_user,running_dict)
    print("\n", end="")
    running = running_dict['value']
