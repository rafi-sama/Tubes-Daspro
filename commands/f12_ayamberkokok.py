from functions import *

def ayamberkokok(users, candi, bahan_bangunan, active_user, running):

    if active_user[1] == "roro_jonggrang":
        
        N = arr_len(candi)-1
        if N < 100:
            print("Kukuruyuk.. Kukuruyuk.. \n")
            print(f"Jumlah candi: {N} \n")
            print("Selamat, Roro Jonggrang memenangkan permainan! \n")
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")
        else:
            print("Kukuruyuk.. Kukuruyuk.. \n")
            print(f"Jumlah candi: {N} \n")
            print("Yah, Bandung Bondowoso memenangkan permainan!")

        running[0] = 0

    elif active_user[0] == 0:
        print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
    else:
        print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah ayamberkokok.")
    
    return users, candi, bahan_bangunan
