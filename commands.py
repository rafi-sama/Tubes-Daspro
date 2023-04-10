from functions import *

def run(inputan, users, candi, bahan_bangunan, active_user):

   # fungi sementara buat liat list user (ntar dihapus)
   if inputan == "listuser":
      N = len_count(users)

      for i in range(1,N):
            print(users[i])

   if inputan == "help":
      help(active_user)

   elif inputan == "login":

      if active_user[0] != 0:     # Jika sudah login, maka tidak bisa login
            print("Login gagal!")
            print(f"Anda telah login dengan username {active_user[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")

      else: # Jika belum login, maka bisa login
            login(users, active_user)

   elif inputan == "logout":
      logout(active_user)
   
   elif inputan == "summonjin":

      if active_user[0] == "Bondowoso":
            if len_count(users) > 103:
               print("Jumlah jin sudah mencapai batas maksimal!")
            
            else:
               summonjin(users)
      else:
            print("Kamu tidak memiliki akses untuk command summonjin!")
            

def login(user, active_user):

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

      active_user[0] = username #buat username di indeks 0
      active_user[1] = user[lokasi][2] #password username di indeks 1/di sebelah kanan username

   elif username_checker and password != user[lokasi][1]:  # Jika username benar tapi password salah, maka tampilkan bahwa password salah
      print("\nPassword salah!")
   else: # Jika username tidak terdaftar, maka tampilkan pesannya
      print("\nUsername tidak terdaftar!")
      
def logout(active_user):
   if active_user[0] != 0:            # Jika sudah login, maka bisa logout
      print(f"Keluar dari akun dengan username {active_user[0]}")
      active_user[0] = 0
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


   # INPUT NOMOR JIN (untuk tipe jin/role jin)

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

def save():
   print("Ini buat save")

def help(active_user):
   
   if active_user[1] == 0:
      print('''=========== HELP ===========
1. login
   Untuk masuk menggunakan akun
2. load
   Untuk memuat file eksternal ke dalam permainan
3. exit
   Untuk keluar dari permainan
4. help
   Untuk menampilkan command yang dapat dipanggil
============================''')
   
   elif active_user[1] == "bandung_bondowoso":
      print('''=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. summonjin
   Untuk memanggil jin dari dunia lain
3. hapusjin
   Untuk menghapus jin yang telah dipanggil
4. ubahjin
   Untuk mengubah tipe jin yang telah dipanggil
5. batchkumpul
   Untuk mengerahkan seluruh pasukan jin pengumpul
6. batchbangun
   Untuk mengerahkan seluruh pasukan jin pengumpul
7. laporanjin
   Untuk mengambil laporan kinerja jin
8. laporancandi
   Untuk mengambil laporan progress pembangunan candi
9. exit
   Untuk keluar dari permainan
10. help
   Untuk menampilkan command yang dapat dipanggil
============================''')

   elif active_user[1] == "roro_jonggrang":
      print('''=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. hancurkancandi
   Untuk menghancurkan candi
3. ayamberkokok
   Untuk memalsukan ayam berkokok di pagi hari
4. exit
   Untuk keluar dari permainan
5. help
   Untuk menampilkan command yang dapat dipanggil
============================''')

   elif active_user[1] == "Pengumpul":
      print('''=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. kumpul
   Untuk mengumpulkan bahan-bahan yang diperlukan untuk membangun candi
3. exit
   Untuk keluar dari permainan
4. help
   Untuk menampilkan command yang dapat dipanggil
============================''')

   else: # role[1] == "Pembangun"
      print('''=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. bangun
   Untuk membangun candi
3. exit
   Untuk keluar dari permainan
4. help
   Untuk menampilkan command yang dapat dipanggil
============================''')
      
def exit():
   choice = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)\n")
   if choice == y:
      save()
      print("Save sukses, sampai jumpa!")
      break
   elif choice == n:
      print("Keluar dari game tanpa melakukan save.")
      break
   else:
      print("Input (y/n) untuk melakukan save atau tidak.")