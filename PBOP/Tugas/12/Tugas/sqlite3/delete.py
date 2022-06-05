from connect import db, cur

# delete transaksi
cur.execute(
    "DELETE FROM Transaksi WHERE noTransaksi = 'trx05' AND idNasabah = 'CLP2';")

# delete rekening
cur.execute("DELETE FROM Rekening WHERE noRekening = '987654321' ;")

# delete nasabah
cur.execute("DELETE FROM Nasabah WHERE idNasabah = 'CLP2';")

# delete cabang bank
cur.execute("DELETE FROM CabangBank WHERE kodeCabang = 'CLP';")


db.commit()

print("DATA BERHASIL DIHAPUS !!!")
