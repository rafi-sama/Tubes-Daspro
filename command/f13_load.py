from functions import *

def load(file_name, variable):

    with open(file_name, 'r') as file:

        # mengubah file menjadi bentuk array/list
        reader = [row for row in file]

        baris = arr_len(reader)

        # membuat array kosong sebanyak baris
        tempArr = ["" for i in range(baris)]

        # looping untuk mengisi setiap baris dengan array string yang sudah di split
        for i in range(baris):
            tempArr[i] = split(reader[i], ";")

        variable = tempArr

    return variable