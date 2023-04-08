# File: main.py
import commands
import argparse
from data import load

from functions import *

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan

# user yang sedang login
active_user = 0 

# Mengisi users, candi, dan bahan_bangunan menggunakan file
users = load(r"file\user.csv", users) # Matrix data user
candi = load(r"file\candi.csv", candi) # Matrix data user
bahan_bangunan = load(r"file\bahan_bangunan.csv", bahan_bangunan) # Matrix data user

role = [0] # Untuk menentukan apakah ada user yang sedang login atau tidak

# Menerima masukan
while True:
    masukan = input(">>> ")
    commands.run(masukan,users,candi,bahan_bangunan,role)
    
    N = len_count(users)

    for i in range(N):
        if i != 0:
            print(users[i])