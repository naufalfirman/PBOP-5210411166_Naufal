from connect import db, cur

# -- INSERT CabangBank
cur.execute("INSERT INTO CabangBank VALUES ('CLP', 'Cilacap', 'Cilacap Jawa Tengah') , ('KBM', 'Kebumen', 'Kebumen Jawa Tengah');")

# -- INSERT Nasabah
cur.execute("INSERT INTO Nasabah VALUES ('CLP1', 'Naufal Firmansyah', 'Kec. Nusawungu'), ('KBM1', 'Dea Meiliyandry', 'Kec. Rowokele'), ('CLP2', 'Nurul Atikah', 'Kec. Nusawungu');")

# -- INSERT Rekening
cur.execute("INSERT INTO Rekening VALUES ('123456789', '123456', 'CLP1', 'CLP', 12000000), ('234567891', '234567', 'CLP2', 'CLP', 10000000), ('987654321', '654321', 'KBM1', 'KBM', 50000000);")

# -- INSERT Transaksi
cur.execute("INSERT INTO Transaksi VALUES ('trx01' , 'Gold', 'CLP1', date('now'), 8000000), ('trx05' , 'Platinum', 'KBM1', date('now'), 30000000);")


# commit database
db.commit()

print("DATA BERHASIL DIINPUTKAN")
