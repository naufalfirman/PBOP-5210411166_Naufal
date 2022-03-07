class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, harga):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.__harga = harga #private

    def tampil(self):
        print( "Judul :", self.judul)
        print( "Pengarang :", self.pengarang)
        print( "Tahun terbit :", self.tahun_terbit)
        print( "Harga :", self.__harga)

# buku = Buku('Tenggelamnya Kapal Van der Wijck','HAMKA', 1938,35000)
# print(Buku._init_._harga)
buku = Buku('Tenggelamnya Kapal Van der Wijck','HAMKA', 1938,35000)
print(buku.tampil())