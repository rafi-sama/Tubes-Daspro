from commands.f06_bangun import *
import commands.b01_randomgenerator as b01
from functions import *
def batchkumpul(users, bahan_bangunan):
    pengumpul = 0
    for i in range (arr_len(users)):
        if users[i][2] == "Pengumpul":
            pengumpul += 1
    
    pasir_total = 0
    batu_total = 0
    air_total = 0
    if pengumpul == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        for i in range (pengumpul):
            pasir = b01.generate_angka_random(0)
            bahan_bangunan[1][2] = str(int(bahan_bangunan[1][2]) + pasir)
            pasir_total += pasir
            
            batu = b01.generate_angka_random(0)
            bahan_bangunan[2][2] = str(int(bahan_bangunan[2][2]) + batu)
            batu_total += batu
            
            air = b01.generate_angka_random(0)
            bahan_bangunan[3][2] = str(int(bahan_bangunan[3][2]) + air)
            air_total += air
            
        print(f"Mengerahkan {pengumpul} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan total {pasir_total} pasir, {batu_total} batu, dan {air_total} air.")
        
def batchbangun(users,candi, bahan_bangunan, active_user):
    pembangun = 0
    list_jin = []
    for i in range (arr_len(users)):
        if users[i][2] == "Pembangun":
            pembangun += 1
            list_jin = konso(list_jin, users[i])
    
    bahan_baru = bahan_bangunan
    candi_baru = candi
    pasir_total = 0
    batu_total = 0
    air_total = 0
    pasir_sisa = 0
    batu_sisa = 0
    air_sisa = 0
    gagal = 0
    total_candi = 0
    if pembangun == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        for j in range (pembangun):
            pasir = b01.generate_angka_random(1)
            batu = b01.generate_angka_random(1)
            air = b01.generate_angka_random(1)
            pasir_total += pasir
            batu_total += batu
            air_total += air
            if isCukup(pasir, batu, air, bahan_baru):

                bahan_baru[1][2] = str(int(bahan_baru[1][2])-pasir)
                bahan_baru[2][2] = str(int(bahan_baru[2][2])-batu)
                bahan_baru[3][2] = str(int(bahan_baru[3][2])-air)

                id_candi = 0 

                for i in range(1,arr_len(candi_baru)):
                    if id_candi + 1 == int(candi_baru[i][0]):
                        id_candi +=1
                    else:
                        break
                id_candi += 1
                total_candi += 1

                if arr_len(candi_baru) < 101:
                    candi_baru = konso(candi_baru, [str(id_candi), str(list_jin[j][1]), str(pasir), str(batu), str(air)])
                    candi_baru = sortCandi(candi_baru)

            else:
                gagal += 1
                break

        if gagal != 0:
            if pasir_total - int(bahan_baru[1][2]) < 0:
                pasir_sisa = 0
            else:
                pasir_sisa = pasir_total - int(bahan_baru[1][2])
            if batu_total - int(bahan_baru[2][2]) < 0:
                batu_sisa = 0
            else:
                batu_sisa = batu_total - int(bahan_baru[2][2])
            if air_total - int(bahan_baru[3][2]) < 0:
                air_sisa = 0
            else:
                air_sisa = air_total - int(bahan_baru[3][2])
            print(f"Mengerahkan {pembangun} jin untuk membangun candi dengan total bahan {pasir_total} pasir, {batu_total} batu, dan {air_total} air.")
            print(f"Bangun gagal. Kurang {pasir_sisa} pasir, {batu_sisa} batu, dan {air_sisa} air.")
        else:
            print(f"Mengerahkan {pembangun} jin untuk membangun candi dengan total bahan {pasir_total} pasir, {batu_total} batu, dan {air_total} air.")
            print(f"Jin berhasil membangun total {total_candi} candi.")
            bahan_bangunan[:] = bahan_baru
            candi[:] = candi_baru