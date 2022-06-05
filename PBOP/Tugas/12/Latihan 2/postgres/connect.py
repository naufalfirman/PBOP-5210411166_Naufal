import psycopg2

mydb = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="123",
    database="tugas_pbop"
)


print("SUCCSESFULL CONNECTION TO DATABASE")