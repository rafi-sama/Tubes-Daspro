# File: main.py
import commands
from data import load

import os

from functions import *

os.system("cls")

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan

# Mengisi users, candi, dan bahan_bangunan menggunakan file
users = load(r"file\user.csv", users) # Matrix data user
candi = load(r"file\candi.csv", candi) # Matrix data user
bahan_bangunan = load(r"file\bahan_bangunan.csv", bahan_bangunan) # Matrix data user

active_user = [0,0] # Untuk menentukan apakah ada user yang sedang login atau tidak

iterasi = 0 

# Menerima masukan
while True:

    users = load(r"file\user.csv", users) # Matrix data user
    candi = load(r"file\candi.csv", candi) # Matrix data user
    bahan_bangunan = load(r"file\bahan_bangunan.csv", bahan_bangunan) # Matrix data user
    if iterasi == 0:
        masukan = input(">>> ")

    else:
        masukan = input("\n>>> ")

    iterasi += 1

    commands.run(masukan,users,candi,bahan_bangunan,active_user)