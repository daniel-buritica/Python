import sqlite3

con = sqlite3.connect(r"C:\Users\burit\Documents\Backend\Python\sqllite\app.db")
cursor = con.cursor()
con.close()