import asyncio

async def check_even_odd(n):
    await asyncio.sleep(1)

    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")

async def main():
    await asyncio.gather(
        check_even_odd(10),
        check_even_odd(15),
        check_even_odd(20)
    )

asyncio.run(main())
