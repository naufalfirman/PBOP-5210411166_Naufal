# Latihan Fungsi Hak Aksess Public, Private, Protected

class pegawai:
    __nama =  ''
    __alamat = ''
    __gaji = 0

    def __init__(self, nama, alamat) -> None:
        self.__nama=nama
        self.__alamat=alamat
    
    def __hitunggaji(self):
        upahlembur = 20000
        gajipokok = 2000000
        waktulembur = int(input("Total Jam Lembur"))
        self.__gaji = (upahlembur*waktulembur)+gajipokok

    def tampildetail(self):
        print('\n -- Menghitung Dan Menampilkan Detail Gaji Karyaawan -- ')
        self.__hitunggaji()
        print("Nama : ", self.__nama)
        print("Alamat : ", self.__alamat)
        print("Total Gaji :", self.__gaji)

pgw1 = pegawai('Naufal', 'Wall ROse')
pgw1.tampildetail()

pgw2 = pegawai('Saya Kisaragi', 'Wall ROse')
pgw2.tampildetail()
