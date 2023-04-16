# from functions import *

# user_csv = open("file/user.csv",'r')

# user_csv = [row for row in user_csv]

# print(user_csv)

# # for row in user_csv:
# #     print(row)

# baris = len_count(user_csv)

# kolom = 0
# temp = user_csv[0]

# for i in range(len_count(temp)):
#     if temp[i] == ";":
#         kolom = 0

# kolom += 1

# user = ["" for i in range(baris)]


# for i in range(baris):

#     user[i] = split(user_csv[i], ";")

# print(user)

from functions import *
x = [["id","pembuat","pasir","batu","air"],
     ["1","kirito","2","3","4"],
     ['2','asuna','4','1','3'],
     ['3','rimuru','3','1','3'],
     ['4','tempest','1','2','4']]



 #TOTAL CANDI
sum_candi = arr_len(x) - 1
total_pasir = 0
total_batu = 0                    #semua bahan-bahan dibikin 0 dulu
total_air = 0
arr_pasir = []  
arr_batu = []
arr_air = []
harga_candi = []                       #variable ini berisi list total harga x dari perhitungan
#TOTAL PASIR, AIR,DAN BATU YANG DIGUNAKAN

for i in range (1,arr_len(x)):    #iterasi dari baris kedua ke baris terakhir
    total_pasir += int(x[i][2])
    total_batu += int(x[i][3])       #penambahan tiap data pada masing-masing bahan
    total_air += int(x[i][4])        #ke dalam variable yang sudah dikosongkan
    i += 1


#ID CANDI TERMAHAL
#1: Deteksi Bahan                                    
for i in range (1,arr_len(x)):    #masukkan semua data bahan dalam variable list
    arr_pasir += (x[i][2])
    arr_batu += (x[i][3])         #proses yang dilakukan sama, namun variable yang dihasilkan
    arr_air += (x[i][4])          #bertipe nested list seperti pasir = [2,4,3,1], air = [3,5,6,1]
    i += 1


#2: perhitungan
for i in range(5):
    total_i = 10000*arr_pasir[0]

if sum_candi == 0:
    total_pasir = 0
    total_batu = 0                    #sebenarnya syarat ini tidak perlu, tapi saya takut akan adanya 
    total_air = 0                     #kesalahan perhitungan
candi_mahal = 0
candi_murah = 0
print(f"Total Candi: {sum_candi} \n")
print(f"Total Pasir yang digunakan: {total_pasir} \n")
print(f"Total Batu yang digunakan: {total_batu} \n")
print(f"Total Air yang digunakan: {total_air} \n")
print(f"ID Candi Termahal: {candi_mahal} \n")
print(f"ID Candi Termurah: {candi_murah} \n")









