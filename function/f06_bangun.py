from functions import *
import random

def isCukup(pasir, batu, air, bahan_bangunan):

    if ((pasir > int(bahan_bangunan[1][2])) or (batu > int(bahan_bangunan[2][2])) or (air > int(bahan_bangunan[3][2]))):
        return False
    
    else:
        return True

def bangun(active_user, candi, bahan_bangunan):

    pasir = random.randint(0,5)
    batu = random.randint(0,5)
    air = random.randint(0,5)

    if isCukup(pasir, batu, air, bahan_bangunan):

        tempBahan = bahan_bangunan
        tempCandi = candi

        tempBahan[1][2] = str(int(bahan_bangunan[1][2])-pasir)
        tempBahan[2][2] = str(int(bahan_bangunan[2][2])-batu)
        tempBahan[3][2] = str(int(bahan_bangunan[3][2])-air)

        id_candi = arr_len(tempCandi)

        tempCandi = konso(tempCandi, [id_candi, active_user[0], pasir, batu, air])

        candi[:] = tempCandi
        bahan_bangunan[:] = tempBahan

        sisa = 100-(arr_len(candi)-1)

        print("Candi berhasil dibangun.")
        print(f"Sisa candi yang perlu dibangun: {sisa}.")

    
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    