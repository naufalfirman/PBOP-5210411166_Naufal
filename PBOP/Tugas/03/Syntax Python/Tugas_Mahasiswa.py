class Mahasiswa:
    def _init_(self, nama, nim, prodi,thn_masuk):
        self.nama      = nama
        self.nim       = nim
        self.prodi     = prodi
        self.thn_masuk = thn_masuk

m1 = Mahasiswa('Udin', '10120371','Sistem Informasi',2020)
m2 = Mahasiswa('Naufal', '5210411166','Informatika',2021)
m3 = Mahasiswa('Abel', '5210411181','Pariwisata',2021)
mahasiswa  = [m1, m2, m3]

for m in mahasiswa:
    teks = '{} adalah mahasisma {}angkatan {} dengan NIM {}'.format(m.nama, m.prodi, m.thn_masuk, m.nim)
    print(teks)