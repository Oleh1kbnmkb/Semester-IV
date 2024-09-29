import httpx
import asyncio

async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://goiteens.com/')
        print(response.text)

asyncio.run(fetch_data())