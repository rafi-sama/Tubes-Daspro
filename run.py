from functions import *
import commands.f01_login as f01
import commands.f02_logout as f02
import commands.f03_summonjin as f03
import commands.f04_hapusjin as f04
import commands.f05_ubahjin as f05
import commands.f06_bangun as f06
import commands.f07_kumpul as f07
import commands.f08_batchkumpulbangun as f08
import commands.f09_laporanjin as f09
import commands.f10_laporancandi as f10
import commands.f11_hancurkancandi as f11
import commands.f12_ayamberkokok as f12
import commands.f13_load as f13
import commands.f14_save as f14
import commands.f15_help as f15
import commands.f16_exit as f16

def run(command, users, candi, bahan_bangunan, active_user, running_dict):
   
   # Menampilkan list user
   if command == "listuser":
      N = arr_len(users)
      for i in range(1,N):
            print(users[i])
      return 0
   
   # Menampilkan list bahan
   if command == "listbahan":
      N = arr_len(bahan_bangunan)
      for i in range(1,N):
            print(bahan_bangunan[i])
      return 0
   
   # Menampilkan list candi
   if command == "listcandi":
      N = arr_len(candi)
      for i in range(1,N):
            print(candi[i])
      return 0

   # f01 Login
   if command == "login":
      if active_user[0] != 0:     # Jika sudah login, maka tidak bisa login
            print("Login gagal!")
            print(f"Anda telah login dengan username {active_user[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")

      else: # Jika belum login, maka bisa login
            f01.login(users, active_user)
   
   # f02 Logout
   elif command == "logout":
      f02.logout(active_user)
   
   # f03 Summon Jin   
   elif command == "summonjin":
      if active_user[0] == "Bondowoso":
            if arr_len(users) > 103:
               print("Jumlah jin sudah mencapai batas maksimal!")
            else:
               f03.summonjin(users)
      else:
            print("Kamu tidak memiliki akses untuk command summonjin!")
   
   # f04 Hapus Jin
   elif command == "hapusjin":
      if active_user[0] == "Bondowoso":
         f04.hapusjin(active_user, users, candi)
      elif active_user[0] == 0:
         print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
      else:
         print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah hapusjin")
   
   # f05 Ubah Jin
   elif command == "ubahjin":
      if active_user[0] == "Bondowoso":
         f05.ubahjin(users)
      elif active_user[0] == 0:
         print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
      else:
         print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah ubahjin")

   # f06 Bangun
   elif command == "bangun":
      if active_user[1] == "Pembangun":
         f06.bangun(active_user, candi, bahan_bangunan)
      else:
         print(f"Kamu tidak memiliki akses untuk command bangun")

   # f07 Kumpul
   elif command == "kumpul":
      if active_user[1] == "Pengumpul":
         f07.kumpul(bahan_bangunan)
      else:
         print(f"Kamu tidak memiliki akses untuk command bangun")
   
   # f08 Batch Bangun
   elif command == "batchbangun":
      print("command belum tersedia")
   
   # f08 Batch Kumpul
   elif command == "batchkumpul":
      print("command belum tersedia")

   # f09 Laporan Jin
   elif command == "laporanjin":
      f09.LaporanJin(users, candi, bahan_bangunan)

   # f10 Laporan Candi
   elif command == "laporancandi":
      f10.LaporanCandi(candi)

   # f11 Hancurkan Candi
   elif command == "hancurkancandi":
      f11.hancurkan(candi, active_user)
      
   # f12 Ayam Berkokok
   elif command == "ayamberkokok":
      if active_user[0] == "Roro":
         f12.ayamberkokok(candi)
         # running[0] = 0
      elif active_user[0] == 0:
         print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
      else:
         print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah ayamberkokok.")

   # f13 Load
   elif command == "load":
      print("command belum tersedia")

   # f14 Save
   elif command == "save":
      f14.save(users, candi, bahan_bangunan)

   # f15 Help
   elif command == "help":
      f15.help(active_user)

   # f16 Exi
   elif command == "exit":
      f16.exit(users, candi, bahan_bangunan)
      # running[0] = 0

   # Command tidak tersedia
   else:
      print(f"Command \"{command}\" tidak tersedia.")
      print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")



      

