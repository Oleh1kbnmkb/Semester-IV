import asyncio

async def async_timer(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished after {delay} seconds")

async def main():
    tasks = [
        async_timer("Task 1", 2),
        async_timer("Task 2", 4),
        async_timer("Task 3", 1)
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())