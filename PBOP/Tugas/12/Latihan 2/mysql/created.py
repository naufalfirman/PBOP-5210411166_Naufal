from connect import mydb

cur = mydb.cursor()



sql1 = '''CREATE TABLE IF NOT EXISTS Dosen (
    Kode_Dos VARCHAR(5) PRIMARY KEY NOT NULL,
    Nama_Dos VARCHAR(40),
    Alamat_Dos VARCHAR(125),
    No_Telp VARCHAR(15)
    );'''
sql2 = '''CREATE TABLE IF NOT EXISTS MataKuliah (
    Kode_MK VARCHAR(5) PRIMARY KEY NOT NULL,
    Nama_MK VARCHAR(40),
    SKS VARCHAR(1),
    Semester VARCHAR(1)    
);'''

sql3 = '''CREATE TABLE IF NOT EXISTS Kuliah (
    Kode_MK VARCHAR(5) ,
    Kode_Dos VARCHAR(5),
    Waktu TIME,
    Tempat VARCHAR(5),
    FOREIGN KEY(Kode_Dos) REFERENCES Dosen (Kode_Dos),
    FOREIGN KEY(Kode_MK) REFERENCES MataKuliah (Kode_MK)
    );'''

cur.execute(sql1)
cur.execute(sql2)
cur.execute(sql3)

print( " TABEL BERHASIL DIBUAT !!! ")