import asyncio
import time


async def do_something_async():
    await asyncio.sleep(2)
    return "Асинхронне завдання завершено"


start = time.time()
asyncio.run(do_something_async())
end = time.time()

print(f"Асинхронне виконання завершено за {end - start:.2f} секунд")
