class computerPart:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class storage(computerPart):
    def __init__(self, nama, harga, jenis):
        super().__init__(nama, harga)
        self.jenis = jenis
        


class hdd(storage):
    def __init__(self,nama, harga, kapasistas, rpm):
        super().__init__(nama, harga, 'SSD')
        self.kapasitas = kapasistas
        self.rpm = rpm


pc = hdd('Seagate Harddisk Internal Barracuda',750000,'1 TB', '7200 rpm')

print(f'Alhamdulillah Saya Mampu Memiliki Perangkatb Computer dengan penyimpanan jenis {pc.jenis} yang berkapasitas {pc.kapasitas} dan memiliki RPM {pc.rpm}')