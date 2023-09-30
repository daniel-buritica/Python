import sqlite3

con = sqlite3.connect(r"C:\Users\burit\Documents\Backend\Python\sqllite\app.db")
cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios
    (id INTEGER primary key, nombre varchar(50));
    """
)
con.commit()
con.close()
