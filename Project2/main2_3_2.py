import asyncio

async def factorial(n):
    if n == 0:
        return 1
    else:
        return n * await factorial(n-1)

async def main():
    result = await factorial(10)
    print(f"Факторіал 10 = {result}")

asyncio.run(main())