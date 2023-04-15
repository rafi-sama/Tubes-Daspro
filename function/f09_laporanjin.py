from functions import *
import random
def LaporanJin (list_jin,users, bahan_bangunan):
    J_total = arr_len[list_jin]
    J_kumpul = users
    a = bahan_bangunan
    
    print(f"Total Jin: {J_total} \n")
    print(f"Total JIn Pengumpul: {J_kumpul} \n")
    print(f"Total Jin Pembangun: {J_total-J_kumpul} \n")
    
    
LaporanJin()