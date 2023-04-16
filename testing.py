# from functions import *

# user_csv = open("file/user.csv",'r')

# user_csv = [row for row in user_csv]

# print(user_csv)

# # for row in user_csv:
# #     print(row)

# baris = len_count(user_csv)

# kolom = 0
# temp = user_csv[0]

# for i in range(len_count(temp)):
#     if temp[i] == ";":
#         kolom = 0

# kolom += 1

# user = ["" for i in range(baris)]


# for i in range(baris):

#     user[i] = split(user_csv[i], ";")

# print(user)

from functions import *
x = [["id","pembuat","pasir","batu","air"],
     ["1","kirito","2","3","4"],
     ['2','asuna','4','1','3'],
     ['3','rimuru','3','1','3'],
     ['4','tempest','1','2','4']]


def DetectBahan(candi):
        c = 1
        pasir = 0
        batu = 0
        air = 0
        for i in range (1,arr_len(candi)):
            pasir += int(candi[i][2])
            batu += int(candi[i][3])
            air += int(candi[i][4])
            i += 1
        return pasir,batu,air


print(DetectBahan(x))


