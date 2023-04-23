from commands.f06_bangun import *
import commands.b01_randomgenerator as b01
from functions import *

def batchkumpul(users,candi, bahan_bangunan, active_user):

    if active_user[1] == "bandung_bondowoso":
    
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
    
    elif active_user[1] == 0:
        print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
    
    else:
        print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah batchbangun.")
        
    return users, candi, bahan_bangunan
        
def batchbangun(users,candi, bahan_bangunan, active_user):

    if active_user[1] == "bandung_bondowoso":

        pembangun = 0
        list_jin = []
        for i in range (arr_len(users)):
            if users[i][2] == "Pembangun":
                pembangun += 1
                list_jin = konso(list_jin, users[i])
        
        bahan = [bahan_bangunan[i] for i in range(arr_len(bahan_bangunan))]
        bahan_baru = [bahan_bangunan[i] for i in range(arr_len(bahan_bangunan))]
        candi_baru = [candi[i] for i in range(arr_len(candi))]
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
                        candi_baru = konso(candi_baru, [str(id_candi), str(list_jin[j][0]), str(pasir), str(batu), str(air)])
                        candi_baru = sortCandi(candi_baru)
                    bahan = bahan_baru
                else:
                    bahan = bahan
                    gagal += 1

            if gagal != 0:
                if pasir_total - int(bahan[1][2]) < 0:
                    pasir_sisa = 0
                else:
                    pasir_sisa = pasir_total - int(bahan[1][2])
                if batu_total - int(bahan[2][2]) < 0:
                    batu_sisa = 0
                else:
                    batu_sisa = batu_total - int(bahan[2][2])
                if air_total - int(bahan[3][2]) < 0:
                    air_sisa = 0
                else:
                    air_sisa = air_total - int(bahan[3][2])
                print(f"Mengerahkan {pembangun} jin untuk membangun candi dengan total bahan {pasir_total} pasir, {batu_total} batu, dan {air_total} air.")
                print(f"Bangun gagal. Kurang {pasir_sisa} pasir, {batu_sisa} batu, dan {air_sisa} air.")
                return users, candi_baru, bahan
            else:
                bahan[1][2] = int(bahan[1][2]) - pasir_total
                bahan[2][2] = int(bahan[2][2]) - batu_total
                bahan[3][2] = int(bahan[3][2]) - air_total
                print(f"Mengerahkan {pembangun} jin untuk membangun candi dengan total bahan {pasir_total} pasir, {batu_total} batu, dan {air_total} air.")
                print(f"Jin berhasil membangun total {total_candi} candi.")
                return users, candi_baru, bahan_baru
            
    elif active_user[1] == 0:
        print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
    
    else:
        print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah batchbangun.")
        
    return users, candi, bahan_bangunan