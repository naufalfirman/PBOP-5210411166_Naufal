# from abc import ABC, abstractmethod

# class bentuk(ABC) :
#     @abstractmethod
#     def luas(self):
#         return self.__sisi * self.__sisi

#     @abstractmethod
#     def keliling(self):
#         return 4 * self.__sisi  

# class persegi(bentuk):
#         def __init__(self,sisi):
#             self.__sisi = sisi
#         def luas(self):
#             return self.__sisi * self.__sisi
#         def keliling(self):
#             return 4 * self.__sisi 

# Persegi = persegi(6)
# print(Persegi.luas())
# print(Persegi.keliling())

3
# Overloading
# class Pegawai:
#     jumlah = 0
#     def __init__(self, nama, gaji) -> None:
#         self.nama = nama
#         self.gaji = gaji
#         Pegawai.jumlah += 1
 
#     def tampiljumlah (self):
#         print("Total Pegawai : ", Pegawai.jumlah)
#     def tampilpegawai (self):
#         print(f'''  
# Nama    : {self.nama}
# Gaji    : {self.gaji}
# ''')
#     def tunjangan(sekkf, istri = None, anak = None):
#         if anak != None and istri != None :
#             total = anak + istri
#             print(f'''
# Tunjangan Istri Dan Anak    : {total}''')
#         else :
#             total = istri
#             print(f'''
# Tunjangan Istri     : {total}''')


# peg1 = Pegawai("EREN", 2000)
# peg2 = Pegawai("DEA",6000)

# peg1.tampilpegawai()
# peg2.tampilpegawai()
# peg1.tunjangan(2500.2500)
# peg2.tunjangan(2500)

# print("Total Peggawai %d" % Pegawai.jumlah)
# rataGaji = (peg1.gaji + peg2.gaji)/ Pegawai.jumlah
# print("Rata - rata Gaji Pegawai : ", str(rataGaji))


4
# Plymorhism
# Simple Example using len function

# print(len("Polymorphism"))
# print(len([1,2,3,4]))

# # using class 
# class jerman :
#     def ibukota(self):
#         print("berlin adalah ibukota negara jerman")
# class jepang :
#     def ibukota(self):
#         print("Tokyo adalah ibukota negara jepang")

# negara = jerman()
# ngr = jepang()
# for i in (negara, ngr):
#     i.ibukota()


5
# 5 Tugas 

# Overloading
# class ComputerPart:
#     def __init__(self, pabrikan, nama):
#         self.pabrikan = pabrikan
#         self.nama     = nama
    
#     def detComputer(self):
#         print('Pabrikan: ', self.pabrikan, 'nama: ', self.nama)

#     def HitungHarga(self, harga=None):
#         if harga != None:
#             h = harga
#             print('Harga: ', h)
#         else:
#             print('Tidak ada pesanan')

# com1 = ComputerPart('ASUS', 'ROG STRIX')
# com2 = ComputerPart('ASUS', 'TUF GAMING')
# com1.detComputer()
# com2.detComputer()
# com1.HitungHarga(100000)
# com2.HitungHarga(200000)

6
#  Tugas 
# Overriding
# class ComputerPart:
#     def __init__(self, pabrikan, nama):
#         self.pabrikan = pabrikan
#         self.nama     = nama
    
#     def detComputer(self):
#         print('Nama:',self.nama,'Harga: Rp.1000000')

# class ComputerPart_2(ComputerPart):
#     def __init__(self, pabrikan, nama):
#         self.pabrikan = pabrikan
#         self.nama     = nama
    
#     def detComputer(self):
#         print('Nama:',self.nama,'Harga: Rp.200000000')

# com1 = ComputerPart_2('Asus'  , 'ROG STRIX PRO')
# com2 = ComputerPart(  'Asus'  , 'TUF GAMING PRO')

# print(com1.pabrikan, com1.nama)
# com1.detComputer()

# print(com2.pabrikan, com2.nama)
# com2.detComputer()


7


# class burung:
#     def intro(self):
#         print("Di dunia ini ada beberapa type berbeda dari spesies burung")

#     def terbang(self):
#         print("Hampir semua burung dapat terbang, namun ada beberapa yang tidak dapat terbang")

# class Elang(burung):
#     def terbang(self):
#         print("Elang dapat terbang")

# class BurungUnta(burung):
#     def terbang(self):
#         print("Burung unta tidak dapat terbang")

# obj_burung = burung()
# obj_elang = Elang()
# obj_burung_unta = BurungUnta()

# obj_burung.intro()
# obj_burung.terbang()

# obj_elang.intro()
# obj_elang.terbang()

# obj_burung_unta.intro()
# obj_burung_unta.terbang()

8
# class Segiempat():
#     def __init__(self, panjang, lebar):
#         self.panjang = panjang
#         self.lebar   = lebar

#     def hitungLuas(self):
#         print("Luas Segiempat =", self.panjang * self.lebar, "m^2")
    
# class Bujursangkar(Segiempat):
#     def __init__(self, sisi):
#         self.side = sisi
#         Segiempat.__init__(self, sisi, sisi)

#     def hitungLuas(self):
#         print("Luas bujur sangkar =", self.side*self.side, "m^2")

# b = Bujursangkar(4)
# s = Segiempat(2,4)
# b.hitungLuas()
# s.hitungLuas()

9 

# Mahasiswa Overloading
# class Mahasiswa:
#     def __init__(self, nama, nim):
#         self.nama = nama
#         self.nim = nim

#     def tampilMhs(self):
#         print("Nama:", self.nama, ", nim:", self.nim)
    
#     #   Method Overloading
#     def hitungSKS(self, jmlsks=None, sks=None):
#         if jmlsks !=None and sks!=None:
#             totalsks = jmlsks + sks
#             print("Total sks =", totalsks)
#         else:
#             totalsks = jmlsks
#             print("Total sks =", totalsks)

#         if totalsks >= 100:
#             print("Diperbolehkan mengambil skripsi")
        
#         else:
#             print("Tidak diperbolehkan mengambil skripsi")

# mhs1 = Mahasiswa("Eren", 123180015)
# mhs2 = Mahasiswa("Luffy", 123190007)
# mhs1.tampilMhs()
# mhs2.tampilMhs()
# mhs1.hitungSKS(80, 34)
# mhs2.hitungSKS(83)


10
# class Mahasiswa:
#     def __init__(self, nama, nim):
#         self.nama = nama
#         self.nim = nim

#     def detSiswa(self):
#         print(self.nama, 'alamat: wall rose')

# class Siswa(Mahasiswa):
#     def __init__(self, nama, nim):
#         self.nama = nama
#         self.nim  = nim

#     def detSiswa(self):
#         print(self.nama, 'Jurusan: Informatika')

# mhs1 = Siswa('Mikasa', 135105)
# mhs2 = Mahasiswa('Nezuko', 135119)

# print(mhs1.nim, mhs1.nama)
# mhs1.detSiswa()
# print(mhs2.nim, mhs2.nama)
# mhs2.detSiswa()


10
# class Kucing:
#     def __init__(self, nama, umur):
#         self.nama = nama
#         self.umur = umur

#     def bersuara(self):
#         print('Meow')

# class Dog:
#     def __init__(self, nama, umur):
#         self.nama = nama 
#         self.umur = umur

#     def bersuara(self):
#         print('Guk...guk...')

# kucing1 = Kucing("Tom", 3)
# anjing1 = Dog("Spike", 4)

# for hewan in (kucing1, anjing1):
#     hewan.bersuara()
