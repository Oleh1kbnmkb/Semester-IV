import aiohttp
import aiosqlite
import asyncio

API_URL = 'https://jsonplaceholder.typicode.com/users'


async def fetch_users_from_api():
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as response:
            if response.status == 200:
                users = await response.json()
                return users
            else:
                print(f"Помилка запиту: {response.status}")
                return None


async def get_db_connection():
    conn = await aiosqlite.connect('users.db')
    return conn


async def create_table():
    conn = await get_db_connection()
    async with conn.cursor() as cur:
        await cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        await conn.commit()
    await conn.close()


async def add_user(name, email):
    conn = await get_db_connection()
    await conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    await conn.commit()
    await conn.close()


async def delete_user(user_id):
    conn = await get_db_connection()
    await conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    await conn.commit()
    await conn.close()


async def fetch_users_from_db():
    conn = await get_db_connection()
    async with conn.execute("SELECT * FROM users") as cursor:
        users = await cursor.fetchall()
    await conn.close()
    return users


async def main():
    await create_table()
    users_from_api = await fetch_users_from_api()

    if users_from_api:
        print("Користувачі з API:")
        for user in users_from_api:
            print(f"Name: {user['name']}, Email: {user['email']}")
            await add_user(user['name'], user['email'])

    users_from_db = await fetch_users_from_db()
    print("\nКористувачі з бази даних:")
    for user in users_from_db:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

    await delete_user(1)
    print("\nКористувач з ID = 1 видалений.")

    users_from_db_after_deletion = await fetch_users_from_db()
    print("\nКористувачі з бази даних після видалення:")
    for user in users_from_db_after_deletion:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

if __name__ == "__main__":
    asyncio.run(main())
