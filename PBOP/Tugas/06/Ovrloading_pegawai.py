#Overloading#
class Pegawai:
    jumlah = 0
    def __init__(self, nama, gaji) -> None:
        self.nama = nama
        self.gaji = gaji
        Pegawai.jumlah += 1
 
    def tampiljumlah (self):
        print("Total Pegawai : ", Pegawai.jumlah)
    def tampilpegawai (self):
        print(f'''  
Nama    : {self.nama}
Gaji    : {self.gaji}
''')
    def tunjangan(sekkf, istri = None, anak = None):
        if anak != None and istri != None :
            total = anak + istri
            print(f'''
Tunjangan Istri Dan Anak    : {total}''')
        else :
            total = istri
            print(f'''
Tunjangan Istri     : {total}''')


peg1 = Pegawai("EREN", 2000)
peg2 = Pegawai("DEA",6000)

peg1.tampilpegawai()
peg2.tampilpegawai()
peg1.tunjangan(2500.2500)
peg2.tunjangan(2500)

print("Total Peggawai %d" % Pegawai.jumlah)
rataGaji = (peg1.gaji + peg2.gaji)/ Pegawai.jumlah
print("Rata - rata Gaji Pegawai : ", str(rataGaji))