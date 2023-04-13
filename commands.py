from functions import *
import function.f01_login as f01
import function.f02_logout as f02
import function.f03_summonjin as f03
import function.f04_hapusjin as f04
import function.f05_ubahjin as f05
import function.f06_bangun as f06
import function.f07_kumpul as f07
import function.f08_batchkumpulbangun as f08
import function.f09_laporanjin as f09
import function.f10_laporancandi as f10
import function.f11_hancurkancandi as f11
import function.f12_ayamberkokok as f12
import function.f13_load as f13
import function.f14_save as f14
import function.f15_help as f15
import function.f16_exit as f16

def run(inputan, users, candi, bahan_bangunan, active_user):
   
   # Menampilkan list user
   if inputan == "listuser":
      N = arr_len(users)
      for i in range(1,N):
            print(users[i])
      return 0
   
   # Menampilkan list bahan
   if inputan == "listbahan":
      N = arr_len(bahan_bangunan)
      for i in range(1,N):
            print(bahan_bangunan[i])
      return 0
   
   # Menampilkan list candi
   if inputan == "listcandi":
      N = arr_len(candi)
      for i in range(1,N):
            print(candi[i])
      return 0

   # f01 Login
   if inputan == "login":
      if active_user[0] != 0:     # Jika sudah login, maka tidak bisa login
            print("Login gagal!")
            print(f"Anda telah login dengan username {active_user[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")

      else: # Jika belum login, maka bisa login
            f01.login(users, active_user)
   
   # f02 Logout
   elif inputan == "logout":
      f02.logout(active_user)
   
   # f03 Summon Jin   
   elif inputan == "summonjin":
      if active_user[0] == "Bondowoso":
            if arr_len(users) > 103:
               print("Jumlah jin sudah mencapai batas maksimal!")
            else:
               f03.summonjin(users)
      else:
            print("Kamu tidak memiliki akses untuk command summonjin!")
   
   # f04 Hapus Jin
   elif inputan == "hapusjin":
      if active_user[0] == "Bondowoso":
         f04.hapusjin(active_user, users, candi)
      elif active_user[0] == 0:
         print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
      else:
         print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah hapusjin")
   
   # f05 Ubah Jin
   elif inputan == "ubahjin":
      if active_user[0] == "Bondowoso":
         f05.ubahjin(users)
      elif active_user[0] == 0:
         print("Silahkan login dahulu sebelum menggunakan perintah tersebut!")
      else:
         print(f"User dengan username {active_user[0]} tidak memiliki akses terhadap perintah ubahjin")

   # f06 Bangun
   elif inputan == "bangun":
      if active_user[1] == "Pembangun":
         f06.bangun(active_user, candi, bahan_bangunan)
      else:
         print(f"Kamu tidak memiliki akses untuk command bangun")

   # f07 Kumpul
   elif inputan == "kumpul":
      print("command belum tersedia")
   
   # f08 Batch Bangun
   elif inputan == "batchbangun":
      print("command belum tersedia")
   
   # f08 Batch Kumpul
   elif inputan == "batchkumpul":
      print("command belum tersedia")

   # f09 Laporan Jin
   elif inputan == "laporanjin":
      print("command belum tersedia")

   # f10 Laporan Candi
   elif inputan == "laporancandi":
      print("command belum tersedia")

   # f11 Hancurkan Candi
   elif inputan == "hancurkancandi":
      f11.hancurkan(candi, active_user)
      
   # f12 Ayam Berkokok
   elif inputan == "ayamberkokok":
      print("command belum tersedia")

   # f13 Load
   elif inputan == "load":
      print("command belum tersedia")

   # f14 Save
   elif inputan == "save":
      f14.save(users, candi, bahan_bangunan)

   # f15 Help
   elif inputan == "help":
      f15.help(active_user)

   # f16 Exi
   elif inputan == "exit":
      f16.exit(users, candi, bahan_bangunan)

   # Command tidak tersedia
   else:
      print(f"Command \"{inputan}\" tidak tersedia.")
      print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")



      

