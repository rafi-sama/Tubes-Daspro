from functions import *

def laporanjin(users, candi, bahan_bangunan):
    nama_pembuat = []
    jumlah_pembuatan = []
    pengumpul = 0
    pembangun = 0
    
    for i in range(arr_len(users)):
        if users[i][2] == "Pengumpul":
            pengumpul += 1
        if users[i][2] == "Pembangun":
            pembangun += 1

    for i in range(1, arr_len(candi)):
        pembuat = candi[i][1]
        found = False
        for j in range(arr_len(nama_pembuat)):
            if nama_pembuat[j] == pembuat:
                found = True
                jumlah_pembuatan[j] += 1
                break
        if not found:
            nama_pembuat = konso(nama_pembuat, pembuat)
            jumlah_pembuatan = konso(jumlah_pembuatan, 1)

    # mencari pembuat dengan pembuatan terbanyak
    pembuat_terbanyak = ''
    jumlah_pembuatan_terbanyak = 0  # inisialisasi dengan nilai nol

    for i in range(arr_len(nama_pembuat)):
        if jumlah_pembuatan[i] > jumlah_pembuatan_terbanyak:
            jumlah_pembuatan_terbanyak = jumlah_pembuatan[i]
            pembuat_terbanyak = nama_pembuat[i]

    # mengecek apakah ada lebih dari satu pembuat dengan pembuatan terbanyak
    jumlah_terbanyak_sama = 0
    for i in range(arr_len(nama_pembuat)):
        if jumlah_pembuatan[i] == jumlah_pembuatan_terbanyak:
            jumlah_terbanyak_sama += 1
            
    if jumlah_terbanyak_sama > 1:
        nama_pembuat_terbanyak = []
        for i in range(len(nama_pembuat)):
            if jumlah_pembuatan[i] == jumlah_pembuatan_terbanyak:
                nama_pembuat_terbanyak = konso(nama_pembuat_terbanyak, nama_pembuat[i])
        pembuat_terbanyak = sorting_arr_leks(nama_pembuat_terbanyak)[0]

    # mencari pembuat dengan pembuatan terkecil
    pembuat_terkecil = ''
    jumlah_pembuatan_terkecil = arr_len(candi) - 1  # inisialisasi dengan nilai maksimal

    for i in range(arr_len(nama_pembuat)):
        if jumlah_pembuatan[i] < jumlah_pembuatan_terkecil:
            jumlah_pembuatan_terkecil = jumlah_pembuatan[i]
            pembuat_terkecil = nama_pembuat[i]

    # mengecek apakah ada lebih dari satu pembuat dengan pembuatan terkecil
    jumlah_terkecil_sama = 0
    for i in range(arr_len(nama_pembuat)):
        if jumlah_pembuatan[i] == jumlah_pembuatan_terkecil:
            jumlah_terkecil_sama += 1

    if jumlah_terkecil_sama > 1:
        nama_pembuat_terkecil = []
        for i in range(len(nama_pembuat)):
            if jumlah_pembuatan[i] == jumlah_pembuatan_terkecil:
                nama_pembuat_terkecil = konso(nama_pembuat_terkecil, nama_pembuat[i])
        pembuat_terkecil = sorting_arr_leks(nama_pembuat_terkecil)[arr_len(nama_pembuat)-1]

    if pembangun == 0:
        pembuat_terbanyak = "-"
        pembuat_terkecil = "-"

    print(f"Total Jin: {pengumpul + pembangun}")
    print(f"Total Jin Pengumpul: {pengumpul}")
    print(f"Total Jin Pembangun: {pembangun}")
    print(f"Jin Terajin: {pembuat_terbanyak}")
    print(f"Jin Termalas: {pembuat_terkecil}")
    print(f"Jumlah Pasir: {bahan_bangunan[1][2]} unit")
    print(f"Jumlah Air: {bahan_bangunan[3][2]} unit")
    print(f"Jumlah Batu: {bahan_bangunan[2][2]} unit")
# def LaporanJin (list_jin,users, candi):
#     J_bangun = 0
#     J_kumpul = 0
#     i = 3
#     pp = arr_len(users)
    
#     for i in range (1,pp):
#         if users[i][2] == "Pengumpul":
#             J_kumpul += 1
#         elif users[i][2] == "Pembangun":
#             J_bangun += 1
        
#         i += 1
        
#     J_total = J_bangun + J_kumpul
    
#     count = {}
#     for i in range(1, len(candi)):
#         if candi[i][1] in count:       #Menghitung Jumlah Kemunculan semua data di kolom kedua dalam list candi, yaitu nama jin
#             count[candi[i][1]] += 1
#         else:
#             count[candi[i][1]] = 1


#     max_count = 0
#     J_rajin = []
#     for g in count:
#         if count[g] > max_count:
#             max_count = count[g]     # Mencari nama jin dengan jumlah kemunculan terbanyak
#             J_rajin = [g]
        
#         elif count[g] == max_count:
#             konso([J_rajin],g)
            
#     if len(J_rajin) > 1:     #syarat jin ter-rajin yang didapat lebih dari satu
#         awal = J_rajin[0]       # menentukan leksiografis terendah dari list jin ter-rajin
#         for item in J_rajin:
#             if item < awal:
#                 awal = item
                
#     min_count = float("inf")        #mencari nama jin dengan jumlah kemunculan terkecil
#     J_malas = []
#     for g in count:
#         if count[g] < min_count:
#             min_count = count[g]
        
#         elif count[g] == min_count:
#             konso([J_malas],g)
            
            
#     if len(J_malas) > 1:        # jika jin termalas yang didapat lebih dari satu
#         awal = J_malas[0]       # menentukan leksiografis tertinggi dari list jin termalas
#         for item in J_malas:
#             if item > awal:
#                 awal = item
            

#     total_pasir = 0
#     total_batu = 0                    #semua bahan-bahan dibikin 0 dulu
#     total_air = 0

#     for row in candi[1:]:
#         total_pasir += int(row[2])
#         total_batu += int(row[3])           #iterasi dari baris kedua hingga akhir dalam candi, dimana tiap data
#         total_air += int(row[4])            #dari kolom tersebut ditambahkan

    
       
        
#     print(f"Total Jin: {J_total} \n")
#     print(f"Total JIn Pengumpul: {J_kumpul} \n")
#     print(f"Total Jin Pembangun: {J_bangun} \n")
#     print(f"Jin Terajin: {J_rajin} \n")
#     print(f"JIn Termalas: {J_malas} \n")        #output
#     print(f"Jumlah Pasir: {total_pasir} \n")
#     print(f"Jumlah Air: {total_air} \n")
#     print(f"Jumlah Batu: {total_batu} \n")
       
            
    
    
