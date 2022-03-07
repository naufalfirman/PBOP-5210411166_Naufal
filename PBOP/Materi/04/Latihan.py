# from argparse import Namespace


# class Segitiga:
#      def _init_(self, alas, tinggi):
#           self.alas = alas
#           self.tinggi = tinggi
#           self.luas = 0.5 * alas * tinggi
# segitiga_besar = Segitiga(100,80)

# # akses variable public :alas, tinggi, dan luas dari kelas segitiga
# print("alas: ", segitiga_besar.alas)
# print("tinggi:", segitiga_besar.tinggi)
# print("luas: ", segitiga_besar.luas)

# class Utama:
#     def _init_(self):
#         self._a = 2


# class Turunan(Utama):
#     def _init_(self):
        

#         # memanggil konstruktor pada kelas utama
#         Utama._init_(self)
#         print("Memanggil variabel protected pada class utama : ", self._a)


#         # modify
#         self._a= 3
#         print("Memanggil variabel protected yang di modifikasi diluar class :", self._a)

# objek1 = Turunan()
# objek2 = Utama()

# # memanggil variabel utama
# print("Memanggil variabel protected pada objek1 :", objek1._a)
# print("Memanggil variabel protected pada objek1 :", objek2._a)

# class Hitung:
#     def _init_(self):
#         self._angkaRahasia = 0


#     def tampilkanHitung(self):
#         self._angkaRahasia += 1
#         print(self._angkaRahasia)


#         # modify

# hitungan = Hitung()
# hitungan.tampilkanHitung()


class mobil():
    def __init__(self, jendela, pintu, mesin):
        self.__jendela = jendela
        self.__pintu = pintu
        self.__mesin = mesin
audi = mobil(4,4,"Disel")
audi.mobil__mesin

class pegawai:
    __nama =  ""
    __alamat = ""
    __gaji = 0

    def __init__(self, nama, alamat) :
        self.nama=nama
        self.alamat=alamat
    
    def __hitunggaji (self):
        upahlembur = 20000
        gajipokok = 2000000
        waktulembur = int(input("Total Jam Lembur"))
        self.__gaji= (upahlembur*waktulembur)+gajipokok

    def tampildetail (self):
        print('\n -- Menghitung Dan Menampilkan Detail Gaji Karyaawan -- ')
        print("Nama : ", self.__nama)
        print("Alamat : ", self.__alamat)
        self.__hitunggaji()
        print("Total Gaji :", self.__gaji)

pgw1 = pegawai("Naufal Firmansyah", "Wall ROse")
pgw1.tampildetail()

pgw2 = pegawai("Naufal Firmansyah", "Wall ROse")
pgw2.tampildetail()
