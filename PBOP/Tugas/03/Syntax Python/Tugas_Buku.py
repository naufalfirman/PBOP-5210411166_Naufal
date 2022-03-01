class Buku:
    def _init_(self,judul, pengarang, tahun_terbit):
        self.judul        = judul
        self.pengarang    = pengarang
        self.tahun_terbit = tahun_terbit

buku1 = Buku('Tenggelamnya Kapal Van Der Wijck', 'HAMKA', 1938)
buku2 = Buku('Laskar Pelangi', 'Andrea Hirata', 2005)
buku3 = Buku('Cantik Itu Luka', 'Eka Kurniawan', 2002)

b = [buku1, buku2, buku3]

for buku in b:
    t = 'Buku {} karangan{} pertama kali diterbitkan tahun {}'.format(buku.judul,buku.pengarang,buku.tahun_terbit)
    print(t)
