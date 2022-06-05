import psycopg2

db = psycopg2.connect(
    host="localhost",
    user="nfl",
    password="123",
    database="toko"
)

cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Supplier (
	Kode_Supplier VARCHAR(3) PRIMARY KEY NOT NULL,
	Nama_Supplier VARCHAR(40));''')

cur.execute('''CREATE TABLE IF NOT EXISTS Nota (
	No_Nota VARCHAR(3) PRIMARY KEY,
	Tanggal date,
	Tempo VARCHAR(10),
	Total INT,
	Kode_Supplier VARCHAR(3),
	FOREIGN KEY(Kode_Supplier) REFERENCES Supplier(Kode_Supplier));''')

cur.execute('''CREATE TABLE IF NOT EXISTS Barang (
	Kode_Barang VARCHAR(3) PRIMARY KEY NOT NULL,
	Nama_Barang VARCHAR(40));''')

cur.execute('''CREATE TABLE IF NOT EXISTS Tr_Brg (
	No_Nota VARCHAR(3),
	Kode_Barang VARCHAR(3),
	Qty INT,
	Harga INT,
	FOREIGN KEY(No_Nota) REFERENCES Nota(No_Nota),
	FOREIGN KEY(Kode_Barang) REFERENCES Barang(Kode_Barang));''')

db.commit()

print("DATABASE BERHASIL TERHUBUNG DAN MEMBUAT TABEL")
