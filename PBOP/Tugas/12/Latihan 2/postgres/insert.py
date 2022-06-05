from connect import mydb

cur = mydb.cursor()

# insert data dosen
cur.execute("INSERT INTO Dosen VALUES ('D2L', 'Danu Dwiki Laksana', 'Pemalang City', '0864632638');")
cur.execute("INSERT INTO Dosen VALUES ('EAGS', 'Esa Age Giant Saputra', 'Ngawi', '99999999');")

# insert data matakuliah
cur.execute("INSERT INTO MataKuliah VALUES ('MK1', 'PBOP', '3', '2');")
cur.execute("INSERT INTO MataKuliah VALUES ('MK2', 'Kewarganegaraan', '3', '2');")
cur.execute("INSERT INTO MataKuliah VALUES ('MK3', 'SISCER', '3', '2');")

# insert data Kuliah
cur.execute("INSERT INTO Kuliah VALUES ('MK1', 'D2L', '10:40', 'LC2.2');")
cur.execute("INSERT INTO Kuliah VALUES ('MK2', 'D2L', '14:40', 'LK2.2');")
cur.execute("INSERT INTO Kuliah VALUES ('MK3', 'EAGS', '08:00', 'D3.3');")

mydb.commit()

print("DATA BERHASIL DISISIPKAN !!! \n")

