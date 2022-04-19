class gaji :
    def __init__(self, gaji_bulanan):
        self.gaji_bulanan = gaji_bulanan

    def total(self):
        return (self.gaji_bulanan*12)


class Pegawai :
    jumlah = 0
    def __init__(self, gaji_bulanan, bonus, nama):
        self.gaji_bulanan=gaji_bulanan
        self.bonus= bonus
        self.obj_gaji = gaji(self.gaji_bulanan)
        self.nama = nama
        Pegawai.jumlah += 1

    def hasil_tahunan(self):
        return "Total:"+ str(self.obj_gaji.total() + self.bonus)+ "rupiah"      

    def tampiljumlah():
        print('Total Gaji Pegawai : ', Pegawai.jumlah)
    
    def tampilpegawai(self):
        print("Nama :",self.nama, "Gaji : ", self.gaji_bulanan, "Bonus  : ", self.bonus)

    def tunjangan(self, istri=None, anak=None):
        if anak !=None and istri !=None:
            total = anak+istri
            print("Tunjangan Anak Dan Istri : ", total)
        else :
            total = istri
            print("Tunjangan Istri  : ", total)

nm = str(input("Masukan Nama Pegawai    : "))
Gaji = int(input("Masukan Gaji  : "))
bns = int(input("Masukan Bonus  : "))
istr = int(input("Masukan Tunjangan Istri   : "))
ank = int(input("Masukan Tunjangan Anak : "))

peg1 = Pegawai(Gaji, bns,nm)
peg2 = Pegawai(Gaji, bns, nm)
peg1.tampilpegawai()
peg2.tampilpegawai()
peg1.tunjangan(ank, istr)
peg2.tunjangan(istr)



print("Total pegawai  =  %d" % Pegawai.jumlah)
rataGaji = (peg1.gaji_bulanan + peg2.gaji_bulanan)/Pegawai.jumlah
print("Rata-rata gaji = "+ str(rataGaji))


print(peg1.hasil_tahunan())
print(peg2.hasil_tahunan())
