import aiohttp
import asyncio

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    content = await fetch_url("https://www.youtube.com/")
    print(content)

if __name__ == "__main__":
    asyncio.run(main())
