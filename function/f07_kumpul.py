import function.b01_randomgenerator as b01

def kumpul(bahan): #Fungsi mengumpulkan bahan bangunan
    global bahan_bangunan #mengambil list bahan bangunan dari program utama
    pasir = b01.generate_angka_random() #mengambil secara random jumlah pasir
    batu = b01.generate_angka_random() #mengambil secara random jumlah batu
    air = b01.generate_angka_random() #mengambil secara random jumlah air
    bahan[1][2] = str(int(bahan[1][2]) + pasir) #menambahkan pasir yang diambil ke list bahan bangunan
    bahan[2][2] = str(int(bahan[2][2]) + batu) #menambahkan batu yang diambil ke list bahan bangunan
    bahan[3][2] = str(int(bahan[3][2]) + air) #menambahkan air yang diambil ke list bahan bangunan
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.") #tampilan pada layar jumlah pasir, batu, dan air yang diambil

