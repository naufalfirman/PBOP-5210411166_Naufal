print('\n----> SINGGLE INHERITENCE <----')
class Hewan:
    def bersuara(self):
        print('kucing bersuara')

class Kucing(Hewan):
    def suara(self):
        print('meong...meong...meong')

k = Kucing()
k.suara()
k.bersuara()