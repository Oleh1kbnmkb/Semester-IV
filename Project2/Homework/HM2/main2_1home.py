import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Fetching {url}...")
            return await response.text()

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/posts"
    ]
    tasks = [fetch_url(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    for response in responses:
        print(f"Response length: {len(response)}")

asyncio.run(main())