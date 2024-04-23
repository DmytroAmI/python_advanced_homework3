import sqlite3

conn = sqlite3.connect('sqlite3.db')
cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE "materials" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            weight,
            height,
            additional)
    """)

conn.commit()
conn.close()
