import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS musician (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        instrument TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS album (
        id INTEGER PRIMARY KEY,
        FOREIGN KEY (artist) REFERENCES musician.id,
        release_date TEXT NOT NULL,
        num_stars INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        birthday TEXT NOT NULL,
        age INTEGER NOT NULL,
        mail TEXT NOT NULL
    )
''')