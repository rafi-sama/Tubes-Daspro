from functions import *
import commands.b01_randomgenerator as b01

def sortCandi(arr):

    for i in range(1, arr_len(arr)):
        for j in range(i, arr_len(arr)):
            if int(arr[i][0]) > int(arr[j][0]):
                arr[i], arr[j] = arr[j], arr[i]

    return arr

def isCukup(pasir, batu, air, bahan_bangunan):

    if ((pasir > int(bahan_bangunan[1][2]))\
         or (batu > int(bahan_bangunan[2][2]))\
              or (air > int(bahan_bangunan[3][2]))):
        return False
    
    else:
        return True

def bangun(users, candi, bahan_bangunan, active_user):

    pasir = b01.generate_angka_random()
    batu = b01.generate_angka_random()
    air = b01.generate_angka_random()

    if isCukup(pasir, batu, air, bahan_bangunan):

        bahan_bangunan[1][2] = str(int(bahan_bangunan[1][2])-pasir)
        bahan_bangunan[2][2] = str(int(bahan_bangunan[2][2])-batu)
        bahan_bangunan[3][2] = str(int(bahan_bangunan[3][2])-air)

        id_candi = 0 

        for i in range(1,arr_len(candi)):
            if id_candi + 1 == int(candi[i][0]):
                id_candi +=1
            else:
                break
        id_candi += 1

        if arr_len(candi) < 101:
            candi = konso(candi, [str(id_candi), active_user[0], str(pasir), str(batu), str(air)])
            candi = sortCandi(candi)

        sisa = 100-(arr_len(candi)-1)

        print("Candi berhasil dibangun.")
        print(f"Sisa candi yang perlu dibangun: {sisa}.")

    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    
    return users, candi, bahan_bangunan
    