from abc import ABC, abstractmethod

class bentuk(ABC) :
    @abstractmethod
    def luas(self):
        return self.__sisi * self.__sisi

    @abstractmethod
    def keliling(self):
        return 4 * self.__sisi  

class persegi(bentuk): 
        def __init__(self,sisi):
            self.__sisi = sisi
        def luas(self):
            return self.__sisi * self.__sisi
        def keliling(self):
            return 4 * self.__sisi 

Persegi = persegi(6)
print(Persegi.luas())
print(Persegi.keliling())