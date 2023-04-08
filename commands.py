from functions import *

def run(inputan, users, candi, bahan_bangunan, role):

    if inputan == "login" and role[0] != 0:     # Jika sudah login, maka tidak bisa login
        print("Login gagal!")
        print(f"Anda telah login dengan username {role[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")

    elif inputan == "login" and role[0] == 0:   # Jika belum login, maka bisa login
        login(users, role)

    elif inputan == "logout":
        logout(role)
    
    elif inputan == "summonjin":
        summonjin(users)

def login(user, role):

    # Masukkan username dan password
    username = input("Username: ")
    password = input("Password: ")

    # N = 0       # N untuk mencari panjang array
    username_checker = False    # Untuk mengecek apakah username sudah terdaftar atau belum
    # for elem in user:           # Menghitung panjang array dari file user.csv
    #     N += 1

    N = len_count(user)
    
    for i in range (1, N):       # Mencari apakah username ada pada file user.csv
        if username == user[i][0]:      # Jika username ditemukan, maka ubah checker ke True pertanda username ditemukan. dan tandai lokasi username pada array
            username_checker = True
            lokasi = i
    if username_checker and password == user[lokasi][1]: #Jika username dan password sesuai, maka login berhasil dan ubah role menjadi username untuk menandai bahwa saat ini dalam posisi sudah login

        print(f"Selamat datang, {username}!")
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")

        role[0] = username

        active_user = role[0]

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


def summonjin(users):

    N = len_count(users)

    nama_jin = [users[i][0] for i in range(3, N-2)]
    
    jenis_jin = ["Pengumpul", "Pembangun"] # dengan nomor 0, 1
    nomor_jin = ["1", "2"]

    print("Jenis jin yang dapat dipanggil:")
    print("  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("  (2) Pembangun - Bertugas membangun candi")


    # Input nomor jin

    nomor_jin_input = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ") 

    while (nomor_jin_input not in nomor_jin):
        
        print(f"\nTidak ada jenis jin bernomor \"{nomor_jin_input}\"!")
        nomor_jin_input = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ") 
    
    print(f"\nMemilih jin \"{jenis_jin[int(nomor_jin_input)-1]}\"")


    # Input nama jin

    nama_jin_input = input("\nMasukkan username jin: ")
    
    while (nama_jin_input in nama_jin):
        
        print(f"Username \"{nama_jin_input}\" sudah diambil!")
        nama_jin_input = input("\nMasukkan username jin: ")


    # Input password jin

    password_jin_input = input("Masukkan password jin: ")

    N = len_count(password_jin_input)
    
    while (N < 5 or N > 25):
        
        print("\nPassword panjangnya harus 5-25 karakter!")

        password_jin_input = input("Masukkan password jin: ")

        N = len_count(password_jin_input)
        
    # Mengappend data baru jin ke users (tanpa .append())

    N = len_count(users)

    temp_users = [0 for i in range(N+1)]

    for i in range(N):
        temp_users[i] = users[i]

    temp_users[N] = [nama_jin_input, password_jin_input, jenis_jin[int(nomor_jin_input)-1]]

    users[:] = temp_users


    

