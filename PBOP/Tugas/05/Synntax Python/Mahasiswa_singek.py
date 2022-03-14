class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim
    
    def detailmhs(self):
        return self.nim, self.nama
    
    def cekMhs(self):
        if self.nim < 150000:
            return 'Mahasiswa aktif'
        else:
            return 'Mahasiswa tidak terdaftar'

class Siswa(Mahasiswa):
    def End(self):
        print('Mahasiswa belum melakukan daftar ulang')

mahasiswa1 = Mahasiswa('Mahasiswa 1', 135103)
print(mahasiswa1.detailmhs(), mahasiswa1.cekMhs())

mahasiswa2 = Siswa('Mahasiswa 2', 150503)
print(mahasiswa2.detailmhs(), mahasiswa2. cekMhs())
mahasiswa2.End()