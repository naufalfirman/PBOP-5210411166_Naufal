import sqlite3

with sqlite3.connect('bank.db') as db:
    cur = db.cursor()


