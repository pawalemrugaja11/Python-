import asyncio

async def addition(a, b):
    await asyncio.sleep(1)
    print("Addition =", a + b)

async def main():
    await asyncio.gather(
        addition(10, 20),
        addition(30, 40),
        addition(50, 60)
    )

asyncio.run(main())
