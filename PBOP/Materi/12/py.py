import cx_Oracle


con = cx_Oracle.connect(
    "py",
    "py",
    "127.0.0.1/XE"
)

cur = con.cursor()

sql =  '''
create table produk (
    kode char (10) not null primary key,
    nama varchar (20),
    harga number(100)
)

'''

cur.execute(sql)
cur.close()
con.close()