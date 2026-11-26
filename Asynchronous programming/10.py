import asyncio

async def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    await asyncio.sleep(1)
    print("Factorial of", n, "=", fact)

async def main():
    await asyncio.gather(
        factorial(5),
        factorial(4),
        factorial(3)
    )

asyncio.run(main())
