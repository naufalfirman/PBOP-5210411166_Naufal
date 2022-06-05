from connect import mydb

cur = mydb.cursor()

sql1 = '''CREATE TABLE IF NOT EXISTS Supplier (
	Kode_Supplier VARCHAR(10) PRIMARY KEY NOT NULL,
	Nama_Supplier VARCHAR(40));'''

sql2 = '''CREATE TABLE IF NOT EXISTS Nota (
	No_Nota VARCHAR(10) PRIMARY KEY,
	Tanggal date,
	Tempo VARCHAR(10),
	Total INTEGER(10),
	Kode_Supplier VARCHAR(10),
	FOREIGN KEY(Kode_Supplier) REFERENCES Supplier(Kode_Supplier));'''

sql3 = '''CREATE TABLE IF NOT EXISTS Barang (
	Kode_Barang VARCHAR(10) PRIMARY KEY NOT NULL,
	Nama_Barang VARCHAR(40));'''

sql4 = '''CREATE TABLE IF NOT EXISTS Tr_Brg (
	No_Nota VARCHAR(10),
	Kode_Barang VARCHAR(10),
	Qty INTEGER(10),
	Harga INTEGER,
	FOREIGN KEY(No_Nota) REFERENCES Nota(No_Nota),
	FOREIGN KEY(Kode_Barang) REFERENCES Barang(Kode_Barang));'''



cur.execute(sql1)
cur.execute(sql2)
cur.execute(sql3)
cur.execute(sql4)

print("TABEL BERHASIL DIBUAT !!! ")