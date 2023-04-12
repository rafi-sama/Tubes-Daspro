from functions import *
def hapusjin(list_jin):
    username_jin = input("Masukkan username jin: ")
    list_jin_baru = []
    for i in range (arr_len(list_jin)):
        if username_jin != list_jin[i]:
            konso(list_jin_baru, username_jin)
    
    if arr_len(list_jin) == arr_len(list_jin_baru):
        print("Tidak ada jin dengan username tersebut.")
        return list_jin
    else:
        determine = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
        while True:
            if determine == "y":
                print("Jin telah berhasil dihapus dari alam gaib.")
                return list_jin_baru
                break
            elif determine == "n":
                print("Jin tidak jadi dihapus dari alam gaib.")
                return list_jin
                break
            else:
                print(f"Hanya menerima input y/n. Silahkan ulangi.")
                determine = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
                