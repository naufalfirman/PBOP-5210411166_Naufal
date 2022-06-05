import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='Bank'
)




print("DATABASE BERHASIL TERHUBUNG!!!")