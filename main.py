# File: main.py
import commands
<<<<<<< HEAD
import commands.f13_load as data
=======
import command.f13_load as data
>>>>>>> bb1230600bf9cfe4ed45364e516a4e002505ff04

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

iterasi = 0 

# Menerima masukan
<<<<<<< HEAD
running = True
while running:

    command = input(">>> ")

    running_dict = {'value': running}
    commands.run(command,users,candi,bahan_bangunan,active_user,running_dict)
    print("\n", end="")
    running = running_dict['value']
=======
running = [1]
while running[0] == 1:
    
    if iterasi == 0:
        masukan = input(">>> ")

    else:
        masukan = input("\n>>> ")

    iterasi += 1
    commands.run(masukan,users,candi,bahan_bangunan,active_user, running)
>>>>>>> bb1230600bf9cfe4ed45364e516a4e002505ff04
