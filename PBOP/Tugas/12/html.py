import cx_Oracle

con = cx_Oracle.connect(
    "esa",
    "esa",
    "127.0.0.1/XE"

)

cur = con.cursor()

sql = '''
create table jabatan (
    Kode_Jabatan varchar(3)
    nama_jabatan varchar(40)
    gapok int(10)
)
'''

cur.execute(sql)
