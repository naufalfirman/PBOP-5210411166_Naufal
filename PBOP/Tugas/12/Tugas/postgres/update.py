from connect import db, cur

# update cabang bank
cur.execute(
    "UPDATE CabangBank SET alamatCabang = 'Kab. Cilacap' WHERE kodeCabang = 'CLP'")

# update Nasabah
cur.execute(
    "UPDATE Nasabah SET namaNasabah = 'Danu Dwiki Laksana' WHERE idNasabah = 'CLP2';")

# update rekening Bank
cur.execute(
    "UPDATE Rekening SET saldo = 20000000 WHERE noRekening = '123456789';")

# update transaksi
cur.execute(
    "UPDATE Transaksi SET jumlah = 10000000 WHERE noTransaksi = 'trx01' AND idNasabah = 'CLP2';")

db.commit()

print(" DATA BERHASIL DIUPDATE !!! ")
