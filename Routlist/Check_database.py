import sqlite3
conn = sqlite3.connect("Routes.db")
c = conn.cursor()


#Honestly not sure if this prooved these tables exist, but we will find out
c.execute("SELECT name FROM Routes WHERE type='table' ")

conn.commit()
conn.close()