from functions import *

def run(inputan, users, candi, bahan_bangunan, role):

    if inputan == "help":
        help(role)

    elif inputan == "login":

        if role[0] != 0:     # Jika sudah login, maka tidak bisa login
            print("Login gagal!")
            print(f"Anda telah login dengan username {role[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")

        else: # Jika belum login, maka bisa login
            login(users, role)

    elif inputan == "logout":
        logout(role)
    
    elif inputan == "summonjin":

        if role[0] == "Bondowoso":
            if len_count(users) > 103:
                print("Jumlah jin sudah mencapai batas maksimal!")
            
            else:
                summonjin(users)
        else:
            print("Kamu tidak memiliki akses untuk command summonjin!")
            

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

        print(f"\nSelamat datang, {username}!")
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")

        role[0] = username #buat username di indeks 0
        role[1] = user[lokasi][2] #password username di indeks 1/di sebelah kanan username

    elif username_checker and password != user[lokasi][1]:  # Jika username benar tapi password salah, maka tampilkan bahwa password salah
        print("\nPassword salah!")
    else: # Jika username tidak terdaftar, maka tampilkan pesannya
        print("\nUsername tidak terdaftar!")
        
def logout(role):
    if role[0] != 0:            # Jika sudah login, maka bisa logout
        print(f"Keluar dari akun dengan username {role[0]}")
        role[0] = 0
    else:
        print("Logout gagal!")  # Jika belum login, maka tidak bisa logout
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout.")

def summonjin(users):

    # variabel 'users' berisi data:

    # kolom ke-
    # 0 : username | 1 : password | 2 : role
    # baris ke-
    # 0 : judul kolom | 1 : data bondowoso | 2 : data roro | 3 dst : data jin

    N = len_count(users)

    # membuat array yang berisi nama jin
    # in range(3, N-2) karena data jin pertama kali ada pada baris ke 3
    nama_jin = [users[i][0] for i in range(3, N-2)]
    
    jenis_jin = ["Pengumpul", "Pembangun"] # dengan nomor 0, 1
    nomor_jin = ["1", "2"]

    print("Jenis jin yang dapat dipanggil:")
    print("  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("  (2) Pembangun - Bertugas membangun candi")


    # INPUT NOMOR JIN

    nomor_jin_input = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ") 

    # validasi agar inputan nomor jin sesuai
    while (nomor_jin_input not in nomor_jin):
        
        print(f"\nTidak ada jenis jin bernomor \"{nomor_jin_input}\"!")
        nomor_jin_input = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ") 
    
    print(f"\nMemilih jin \"{jenis_jin[int(nomor_jin_input)-1]}\"")


    # INPUT NAMA JIN

    nama_jin_input = input("\nMasukkan username jin: ")
    
    # validasi agar nama jin tidak ada yang sama
    while (nama_jin_input in nama_jin):
        
        print(f"Username \"{nama_jin_input}\" sudah diambil!")
        nama_jin_input = input("\nMasukkan username jin: ")


    # INPUT PASSWORD JIN

    password_jin_input = input("Masukkan password jin: ")

    N = len_count(password_jin_input)
    
    # validasi agar password sesuai ketentuan
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

def help(role):
    
    if role[1] == 0:
        print("Menu help belum login")
    
    elif role[1] == "bandung_bondowoso":
        print("Menu help bandung bondowoso")

    elif role[1] == "roro_jonggrang":
        print("Menu help roro jonggrang")

    elif role[1] == "Pengumpul":
        print("Menu help jin pengumpul")

    else: # role[1] == "Pembangun"
        print("Menu help jin pembangun")



