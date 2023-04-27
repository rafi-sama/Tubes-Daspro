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

candi = [["id","pembuat","pasir","batu","air"],
        ["1","kirito","2","3","4"],
        ['2','asuna','4','1','3'],
        ['3','rimuru','3','1','3'],
        ['4','tempest','1','2','4'],
        ['5','ud','5','6','3'],
        ["6",'ud','6','8','9']]

user = [['username','password','role'],
['Bondowoso','cintaroro','bandung_bondowoso'],
['Roro','gasukabondo','roro_jonggrang'],
['asuna','kirito','Pengumpul'],
['hori','miyamura','Pembangun']]

def LaporanJin (users, candi):
    global list_jin
    

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
    
    
            
    list_jin = [candi[i][1] for i in range(1, arr_len(candi))]    # Berisi Kemunculan semua data di kolom kedua dalam list candi, yaitu nama jin


    

    # membuat list unik dari list_jin
    data_unik = []
    for i in range(arr_len(list_jin)):
        is_unik = True
    for j in range(arr_len(data_unik)):
        if list_jin[i] == data_unik[j]:
            is_unik = False
            break
    if is_unik:
        data_unik = data_unik + [list_jin[i]]

    # menghitung jumlah kemunculan masing-masing data pada list_jin
    jumlah_kemunculan = [0] * arr_len(data_unik)
    for i, data in enumerate(data_unik):
        for j in range(arr_len(list_jin)):
            if list_jin[j] == data:
                jumlah_kemunculan[i] += 1

    # mencari data dengan kemunculan terbanyak
    max_kemunculan = max(jumlah_kemunculan)
    J_rajin = []
    for i in range(arr_len(jumlah_kemunculan)):
        if jumlah_kemunculan[i] == max_kemunculan:
            J_rajin += [data_unik[i]]

    # mencari data dengan kemunculan terendah
    min_kemunculan = min(jumlah_kemunculan)
    J_malas = []
    for i in range(arr_len(jumlah_kemunculan)):
        if jumlah_kemunculan[i] == min_kemunculan:
            J_malas += [data_unik[i]]














    if arr_len(J_rajin) > 1:     #syarat jin ter-rajin yang didapat lebih dari satu
        awal = J_rajin[0]       # menentukan leksiografis terendah dari list jin ter-rajin
        for item in J_rajin:
            if item < awal:
                awal = item
                

            
            
    if arr_len(J_malas) > 1:        # jika jin termalas yang didapat lebih dari satu
        awal = J_malas[0]       # menentukan leksiografis tertinggi dari list jin termalas
        for item in J_malas:
            if item > awal:
                awal = item