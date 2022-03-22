class ComputerPart:
    def __init__(self, pabrikan, nama):
        self.pabrikan = pabrikan
        self.nama     = nama
    
    def detComputer(self):
        print('Pabrikan: ', self.pabrikan, 'nama: ', self.nama)

    def HitungHarga(self, harga=None):
        if harga != None:
            h = harga
            print('Harga: ', h)
        else:
            print('Tidak ada pesanan')

com1 = ComputerPart('LENOVO', 'THINK STRIX')
com2 = ComputerPart('ASUS', 'TUF GAMING')
com1.detComputer()
com2.detComputer()
com1.HitungHarga(100000)
com2.HitungHarga(200000)