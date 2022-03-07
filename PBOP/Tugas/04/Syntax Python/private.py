#Latihan Hak akses Private

class Hitung:
    def __init__(self):
        self._angkaRahasia = 0

    def tampilkanHitung(self):
        self._angkaRahasia += 1
        print(self._angkaRahasia)

hitungan = Hitung()
hitungan.tampilkanHitung()