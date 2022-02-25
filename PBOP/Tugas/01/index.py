# Tugas 01 
# Membuat program rumus bangun datar 

# Nama : Naufal Firmansyah
# NIM  : 5210411166



def inputkan1():
    print('### Menghitung Luas PERSEGI PANJANG ###')
    pjg = int(input('Masukan Panjang Persegi Panjang : '))
    lbr = int(input('Masukan Lebar Persegi Panjang : '))

    ctk = pjg * lbr

    print('Luas Persegi Panjang : ',ctk)



def inputkan2():
    print('### Menghitung Luas PERSEGI ###')
    sisi = int(input('Masukan Sisi Persegi  : '))
    

    ctk = sisi**2

    print('Luas Persegi : ',ctk)



while True :
    print('''
MENU
1. Hitung Luas Persegi
2. Hitung Luas Persegi Panjang
3. Exit  
 
''')
    pil = int(input('Masukan Pilihan Anda :'))

    if pil == 1 :
        inputkan2()

    if pil == 2 :
        inputkan1()

    if pil == 3 :
        break

