def run(inputan,users,candi,bahan_bangunan,role):
    if inputan == "login" and role[0] != 0:     # Jika sudah login, maka tidak bisa login
        print("Login gagal!")
        print(f"Anda telah login dengan username {role[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")
    elif inputan == "login" and role[0] == 0:   # Jika belum login, maka bisa login
        login(users,role)
    elif inputan == "logout":
        logout(role)

def login(user,role):
    # Masukkan username dan password
    username = input("Username: ")
    password = input("Password: ")
    N = 0       # N untuk mencari panjang array
    username_checker = False    # Untuk mengecek apakah username sudah terdaftar atau belum
    for elem in user:           # Menghitung panjang array dari file user.csv
        N += 1
    for i in range (1,N):       # Mencari apakah username ada pada file user.csv
        if username == user[i][0]:      # Jika username ditemukan, maka ubah checker ke True pertanda username ditemukan. dan tandai lokasi username pada array
            username_checker = True
            lokasi = i
    if username_checker and password == user[lokasi][1]: #Jika username dan password sesuai, maka login berhasil dan ubah role menjadi username untuk menandai bahwa saat ini dalam posisi sudah login
        print(f"Selamat datang, {username}!")
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        role[0] = username

    elif username_checker and password != user[lokasi][1]:  # Jika username benar tapi password salah, maka tampilkan bahwa password salah
        print("Password salah!")
    else: # Jika username tidak terdaftar, maka tampilkan pesannya
        print("Username tidak terdaftar!")
        
def logout(role):
    if role[0] != 0:            # Jika sudah login, maka bisa logout
        print(f"Keluar dari akun dengan username {role[0]}")
        role[0] = 0
    else:
        print("Logout gagal!")  # Jika belum login, maka tidak bisa logout
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout.")