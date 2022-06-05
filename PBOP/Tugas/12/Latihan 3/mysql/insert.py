from connect import mydb

cur = mydb.cursor()

# insert data supplier
cur.execute("INSERT INTO Supplier VALUES ('A1', 'Danu Dwiki Laksana'), ('A2', 'Esa Age Giant');")

# insert data Nota
cur.execute("INSERT INTO Nota VALUES ('001' ,date('now'), 'Tempo apasi', 1000000, 'A1'), ('002',date('now'), 'Tempo bos', 1500000, 'A2');")

# insert barang
cur.execute("INSERT INTO Barang VALUES ('B01', 'MACBOOK'), ('B02', 'Asus ROG 17 Pixel');")

# # insert tr_brg
cur.execute("INSERT INTO Tr_Brg VALUES ('001', 'B01', 2, 16000000), ('002', 'B02', 1, 10000000);")

mydb.commit()

print("DATA BERHASIL DIINPUTKAN !!!")
