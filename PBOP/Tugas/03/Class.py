from numpy import broadcast_arrays


class mobil :
    def __init__(self,nama, tanggal, brand) :
        self.nama = nama
        self.tanggal = tanggal
        self.brand = brand

mobil1 = mobil('Avanza', 2003, 'Toyota')
mobil2 = mobil('Inova', 2004, 'Toyota')
mobil3 = mobil('Ferarri', 1929, 'Ferarri')

mobils = [mobil1, mobil2, mobil3]
for i in mobils :
    print(f'''Mobil {i.nama} pertama launching pada tahu {i.tanggal}, Mobil {i.nama} di produksi Oleh Perusahaan {i.brand}.''')