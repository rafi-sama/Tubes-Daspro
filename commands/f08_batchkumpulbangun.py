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
            pasir = b01.generate_angka_random()
            bahan_bangunan[1][2] = str(int(bahan_bangunan[1][2]) + pasir)
            pasir_total += pasir
            
            batu = b01.generate_angka_random()
            bahan_bangunan[2][2] = str(int(bahan_bangunan[2][2]) + batu)
            batu_total += batu
            
            air = b01.generate_angka_random()
            bahan_bangunan[3][2] = str(int(bahan_bangunan[3][2]) + air)
            air_total += air
            
        print(f"Mengerahkan {pengumpul} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan total {pasir_total} pasir, {batu_total} batu, dan {air_total} air.")