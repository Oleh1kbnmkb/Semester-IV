import asyncio
import aiofiles

async def read_file(file_name):
    async with aiofiles.open(file_name, mode='r') as file:
        content = await file.read()
        print(f"Read {file_name}")
        return content

async def write_file(file_name, content):
    async with aiofiles.open(file_name, mode='w') as file:
        await file.write(content)
        print(f"Written to {file_name}")

async def main():
    tasks = [read_file(f"file_{i}.txt") for i in range(1, 4)]
    contents = await asyncio.gather(*tasks)

    for i, content in enumerate(contents):
        await write_file(f"output_{i + 1}.txt", content)

asyncio.run(main())