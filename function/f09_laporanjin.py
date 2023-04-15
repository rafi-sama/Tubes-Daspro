from functions import *
import random
def LaporanJin (list_jin,users, candi):
    J_bangun = 0
    J_kumpul = 0
    i = 3
    pp = arr_len(users)
    
    for i in range (1,pp):
        if users[i][2] == "Pengumpul":
            J_kumpul += 1
        elif users[i][2] == "Pembangun":
            J_bangun += 1
        
        i += 1
        
    J_total = J_bangun + J_kumpul
    
    count = {}
    for i in range(1, len(users)):
        if users[i][1] in count:       #Menghitung Jumlah Kemunculan semua data di kolom kedua dalam list candi, yaitu nama jin
            count[users[i][1]] += 1
        else:
            count[users[i][1]] = 1


    max_count = 0
    J_rajin = ""
    for key in count:
        if count[key] > max_count:
            max_count = count[key]     # Mencari nama jin dengan jumlah kemunculan terbanyak
            J_rajin = key
    
    print(f"Total Jin: {J_total} \n")
    print(f"Total JIn Pengumpul: {J_kumpul} \n")
    print(f"Total Jin Pembangun: {J_bangun} \n")
    print(f"Jin Terajin: {J_rajin} \n")
    
    
LaporanJin()