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
        
# def batchbangun(users,candi, bahan_bangunan):
    
# def batchbangun():
#     pasir = random.randint(1, 5)
#     batu = random.randint(1, 5)
#     air = random.randint(1, 5)

#     if (data.bahan_bangunan[1][2] < pasir) or (data.bahan_bangunan[2][2] < batu) or (data.bahan_bangunan[3][2] < air) :
#         print("Bahan bangunan tidak mencukupi. \nCandi tidak bisa dibangun!")

#     else:
#         data.bahan_bangunan[1][2] -= pasir
#         data.bahan_bangunan[2][2] -= batu
#         data.bahan_bangunan[3][2] -= air
#         print("melakukan pembangunan candi.")
#         print(".....\n......")
#         print("Candi berhasil dibangun.")

#         jumlahcandi = funcitons.hitungcandi(data.candi, data.candilength)

#         if jumlahcandi == 100 :
#             print ("Sisa Candi yang perlu dibangun : 0")
#         else: #else jumlah candi < 100
#             Idkosong = -1
#             for i in range (1, data.candilength):
#                 if (data.candi[i][0] == -1):
#                     idkosong = i
#                     break
            
#             if idkosong == -1: #Jika tidak ada slot candi
#                 idkosong = data.candilength
#                 data.candi = functions.appendbuatankita(data.candi, data.candilength, [idkosong, data currentuser, pasir, batu, air])
#                 data.candilength += 1

#                 jumlahcandi = funcitons.hitungcandi(data.candi, data.candilength)
#                 sisa = 100 - jumlahcandi

#             else: #else ada slot candi kosong
#                 data.candi[idkosong] = [idkosong, data.currentuser, pasir, batu, air]

#                 jumlahcandi = functions.hitungcandi(data.candi, data.candilength)
#                 sisa = 100 - jumlahcandi
#             print (f"sisa candi yang perlu dibangun: {sisa}.")