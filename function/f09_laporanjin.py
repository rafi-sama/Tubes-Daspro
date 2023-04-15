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
    J_rajin = []
    for g in count:
        if count[g] > max_count:
            max_count = count[g]     # Mencari nama jin dengan jumlah kemunculan terbanyak
            J_rajin = [g]
        
        elif count[g] == max_count:
            konso([J_rajin],g)
            
    if len(J_rajin) > 1:     #syarat jin ter-rajin yang didapat lebih dari satu
        awal = J_rajin[0]       # menentukan leksiografis terendah dari list jin ter-rajin
        for item in J_rajin:
            if item < awal:
                awal = item
            
        
        
            
    
    
    print(f"Total Jin: {J_total} \n")
    print(f"Total JIn Pengumpul: {J_kumpul} \n")
    print(f"Total Jin Pembangun: {J_bangun} \n")
    print(f"Jin Terajin: {J_rajin} \n")
    
    
LaporanJin()