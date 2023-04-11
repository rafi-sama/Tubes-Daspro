from functions import *

def login(user, active_user):
    # Masukkan username dan password
    username = input("Username: ")
    password = input("Password: ")

    # N = 0       # N untuk mencari panjang array
    username_checker = False    # Untuk mengecek apakah username sudah terdaftar atau belum
    # for elem in user:           # Menghitung panjang array dari file user.csv
    #     N += 1

    N = arr_len(user)
    
    for i in range (1, N):       # Mencari apakah username ada pada file user.csv
        if username == user[i][0]:      # Jika username ditemukan, maka ubah checker ke True pertanda username ditemukan. dan tandai lokasi username pada array
                username_checker = True
                lokasi = i
    if username_checker and password == user[lokasi][1]: #Jika username dan password sesuai, maka login berhasil dan ubah role menjadi username untuk menandai bahwa saat ini dalam posisi sudah login

        print(f"\nSelamat datang, {username}!")
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")

        active_user[0] = username #buat username di indeks 0
        active_user[1] = user[lokasi][2] #password username di indeks 1/di sebelah kanan username

    elif username_checker and password != user[lokasi][1]:  # Jika username benar tapi password salah, maka tampilkan bahwa password salah
        print("\nPassword salah!")
    else: # Jika username tidak terdaftar, maka tampilkan pesannya
        print("\nUsername tidak terdaftar!")