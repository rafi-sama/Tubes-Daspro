# fungsi yang menambahkan arr + element (element di indeks terakhir)
def konso(arr, element):

    len = arr_len(arr)

    temp = ["" for i in range(len+1)]

    for i in range(len):
        temp[i] = arr[i]
    
    temp[len] = element

    return temp

# fungsi yang menambahkan element + arr (element di indeks pertama)
def konsDot(element, arr):

    len = arr_len(arr)

    temp = ["" for i in range(len+1)]

    for i in range(1, len+1):
        temp[i] = arr[i]
    
    temp[0] = element

    return temp  

# fungsi yang menggabungkan 2 arr
def konkat(arr1, arr2):
    
    len1 = arr_len(arr1) 
    len2 = arr_len(arr2)

    temp = ["" for i in range(len1+len2)]

    for i in range(len1):
        temp[i] = arr1[i]

    for j in range(len1, len1+len2):
        temp[j] = arr2[j-len1]
        print(temp)

    return temp

# fungsi yang menentukan panjang string
def str_len(string):

    len = 0
    temp = ""

    while temp != string:

        temp += string[len]
        len += 1
    
    return len

# fungsi yang menentukan panjang array
def arr_len(arr):

    temp = arr

    if temp == []:
        return 0

    temp[-1] = "*"

    for i in range(1000):

        if temp[i] == "*":

            return i+1


def split(string, delimiter):

    # variabel yang menyatakan banyaknya pemisah (ex: titik koma pada file .csv)
    NDelimiter = 0 

    # banyaknya karakter pada string yang ingin di split
    len = str_len(string) 

    # menghitung banyaknya separator
    for i in range(len): 
        if string[i] == delimiter:
            NDelimiter += 1
    
    # array yang akan diisi dengan elemen string yang sudah di split
    tempArr = ["" for i in range(NDelimiter + 1)]

    # elemen pada array yang akan di split
    tempElement = ""

    # nomor kolom pada array yang akan diisi dengan tempElement
    kolom = 0

    # looping untuk mengecek tiap karakter pada string
    for i in range(len):

        # jika pada looping ketemu separator
        if string[i] == delimiter:
            
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
            tempElement += string[i]
    
    # mengeembalikan array yang berisi string yang sudah di split
    return tempArr