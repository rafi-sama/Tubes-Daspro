from functions import *
def ubahjin(list_jin) :
    username_jin = input("Masukkan username jin: ")
    found = False
    N = arr_len(list_jin)

    for i in range (N) :
        if username_jin == list_jin[i][0] :
            lokasi = i
            found = True

    if found == False :
        print ("Tidak ada jin dengan username tersebut.")
    else :
        if list_jin[lokasi][2] == "Pengumpul" :
            determine = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
            while True :
                if determine == "Y" or determine == "y" :
                    list_jin[lokasi][2] = "Pembangun"
                    list_jin[:] = list_jin
                    print("Jin telah berhasil diubah.")
                    break
                elif determine == "N" or determine == "n" :
                    print("Jin tidak jadi diubah.")
                    list_jin[:] = list_jin
                    break
                else :
                    print(f"Hanya menerima input y/n. Silahkan ulangi.")
                    determine = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
        else :
            determine = input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
            while True :
                if determine == "Y" or determine == "y" :
                    list_jin[lokasi][2] = "Pengumpul"
                    list_jin[:] = list_jin
                    print("Jin telah berhasil diubah.")
                    break
                elif determine == "N" or determine == "n" :
                    print("Jin tidak jadi diubah.")
                    list_jin[:] = list_jin
                    break
                else :
                    print(f"Hanya menerima input y/n. Silahkan ulangi.")
                    determine = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")

