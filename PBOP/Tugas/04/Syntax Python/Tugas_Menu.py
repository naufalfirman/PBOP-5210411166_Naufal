class MenuMinuman:
    def _init_(self,nama,deskripsi,harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga

mnm1 = MenuMinuman('Jus Jambu', 'Jus Jambu Merah Tanpa Gula', 8500)
mnm2 = MenuMinuman('Jus Alpukan Ori', 'Jus Alpukat Dengan Tambahan Air Gula Merah', 15000)
mnm3 = MenuMinuman('Jus Alpukat Xtra Milk', 'Jus Alpukat Dengan Campuran Susu Cokelat dan Taburan Kepingan Choco', 15000)
mnm4 = MenuMinuman('Red & Smooth', 'Smoothie pisang susu dengan strawberry', 17500)


pilihan_minuman = [mnm1, mnm2, mnm3, mnm4]
print('Daftar menu Healthy Fruits')
for mn in pilihan_minuman:
    t = '{} harga Rp {}, {}'.format(mn.nama, mn.harga, mn.deskripsi)
    print(t)