import asyncio
import aiopg

DSN = "dbname={назва} user={ім’я} password={пароль} host=127.0.0.1"

async def go():
    async with aiopg.create_pool(DSN) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT 1")
                ret = await cur.fetchone()
                print(ret)

asyncio.run(go())