from functions import *


arr_pasir = []  
arr_batu = []
arr_air = []
harga_candi = []



#TOTAL CANDI
def LaporanCandi (candi):
    total_pasir = 0
    total_batu = 0                    #semua bahan-bahan dibikin 0 dulu
    total_air = 0
    #Globalisasi Varb
    
    global arr_air #variable ini berisi list bahan air
    global arr_batu #variable ini berisi list bahan dari batu
    global arr_pasir #variable ini berisi list bahan dari pasir
    global harga_candi#variable ini berisi list total harga candi dari perhitungan
    

#TOTAL PASIR, AIR,DAN BATU YANG DIGUNAKAN
    sum_candi = arr_len(candi)
    for i in range (1,sum_candi - 1):    #iterasi dari baris kedua ke baris terakhir
        total_pasir += int(candi[i][2])
        total_batu += int(candi[i][3])       #penambahan tiap data pada masing-masing bahan
        total_air += int(candi[i][4])        #ke dalam variable yang sudah dikosongkan
        i += 1


#ID CANDI TERMAHAL
#1: Deteksi Bahan                                    
    for i in range (1,sum_candi - 1):    #masukkan semua data bahan dalam variable list
        arr_pasir += (candi[i][2])
        arr_batu += (candi[i][3])         #proses yang dilakukan sama, namun variable yang dihasilkan
        arr_air += (candi[i][4])          #bertipe nested list seperti pasir = [2,4,3,1], air = [3,5,6,1]
        i += 1


#2: perhitungan
    c = 0

    for i in range(1,arr_len(arr_batu)):
        total_i = 10000*(int(arr_pasir[c])) + 15000*(int(arr_batu[c])) + 7500*(int(arr_air[c])) 
        harga_candi += [total_i]  
        c += 1
    
#PENENTUAN CANDI TERBESAR DAN TERKECIL
    maks = harga_candi[0]   
    min = harga_candi[0]
    for c in harga_candi:               #karena list harga_candi sudah dibuat, kita tinggal menentukan data terbesar         
        if c > maks:                    #atau terkecil dari list tersebut
            maks = c
        elif c < min:
            min = c    

    max_score = -1
    max_id = ''
    for i in range(1, arr_len(candi)):
        cur_id = candi[i][0]
        cur_pasir = int(candi[i][2])
        cur_batu = int(candi[i][3])
        cur_air = int(candi[i][4])

        cur_score = cur_pasir + cur_batu + cur_air

        if cur_score > max_score:
            max_score = cur_score
            max_id = cur_id
    
    
    if candi == 0 or []:
        print("Total Candi: 0")
        print("Total Pasir yang digunakan: 0")
        print("Total Batu yang digunakan: 0")
        print("Total Air yang digunakan: 0")
        print("ID Candi Termahal: -")
        print(f"ID Candi Termurah: -")
    
        
    
    
    
    
    
    
    
    


    print(f"Total Candi: {sum_candi-1} \n")
    print(f"Total Pasir yang digunakan: {total_pasir} \n")
    print(f"Total Batu yang digunakan: {total_batu} \n")
    print(f"Total Air yang digunakan: {total_air} \n")
    print(f"ID Candi Termahal: {max_id} (Rp: {maks}) \n")
    print(f"ID Candi Termurah: (Rp: {min}) \n")
    
    
    #fnioe