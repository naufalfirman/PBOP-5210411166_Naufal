import psycopg2

db = psycopg2.connect(
    user="postgres",
    password="123",
    host="localhost",
    database="tugas_pbop"
)

print("DATABASE BERHASIL TERKONEKSI")