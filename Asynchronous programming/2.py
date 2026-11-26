import asyncio

async def task1():
    print("Task 1 Started")
    await asyncio.sleep(2)
    print("Task 1 Completed")

async def task2():
    print("Task 2 Started")
    await asyncio.sleep(1)
    print("Task 2 Completed")

async def main():
    await task1()
    await task2()

asyncio.run(main())
