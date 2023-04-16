from functions import *





def LaporanCandi (candi):
    #TOTAL CANDI
    sum_candi = arr_len(candi) - 1
    total_pasir = 0
    total_batu = 0                    #semua bahan-bahan dibikin 0 dulu
    total_air = 0
    arr_pasir = []  
    arr_batu = []
    arr_air = []
    harga_candi = []                       #variable ini berisi list total harga candi dari perhitungan
    #TOTAL PASIR, AIR,DAN BATU YANG DIGUNAKAN
  
    for i in range (1,arr_len(candi)):    #iterasi dari baris kedua ke baris terakhir
        total_pasir += int(candi[i][2])
        total_batu += int(candi[i][3])       #penambahan tiap data pada masing-masing bahan
        total_air += int(candi[i][4])        #ke dalam variable yang sudah dikosongkan
        i += 1
    
    
    #ID CANDI TERMAHAL
    #1: Deteksi Bahan                                    
    for i in range (1,arr_len(candi)):    #masukkan semua data bahan dalam variable list
        arr_pasir += (candi[i][2])
        arr_batu += (candi[i][3])         #proses yang dilakukan sama, namun variable yang dihasilkan
        arr_air += (candi[i][4])          #bertipe nested list seperti pasir = [2,4,3,1], air = [3,5,6,1]
        i += 1
    
   
   #2: perhitungan
    c = 0
    for i in range(arr_len(arr_air)):
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

    
    
    if sum_candi == 0:
        total_pasir = 0
        total_batu = 0                    #sebenarnya syarat ini tidak perlu, tapi saya takut akan adanya 
        total_air = 0                     #kesalahan perhitungan
        candi_mahal = '-'
        candi_murah = '-'
    
    
    #ID CANDI TERMAHAL


    #HITUNG HARGA CANDI
        
    
    
    
    
    
    
    
    
    

    print(f"Total Pasir yang digunakan: {total_pasir} \n")
    print(f"Total Batu yang digunakan: {total_batu} \n")
    print(f"Total Air yang digunakan: {total_air} \n")
    print(f"ID Candi Termahal: {candi_mahal} \n")
    print(f"ID Candi Termurah: {candi_murah} \n")


