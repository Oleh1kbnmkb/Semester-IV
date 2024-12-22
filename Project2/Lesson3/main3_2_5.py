import asyncio
import aiomysql

async def main():
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='your_username', password='your_password',
                                      db='your_db_name')

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM your_table_name;")
            print(await cur.fetchall())

    pool.close()
    await pool.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
