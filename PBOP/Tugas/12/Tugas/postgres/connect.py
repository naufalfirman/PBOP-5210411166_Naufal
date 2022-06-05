import psycopg2

db = psycopg2.connect(
    host='localhost',
    user='naufal',
    password='123',
    database='Bank'
)
cur = db.cursor()

