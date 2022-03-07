class Mobilprotected:
    # protected variabel
    def __init__(self, jendela, pintu, mesin):
        self._jendela = jendela
        self._pintu = pintu
        self._mesin = mesin
mobil1 = Mobilprotected(2, 2, "2JZ-GTE")

print(mobil1._jendela)