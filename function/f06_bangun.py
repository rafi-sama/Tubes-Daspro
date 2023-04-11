from functions import *
import random

def bangun(active_user, candi, bahan_bangunan):

    pasir = random.randint(0,5)
    batu = random.randint(0,5)
    air = random.randint(0,5)

    tempBahan = bahan_bangunan
    tempCandi = candi

    tempBahan[1][2] = str(int(bahan_bangunan[1][2])-pasir)
    tempBahan[2][2] = str(int(bahan_bangunan[2][2])-batu)
    tempBahan[3][2] = str(int(bahan_bangunan[3][2])-air)

    id_candi = arr_len(tempCandi)

    tempCandi = konso(tempCandi, [id_candi, active_user[0], pasir, batu, air])

    candi[:] = tempCandi
    bahan_bangunan[:] = tempBahan
    