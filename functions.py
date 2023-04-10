def len_count(x):

    N = 0

    # untuk setiap elemen pada X, nilai N bertambah 1
    for i in x:
        N += 1
    
    return N

def split(data, separator):

    # variabel yang menyatakan banyaknya pemisah (ex: titik koma pada file .csv)
    NSeparator = 0 

    # banyaknya karakter pada string yang ingin di split
    len = len_count(data) 

    # menghitung banyaknya separator
    for i in range(len): 
        if data[i] == separator:
            NSeparator += 1
    
    # array yang akan diisi dengan elemen string yang sudah di split
    tempArr = ["" for i in range(NSeparator + 1)]

    # elemen pada array yang akan di split
    tempElement = ""

    # nomor kolom pada array yang akan diisi dengan tempElement
    kolom = 0

    # looping untuk mengecek tiap karakter pada string
    for i in range(len):

        # jika pada looping ketemu separator
        if data[i] == separator:
            
            # tempElement di assign ke current kolom
            tempArr[kolom] = tempElement

            # mereset nilai tempElement
            tempElement = ""

            # kolom berikutnya yang akan diisi
            kolom += 1

        # karena pada tempElement terakhir tidak ada seperator setelahnya
        # untuk mengetahui string sudah habis digunakan len-1 dari string tersebut
        elif i == len-1 :
            
            # tempElement di assign ke current kolom
            tempArr[kolom] = tempElement

        # jika belum ketemu separator
        else:

            # karakter akan di tambahkan ke tempElement
            tempElement += data[i]
    
    # mengeembalikan array yang berisi string yang sudah di split
    return tempArr