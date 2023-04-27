from functions import *

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

def laporanjin(users, candi, bahan_bangunan, active_user):
    if active_user[1] == "bandung_bondowoso":
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

        if arr_len(nama_pembuat) == 0:
            pembuat_terbanyak = "-"
            pembuat_terkecil = "-"
        # elif pembangun == 1:
        #     pembuat_terbanyak = nama_pembuat[0]
        #     pembuat_terkecil = "-"

            

        print(f"Total Jin: {pengumpul + pembangun}")
        print(f"Total Jin Pengumpul: {pengumpul}")
        print(f"Total Jin Pembangun: {pembangun}")
        print(f"Jin Terajin: {pembuat_terbanyak}")
        print(f"Jin Termalas: {pembuat_terkecil}")
        print(f"Jumlah Pasir: {bahan_bangunan[1][2]} unit")
        print(f"Jumlah Air: {bahan_bangunan[3][2]} unit")
        print(f"Jumlah Batu: {bahan_bangunan[2][2]} unit")
    else:
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    
    return users ,candi, bahan_bangunan