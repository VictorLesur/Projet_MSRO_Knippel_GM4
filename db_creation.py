import sqlite3

conn = sqlite3.connect('sqli_db.db')

c = conn.cursor()

c.execute('''CREATE TABLE users
(user TEXT, pass TEXT)''')


c.execute('''INSERT INTO users
VALUES('admin','mdpAdmin')''')

def maBelleFonction(nombre):
    return nombre*3


print("wsh")

def f(x) :
	return x

conn.commit()

conn.close()
