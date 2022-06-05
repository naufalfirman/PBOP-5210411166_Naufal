import cx_Oracle
con = cx_Oracle.connect(
    "tugas_pbop",
    "pbop",
    "127.0.0.1/XE"
)
print("DATABASE BERHASIL TERKONEKSI")