import function.f14_save as f14
def exit(users, candi, bahan_bangunan):
    choice = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)\n")
    while True:
        if choice == "y" or choice == "Y":
            f14.save(users, candi, bahan_bangunan)
            break
        elif choice == "n" or choice == "N":
            print("Keluar dari game tanpa melakukan save.")
            break
        else:
            print("Input (y/n) untuk melakukan save atau tidak.")
            choice = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)\n")
    return False