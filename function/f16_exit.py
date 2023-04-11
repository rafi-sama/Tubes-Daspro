def exit():
    choice = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)\n")
    while True:
        if choice == "y":
            save()
            print("Save sukses, sampai jumpa!")
            break
        elif choice == "n":
            print("Keluar dari game tanpa melakukan save.")
            break
        else:
            print("Input (y/n) untuk melakukan save atau tidak.")
            choice = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)\n")
    return False