import time

# Tentukan nilai awal (seed) dan konstanta LCG
seed = int(time.time())
a = 1103515245
c = 12345
m = 2**31

# Fungsi untuk menghasilkan angka acak antara 0 dan 5
def generate_angka_random():
    global seed
    seed = (a*seed + c) % m
    return seed % 6