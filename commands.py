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
   # fungi sementara buat liat list user (ntar dihapus)
   if inputan == "listuser":
      N = arr_len(users)

      for i in range(1,N):
            print(users[i])
      
   if inputan == "listbahan":
      N = arr_len(bahan_bangunan)
      for i in range(1,N):
            print(bahan_bangunan[i])
      
   if inputan == "listcandi":
      N = arr_len(candi)
      for i in range(1,N):
            print(candi[i])

   if inputan == "help":
      f15.help(active_user)

   elif inputan == "login":

      if active_user[0] != 0:     # Jika sudah login, maka tidak bisa login
            print("Login gagal!")
            print(f"Anda telah login dengan username {active_user[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")

      else: # Jika belum login, maka bisa login
            f01.login(users, active_user)

   elif inputan == "logout":
      f02.logout(active_user)
   
   elif inputan == "summonjin":
      if active_user[0] == "Bondowoso":
            if arr_len(users) > 103:
               print("Jumlah jin sudah mencapai batas maksimal!")
            else:
               f03.summonjin(users)
      else:
            print("Kamu tidak memiliki akses untuk command summonjin!")
            
   elif inputan == "save":
      f14.save()
      
   elif inputan == "exit":
      f16.exit()

   elif inputan == "bangun":
      f06.bangun(active_user, candi, bahan_bangunan)