import sqlite3

with sqlite3.connect("D:\Documentos\Backend\Python\sqllite\app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        "insert into usuarios values (?,?)",
        (1, "daniel")
    )