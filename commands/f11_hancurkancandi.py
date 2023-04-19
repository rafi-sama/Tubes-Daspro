from functions import *

def hancurkan(candi, active_user):
   
   if active_user[1] == "roro_jonggrang":
   
        id = input("Masukkan ID candi: ")
            
        ada_candi = False
        
        for i in range(1, arr_len(candi)):
            if candi[i][0] == id:
                
                ada_candi = True
                indeks = i
                
        if ada_candi:
            
            confirm = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)?")
            while confirm != "Y" or confirm != "N":
                confirm = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)?")

            if confirm == "Y":
                tempArr = [[0 for i in range(2)] for j in range(arr_len(candi)-1)]
                    
                for i in range(arr_len(candi)):
                    if i < indeks:
                        tempArr[i] = candi[i]
                            
                    elif i > indeks:
                        tempArr[i-1] = candi[i]
                            
                candi[:] = tempArr
                
            else:
                print(f"Batal menghancurkan candi ID: {id}")
            
        else:
            print("Tidak ada candi dengan ID tersebut")
    
   else:
        print("Tidak memmiliki akses untuk command \"hancurkancandi\"")