class Mahasiswa():
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim

class siswa1(Mahasiswa):
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

class siswa2(Mahasiswa):
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim

mhs1 = Mahasiswa('Mikasa', 1315105)
mhs2 = Mahasiswa('Nezuko', 135117)
mhs3 = Mahasiswa('Hancock', 134079)

print(mhs1.nama, mhs1.nim)
print(mhs2.nim)
print(mhs2.nama)