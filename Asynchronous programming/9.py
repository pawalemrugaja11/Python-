import asyncio

async def greeting(name):
    print("Hello", name)
    await asyncio.sleep(2)
    print("Good Morning", name)

async def main():
    await asyncio.gather(
        greeting("Rahul"),
        greeting("Amit"),
        greeting("Sneha")
    )

asyncio.run(main())
