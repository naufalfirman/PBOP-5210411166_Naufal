class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def detSiswa(self):
        print(self.nama, 'alamat: wall rose')

class Siswa(Mahasiswa):
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim

    def detSiswa(self):
        print(self.nama, 'Jurusan: Informatika')

mhs1 = Siswa('Mikasa', 135105)
mhs2 = Mahasiswa('Nezuko', 135119)

print(mhs1.nim, mhs1.nama)
mhs1.detSiswa()
print(mhs2.nim, mhs2.nama)
mhs2.detSiswa()