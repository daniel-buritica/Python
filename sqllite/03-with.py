import sqlite3

with sqlite3.connect(r"C:\Users\burit\Documents\Backend\Python\sqllite\app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios
        (id INTEGER primary key, nombre varchar(50));
        """
    )


