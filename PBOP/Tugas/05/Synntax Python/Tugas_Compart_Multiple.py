
class prosessor() :
    def __init__(self, prosesor) -> None:
        self.prosesor = prosesor


class RandomAkksesmemori() :
    def __init__(self, detail_ram) -> None:
        self.ram = detail_ram


class Storage() :
    def __init__(self, hdd) -> None:
        self.hdd = hdd

class Monitor() :
    def __init__(self, mntr) -> None:
        self.monitor = mntr

# CHILD

class Computerpart(prosessor, Storage, RandomAkksesmemori, Monitor) :
    def __init__(self, prosesor, ram, hdd, mntr) -> None:
        prosessor.__init__(self, prosesor)
        Storage.__init__(self, hdd)
        RandomAkksesmemori.__init__(self, ram)
        Monitor.__init__(self, mntr)



this_pc = Computerpart("Intel® Core™ i9‑11900H", "DOMINATOR® PLATINUM RGB 32 GB (2 x 16 GB) DDR4 DRAM 3200MHz C16 Memory Kit", "HDD Toshiba 1 TB", "Monitor 24 inch Samsung S24F350FHE")
print("\n",
f'''
Saya mempunyai PC/Komputer dengan Spesifikasi Sebagai Berikut : 

Processor           : {this_pc.prosesor}
Random Acces Memory : {this_pc.ram}
Storage             : {this_pc.hdd}
Monitor             : {this_pc.monitor}
 ''')


