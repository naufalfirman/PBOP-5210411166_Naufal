# # Latihann Hak Ases Public
# class Segitiga:
#      def __init__(self, alas, tinggi):
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

# Latihan Hak Akses Protected


# class Utama:
#     def __init__(self):
#         self._a = 2

# class Turunan(Utama):
#     def __init__(self):
        

#         # memanggil konstruktor pada kelas utama
#         Utama.__init__(self)
#         print("Memanggil variabel protected pada class utama : ", self._a)


#         # modify
#         self._a= 3
#         print("Memanggil variabel protected yang di modifikasi diluar class :", self._a)

# objek1 = Turunan()
# objek2 = Utama()

# # memanggil variabel utama
# print("Memanggil variabel protected pada objek1 :", objek1._a)
# print("Memanggil variabel protected pada objek1 :", objek2._a)

# #Latihan Hak akses Private

# class Hitung:
#     def __init__(self):
#         self._angkaRahasia = 0

#     def tampilkanHitung(self):
#         self._angkaRahasia += 1
#         print(self._angkaRahasia)

# hitungan = Hitung()
# hitungan.tampilkanHitung()

# # Latihan Fungsi Hak Aksess Public, Private, Protected

# class pegawai:
#     __nama =  ''
#     __alamat = ''
#     __gaji = 0

#     def __init__(self, nama, alamat) -> None:
#         self.__nama=nama
#         self.__alamat=alamat
    
#     def __hitunggaji(self):
#         upahlembur = 20000
#         gajipokok = 2000000
#         waktulembur = int(input("Total Jam Lembur"))
#         self.__gaji = (upahlembur*waktulembur)+gajipokok

#     def tampildetail(self):
#         print('\n -- Menghitung Dan Menampilkan Detail Gaji Karyaawan -- ')
#         self.__hitunggaji()
#         print("Nama : ", self.__nama)
#         print("Alamat : ", self.__alamat)
#         print("Total Gaji :", self.__gaji)

# pgw1 = pegawai('Naufal', 'Wall ROse')
# pgw1.tampildetail()

# pgw2 = pegawai('Saya Kisaragi', 'Wall ROse')
# pgw2.tampildetail()



# # Latihan Variabel Hak Ases Public, Protected, Private

# class Mobilpublic:

#     # public variabel
#     def __init__(self, jendela, pintu, mesin):
#         self.jendela = jendela
#         self.pintu = pintu
#         self.mesin = mesin
# mobil1 = Mobilpublic(2, 2, "2JZ-GTE")

# print(mobil1.jendela)

# class Mobilprotected:
#     # protected variabel
#     def __init__(self, jendela, pintu, mesin):
#         self._jendela = jendela
#         self._pintu = pintu
#         self._mesin = mesin
# mobil1 = Mobilprotected(2, 2, "2JZ-GTE")

# print(mobil1._jendela)

# class MobilVariabel:
#     # private variabel
#     def __init__(self, jendela, pintu, mesin):
#         self.__jendela = jendela
#         self.__pintu = pintu
#         self.__mesin = mesin
    
# mobil1 = MobilVariabel(2, 2, '2JZ-GTE')

# print(mobil1._MobilVariabel__jendela, mobil1._MobilVariabel__pintu, mobil1._MobilVariabel__mesin )





# class Buku:
#     def __init__(self,judul, pengarang, tahun_terbit, harga):
#         self.judul        = judul
#         self.pengarang    = pengarang
#         self.tahun_terbit = tahun_terbit
#         self.Buku__harga      = harga

# buku1 = Buku('Tenggelamnya Kapal Van Der Wijck', 'HAMKA', 1938, 35000)
# buku2 = Buku('Laskar Pelangi', 'Andrea Hirata',  2005, 40000)
# buku3 = Buku('Cantik Itu Luka', 'Eka Kurniawan', 2002, 50000)

# b = [buku1, buku2, buku3]

# for buku in b:
#     t = 'Buku {} karangan {} pertama kali diterbitkan tahun {} dengan harga --> {}'.format(buku.judul,buku.pengarang,buku.tahun_terbit, buku.Buku__harga)
#     print(t)




# class Mahasiswa:
#     def __init__(self, nama, nim, prodi,thn_masuk):
#         self.nama      = nama
#         self.nim       = nim
#         self.Mahasiswa__prodi  = prodi
#         self.thn_masuk = thn_masuk

# m1 = Mahasiswa('Udin', '10120371','Sistem Informasi',2020)
# m2 = Mahasiswa('Naufal', '5210411166','Informatika' ,2021)
# m3 = Mahasiswa('Umron' , '5210411671','Pariwisata' ,2021)

# m  =  [m1, m2, m3]

# for teks in m :
#     tt = '{} adalah mahasisma {}angkatan {} dengan NIM {}'.format(teks.nama, teks.Mahasiswa__prodi, teks.thn_masuk, teks.nim)
#     print(tt)


class MenuMinuman:
    def __init__(self,nama,deskripsi,harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.MenuMinuman__harga = harga

mnm1 = MenuMinuman('Jus Jambu', 'Jus Jambu Merah Tanpa Gula', 8500)
mnm2 = MenuMinuman('Jus Alpukan Ori', 'Jus Alpukat Dengan Tambahan Air Gula Merah', 15000)
mnm3 = MenuMinuman('Jus Alpukat Xtra Milk', 'Jus Alpukat Dengan Campuran Susu Cokelat dan Taburan Kepingan Choco', 15000)
mnm4 = MenuMinuman('Red & Smooth', 'Smoothie pisang susu dengan strawberry', 17500)


pilihan_minuman = [mnm1, mnm2, mnm3, mnm4]
print('Daftar menu Healthy Fruits')
for mn in pilihan_minuman:
    t = '{} harga Rp {}, {}'.format(mn.nama, mn.MenuMinuman__harga, mn.deskripsi)
    print(t)