import os
def save(users, candi, bahan_bangunan):
    folder = input("Masukkan nama folder: ")
    savefiles_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "savefiles")
    if not os.path.exists(savefiles_dir):
        os.makedirs(savefiles_dir)
        print("Saving...")
        new_dir_path = os.path.join(savefiles_dir, folder)
        if not os.path.exists(new_dir_path):
            print(f"Membuat folder save\{folder}...")
            os.makedirs(new_dir_path)
            with open(fr"{new_dir_path}\user.csv", 'w') as file_users:
                users_str = '\n'.join(str(user) for user in users)
                users = file_users.write(users_str + '\n')
            with open(fr"{new_dir_path}\candi.csv", 'w') as file_users:
                candi_str = '\n'.join(str(temple) for temple in candi)
                candi = file_users.write(candi_str + '\n')
            with open(fr"{new_dir_path}\bahan_bangunan.csv", 'w') as file_users:
                bahan_bangunan_str = '\n'.join(str(bahan) for bahan in bahan_bangunan)
                bahan_bangunan = file_users.write(bahan_bangunan_str + '\n')
            print(f"Berhasil menyimpan data di folder save\{folder}")
        else:
            new_dir_path = os.path.join(savefiles_dir, folder)
            print("Saving...")
            with open(fr"{new_dir_path}\user.csv", 'w') as file_users:
                users_str = '\n'.join(str(user) for user in users)
                users = file_users.write(users_str + '\n')
            with open(fr"{new_dir_path}\candi.csv", 'w') as file_users:
                candi_str = '\n'.join(str(temple) for temple in candi)
                candi = file_users.write(candi_str + '\n')
            with open(fr"{new_dir_path}\bahan_bangunan.csv", 'w') as file_users:
                bahan_bangunan_str = '\n'.join(str(bahan) for bahan in bahan_bangunan)
                bahan_bangunan = file_users.write(bahan_bangunan_str + '\n')
            print(f"Berhasil menyimpan data di folder save\{folder}")
    else:
        new_dir_path = os.path.join(savefiles_dir, folder)
        if not os.path.exists(new_dir_path):
            os.makedirs(new_dir_path)
            print("Saving...")
            print(f"Membuat folder {folder}")
            with open(fr"{new_dir_path}\user.csv", 'w') as file_users:
                users_str = '\n'.join(str(user) for user in users)
                users = file_users.write(users_str + '\n')
            with open(fr"{new_dir_path}\candi.csv", 'w') as file_users:
                candi_str = '\n'.join(str(temple) for temple in candi)
                candi = file_users.write(candi_str + '\n')
            with open(fr"{new_dir_path}\bahan_bangunan.csv", 'w') as file_users:
                bahan_bangunan_str = '\n'.join(str(bahan) for bahan in bahan_bangunan)
                bahan_bangunan = file_users.write(bahan_bangunan_str + '\n')
            print(f"Berhasil menyimpan data di folder save\{folder}")
        else:
            new_dir_path = os.path.join(savefiles_dir, folder)
            print("Saving...")
            with open(fr"{new_dir_path}\user.csv", 'w') as file_users:
                users_str = '\n'.join(str(user) for user in users)
                users = file_users.write(users_str + '\n')
            with open(fr"{new_dir_path}\candi.csv", 'w') as file_users:
                candi_str = '\n'.join(str(temple) for temple in candi)
                candi = file_users.write(candi_str + '\n')
            with open(fr"{new_dir_path}\bahan_bangunan.csv", 'w') as file_users:
                bahan_bangunan_str = '\n'.join(str(bahan) for bahan in bahan_bangunan)
                bahan_bangunan = file_users.write(bahan_bangunan_str + '\n')
            print(f"Berhasil menyimpan data di folder save\{folder}")