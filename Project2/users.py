import sqlite3

# Підключаємось до бази даних (файл буде створено, якщо не існує)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Створюємо таблицю users
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

# Додаємо нові значення
cursor.execute("INSERT INTO users (name, email) VALUES ('Smth', 'smth@goiteens.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Idk', 'idk@goiteens.com')")

cursor.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@goiteens.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@goiteens.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Charlie', 'charlie@goiteens.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Dave', 'dave@goiteens.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Eve', 'eve@goiteens.com')")


# Зберігаємо зміни
conn.commit()

# Закриваємо підключення
conn.close()
