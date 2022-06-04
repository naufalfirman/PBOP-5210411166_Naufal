from connect import con

cur = con.cursor()

# INSERT DATA JABATAN
cur.execute("INSERT INTO JABATAN VALUES ('K01', 'DIREKTUR', 12000000, 5000000)")
cur.execute("INSERT INTO JABATAN VALUES ('K02', 'SEKRETASRIS', 7000000, 3000000)")
cur.execute("INSERT INTO JABATAN VALUES ('K03', 'KARYAWAN', 5000000, 1000000)")


# INSERT DATA GOLONGAN
cur.execute("INSERT INTO GOLONGAN VALUES ('01', 'Pertama', 500000, 500000, 200000, 100000, 100000)")
cur.execute("INSERT INTO GOLONGAN VALUES ('02', 'Kedua', 400000, 400000, 200000, 100000, 100000)")

# INSERT DATA PEGAWAI
cur.execute("INSERT INTO PEGAWAI VALUES ('123456789', 'Naufal Firmansyah', 'K01' , '01', 'Jomblo', 0)")
cur.execute("INSERT INTO PEGAWAI VALUES ('987654321', 'Zaedar Ghazalba', 'K03' , '01', 'Jomblo High', 0)")


# INSERT DATA GAJI
cur.execute("INSERT INTO GAJI VALUES ('April', '123456789', 23, 0, 2, 1, 0, 50000)")
cur.execute("INSERT INTO GAJI VALUES ('April', '987654321', 22, 1, 1, 1, 1, 50000)")


con.commit()

