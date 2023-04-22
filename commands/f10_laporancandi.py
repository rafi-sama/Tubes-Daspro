from functions import *


def laporancandi(candi):
    total_candi = 0
    total_pasir = 0
    total_batu = 0
    total_air = 0
    list_candi = []
    list_harga = []
    for i in range(1, arr_len(candi)):
        total_candi += 1
        
    for i in range(1,arr_len(candi)):
        total_pasir += int(candi[i][2])
        total_batu += int(candi[i][3])
        total_air += int(candi[i][4])
    
    def hitungharga(pasir, batu, air):
        return pasir*10000 + batu*15000 + air*7500
    
    for i in range(1, arr_len(candi)):
        list_candi = konso(list_candi, candi[i][0])
        list_harga = konso(list_harga, hitungharga(int(candi[i][2]), int(candi[i][3]), int(candi[i][4])))
        
    id_termahal = 0
    id_temurah = 0
    harga_termahal = 0
    harga_termurah = 9999999
    for i in range(arr_len(list_candi)):
        if harga_termahal < list_harga[i]:
            harga_termahal = list_harga[i]
            id_termahal = list_candi[i]
        if harga_termurah > list_harga[i]:
            harga_termurah = list_harga[i]
            id_temurah = list_candi[i]
        
    
    print(f"Total Candi: {total_candi}")
    print(f"Total Pasir yang digunakan: {total_pasir}")
    print(f"Total Batu yang digunakan: {total_batu}")
    print(f"Total Air yang digunakan: {total_air}")
    print(f"ID Candi Termahal: {id_termahal} (Rp. {harga_termahal})")
    print(f"ID Candi Termurah: {id_temurah} (Rp. {harga_termurah})")
# total_pasir = 0
# total_batu = 0                    #semua bahan-bahan dibikin 0 dulu
# total_air = 0
# arr_pasir = []  
# arr_batu = []
# arr_air = []
# harga_candi = []

# #TOTAL CANDI
# def LaporanCandi (candi):

#     #Globalisasi Varb

#     global total_pasir #variable ini berisi total bahan dari pasir
#     global total_batu #variable ini berisi total bahan dari batu
#     global total_air #variable ini berii total bahan dari air
#     global arr_air #variable ini berisi list bahan air
#     global arr_batu #variable ini berisi list bahan dari batu
#     global arr_pasir #variable ini berisi list bahan dari pasir
#     global harga_candi#variable ini berisi list total harga candi dari perhitungan
    

# #TOTAL PASIR, AIR,DAN BATU YANG DIGUNAKAN

#     for i in range (1,arr_len(candi)):    #iterasi dari baris kedua ke baris terakhir
#         total_pasir += int(candi[i][2])
#         total_batu += int(candi[i][3])       #penambahan tiap data pada masing-masing bahan
#         total_air += int(candi[i][4])        #ke dalam variable yang sudah dikosongkan
#         i += 1


# #ID CANDI TERMAHAL
# #1: Deteksi Bahan                                    
#     for i in range (1,arr_len(candi)):    #masukkan semua data bahan dalam variable list
#         arr_pasir += (candi[i][2])
#         arr_batu += (candi[i][3])         #proses yang dilakukan sama, namun variable yang dihasilkan
#         arr_air += (candi[i][4])          #bertipe nested list seperti pasir = [2,4,3,1], air = [3,5,6,1]
#         i += 1


# #2: perhitungan
#     c = 0

#     for i in range(arr_len(arr_air)):
#         total_i = 10000*(int(arr_pasir[c])) + 15000*(int(arr_batu[c])) + 7500*(int(arr_air[c])) 
#         harga_candi += [total_i]  
#         c += 1
    
# #PENENTUAN CANDI TERBESAR DAN TERKECIL
#     maks = harga_candi[0]   
#     min = harga_candi[0]
#     for c in harga_candi:               #karena list harga_candi sudah dibuat, kita tinggal menentukan data terbesar         
#         if c > maks:                    #atau terkecil dari list tersebut
#             maks = c
#         elif c < min:
#             min = c    

#     max_score = -1
#     max_id = ''
#     for i in range(1, len(candi)):
#         cur_id = candi[i][0]
#         cur_pasir = int(candi[i][2])
#         cur_batu = int(candi[i][3])
#         cur_air = int(candi[i][4])

#         cur_score = cur_pasir + cur_batu + cur_air

#         if cur_score > max_score:
#             max_score = cur_score
#             max_id = cur_id
    
    
    
    
    
    
    
    
    
    
    
    

    


#     print(f"Total Candi: {arr_len(candi)-1} \n")
#     print(f"Total Pasir yang digunakan: {total_pasir} \n")
#     print(f"Total Batu yang digunakan: {total_batu} \n")
#     print(f"Total Air yang digunakan: {total_air} \n")
#     print(f"ID Candi Termahal: {max_id} (Rp: {maks}) \n")
#     print(f"ID Candi Termurah: (Rp: {min}) \n")