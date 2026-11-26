import asyncio

async def multiply(a, b):
    print("Multiplication Started")
    await asyncio.sleep(2)
    print("Multiplication =", a * b)

asyncio.run(multiply(10, 5))
