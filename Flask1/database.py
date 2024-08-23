import sqlite3


conn = sqlite3.connect('news.db')
cursor = conn.cursor()

# Створення таблиці для новин
cursor.execute('''
CREATE TABLE IF NOT EXISTS news (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    date TIMESTAMP NOT NULL
)
''')

# Дані для вставки
news_data = [
    ('Данія оголосила про оборонний пакет для України на понад €100 млн', '2024-08-19 15:38'),
    ('AFP: проросійські новинні сайти ширили фейк, що замах на Трампа організував Обама', '2024-08-19 15:32'),
    ('Премʼєр Китаю поїде в росію та Білорусь. Для чого?', '2024-08-19 15:16'),
    ('В Індії тривають масові протести через зґвалтування та вбивство лікарки на роботі', '2024-08-19 15:02'),
    ('Продовжила рятувати навіть після смерті: у Львові трансплант-координаторка стала доноркою органів', '2024-08-19 14:52'),
    ('У США заперечили, що блокують дозвіл на удари ракетами Storm Shadow по території рф', '2024-08-19 14:43'),
    ('Все буде UA!: «Укрпошта» випустила марку до Дня Незалежності', '2024-08-19 14:11'),
    ('Легалізацію медичного канабісу схвалюють понад 40% українців: найбільше — люди віком 50-60 років', '2024-08-19 14:09'),
    ('Німеччина надає Україні новий пакет військової допомоги: у ньому — IRIS-T, артснаряди та дрони', '2024-08-19 13:35'),
    ('Рівень енергоспоживання вже зріс на тлі спеки. Електрику імпортують із 5 країн — «Укренерго»', '2024-08-19 13:35')
]

# Вставка даних до таблиці
cursor.executemany('''
INSERT INTO news (title, date) VALUES (?, ?)
''', news_data)

# Збереження змін
conn.commit()

# Закриття з'єднання з базою даних
conn.close()