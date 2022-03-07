class MobilVariabel:
    # private variabel
    def __init__(self, jendela, pintu, mesin):
        self.__jendela = jendela
        self.__pintu = pintu
        self.__mesin = mesin
    
mobil1 = MobilVariabel(2, 2, '2JZ-GTE')

print(mobil1._MobilVariabel__jendela, mobil1._MobilVariabel__pintu, mobil1._MobilVariabel__mesin )