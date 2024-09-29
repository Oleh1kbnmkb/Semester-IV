import httpx
import asyncio


async def fetch_wikipedia_page(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text


async def main():
    wikipedia_url = "https://uk.wikipedia.org/wiki/"
    languages = ["Python", "Java", "JavaScript", "C++", "C#", "Ruby", "C", "HTML"]
    wikipedia_urls = [wikipedia_url + i for i in languages]
    tasks = [fetch_wikipedia_page(url) for url in wikipedia_urls]
    wikipedia_pages = await asyncio.gather(*tasks)
    for page in wikipedia_pages:
        print(page[:500])


asyncio.run(main())

