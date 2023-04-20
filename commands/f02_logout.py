def logout(users, candi, bahan_bangunan, active_user):
    
    if active_user[0] != 0:            # Jika sudah login, maka bisa logout

        print(f"Keluar dari akun dengan username {active_user[0]}")

        active_user[0] = 0
        active_user[1] = 0

    else:
        print("Logout gagal!")  # Jika belum login, maka tidak bisa logout
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout.")
    
    return users, candi, bahan_bangunan