# Mahasiswa Overloading
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilMhs(self):
        print("Nama:", self.nama, ", nim:", self.nim)
    
    #   Method Overloading
    def hitungSKS(self, jmlsks=None, sks=None):
        if jmlsks !=None and sks!=None:
            totalsks = jmlsks + sks
            print("Total sks =", totalsks)
        else:
            totalsks = jmlsks
            print("Total sks =", totalsks)

        if totalsks >= 100:
            print("Diperbolehkan mengambil skripsi")
        
        else:
            print("Tidak diperbolehkan mengambil skripsi")

mhs1 = Mahasiswa("Eren", 123180015)
mhs2 = Mahasiswa("Luffy", 123190007)
mhs1.tampilMhs()
mhs2.tampilMhs()
mhs1.hitungSKS(80, 34)
mhs2.hitungSKS(83)