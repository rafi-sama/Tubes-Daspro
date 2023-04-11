from functions import *
def summonjin(users):
    # variabel 'users' berisi data:

    # kolom ke-
    # 0 : username | 1 : password | 2 : role
    # baris ke-
    # 0 : judul kolom | 1 : data bondowoso | 2 : data roro | 3 dst : data jin

    N = arr_len(users)

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
    i = 0
    while i < N:
        if users[i][0] == nama_jin_input:
            print(f"Username {nama_jin_input} sudah diambil!")
            nama_jin_input = input("\nMasukkan username jin: ")
        else:
            i += 1
            
    # while (nama_jin_input in nama_jin):
    #     print(f"Username \"{nama_jin_input}\" sudah diambil!")
    #     nama_jin_input = input("\nMasukkan username jin: ")


    # INPUT PASSWORD JIN

    password_jin_input = input("Masukkan password jin: ")

    M = str_len(password_jin_input)
    
    # validasi agar password sesuai ketentuan
    while (M < 5 or M > 25):
        
        print("\nPassword panjangnya harus 5-25 karakter!")

        password_jin_input = input("Masukkan password jin: ")

        M = str_len(password_jin_input)
        
    new_user = f"{nama_jin_input};{password_jin_input};{jenis_jin[int(nomor_jin_input)-1]}"
    with open(r"file\user.csv", 'a') as file_users:
        users = file_users.write('\n' + new_user)
        print("Data successfully added!")
    return users