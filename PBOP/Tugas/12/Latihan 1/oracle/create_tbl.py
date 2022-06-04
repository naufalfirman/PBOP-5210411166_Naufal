from connect import con

cur = con.cursor()

cur.execute('''
        CREATE TABLE jabatan (
            kode_jabatan VARCHAR (3) NOT NULL PRIMARY KEY,
            nama_jabatan VARCHAR (25),
            gapok NUMBER,
            tunjangan_jabatan NUMBER
        )
        ''')


cur.execute('''
        CREATE TABLE Golongan (
            kode_golongan VARCHAR (2) NOT NULL PRIMARY KEY,
            nama_golongan VARCHAR (10),
            tunjangan_suami NUMBER,
            tunjangan_anak NUMBER,
            uang_makan NUMBER,
            uang_lembur NUMBER,
            akses NUMBER
        )
        ''')

cur.execute('''
        CREATE TABLE Pegawai (
            nip	VARCHAR (20) NOT NULL PRIMARY KEY,
            nama_pegawai VARCHAR (40),
            kode_jabatan VARCHAR (3),
            kode_golongan VARCHAR (3),      
            status VARCHAR (15),
            jumlah_anak NUMBER
        )
        ''')

cur.execute('''
CREATE TABLE Gaji (
	bulan VARCHAR (20),
	nip VARCHAR (20),
	masuk NUMBER,
	sakit NUMBER,
	ijin NUMBER,
	alpha NUMBER,
	lembur NUMBER,
	potongan NUMBER
    )
    ''')