# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y

# tabPoint = [Point(0, 0), Point(1, 2), Point(3, 4)]

class User:

    def __init__(self, username: str, password: str, role: str):
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f"<username:{self.username}, password:{self.password}, role:{self.role}>"

    
class Bahan:

    def __init__(self, nama: str, deskripsi: str, jumlah: int):
        self.nama = nama
        self.deskripsi = deskripsi
        self.jumlah = int(jumlah)

    def __str__(self):
        return f"<nama:{self.nama}, deskripsi:{self.deskripsi}, jumlah:{self.jumlah}>"

    
class Candi:

    def __init__(self, id: int, pembuat: str, pasir: int, batu: int, air: int):
        self.id = int(id)
        self.pembuat = pembuat
        self.pasir = int(pasir)
        self.batu = int(batu)
        self.air = int(air)

    def __str__(self):
        return f"<id:{self.id}, pembuat:{self.pembuat}, pasir:{self.pasir}, batu:{self.batu}, pasir:{self.pasir}>"





