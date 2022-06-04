from connect import mydb


cur = mydb.cursor()

# delete  gaji
sql1 = "DELETE FROM Gaji WHERE nip = '987654321' ;"

cur.execute()

# delete pegawai
sql2 = "DELETE FROM Pegawai WHERE nip = '987654321' ;"
cur.execute(sql2)

# delete golongan
sql3 = "DELETE FROM Golongan WHERE kode_golongan = '02' ;"
cur.execute(sql3)

# delete jabatan
sql4 = "DELETE FROM jabatan WHERE kode_jabatan = 'D02' ;"
cur.execute(sql4)

mydb.commit()



print("DATA BERHASIL DIHAPUS !!!")