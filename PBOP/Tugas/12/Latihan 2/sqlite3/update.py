from connect import mydb

cur = mydb.cursor()
# update data Dosen
cur.execute("UPDATE Dosen SET Nama_Dos = 'Zaedar Gazhalba' WHERE Kode_Dos = 'D2L';")

# update data Kuliah
cur.execute(
    "UPDATE Kuliah SET Tempat = 'LC2.3' WHERE Kode_MK = 'MK1' AND Kode_Dos = 'D2L';")

# update data mata kuliah
cur.execute(
    "UPDATE MataKuliah SET Nama_MK = 'Rekayasa Web Praktik' WHERE Kode_MK = 'MK1';")

mydb.commit()

print("DATA BERHASIL DI UPDATE !!! \n")
