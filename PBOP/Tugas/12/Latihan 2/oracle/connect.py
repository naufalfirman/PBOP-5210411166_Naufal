import cx_Oracle

mydb = cx_Oracle.connect(
    "latihan2",
    "latihan2",
    "127.0.0.1/XE"
)


print("DATABASE BERHASIL TERHUBUNG !!! ")