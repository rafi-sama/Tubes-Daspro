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

    if arr == []:
        return 0
    
    temp = arr[-1]
    arr[-1] = "*"

    for i in range(1000):

        if arr[i] == "*":

            arr[-1] = temp
            return i+1


def convertToArr(file, delimiter):

    data = file.readlines()
    row = arr_len(data)

    if row == 0:
        return []

    column = 1
    for i in range(str_len(data[0])):
        if data[0][i] == delimiter:
            column += 1

    tempArr = [[0 for i in range(column)] for i in range(row)]

    for i in range(row):

        temp = ""
        insert_column = 0

        for j in range(str_len(data[i])):

            if ((data[i][j] != "\n") and (data[i][j] != delimiter)):

                temp += data[i][j]
            
            else:

                tempArr[i][insert_column] = temp

                temp = ""
                insert_column += 1

    tempArr[row-1][column-1] = temp

    return tempArr


def isMember(element, arr):
    
    for i in range(arr_len(arr)):

        if arr[i] == element:
            return True
        
    return False