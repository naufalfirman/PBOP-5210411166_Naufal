import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pbop_tugas"
)

print("DATABASE BERHASIL TERHUBUNG !!!")


