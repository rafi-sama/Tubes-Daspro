from functions import *

def LaporanCandi (candi,bahan_bangunan):
    #TOTAL CANDI
    sum_candi = arr_len(candi) - 1


    #TOTAL PASIR, AIR,DAN BATU YANG DIGUNAKAN
    total_pasir = 0
    total_batu = 0                    #semua bahan-bahan dibikin 0 dulu
    total_air = 0

    for row in candi[1:]:
        total_pasir += int(row[2])
        total_batu += int(row[3])           #iterasi dari baris kedua hingga akhir dalam candi, dimana tiap data
        total_air += int(row[4])            #dari kolom tersebut ditambahkan
    
    
    
    #ID CANDI TERMAHAL
    
    
    
    
    
    
    
    
    
    
    if sum_candi == 0:
        total_pasir = 0
        total_batu = 0                    #sebenarnya syarat ini tidak perlu, tapi saya takut akan adanya 
        total_air = 0                     #kesalahan perhitungan
        candi_mahal = '-'
        candi_murah = '-'
    print(f"Total Pasir yang digunakan: {total_pasir} \n")
    print(f"Total Batu yang digunakan: {total_batu} \n")
    print(f"Total Air yang digunakan: {total_air} \n")
    print(f"ID Candi Termahal: {candi_mahal} \n")
    print(f"ID Candi Termurah: {candi_murah} \n")
    