import asyncio

async def download(file):
    print("Downloading", file)
    await asyncio.sleep(2)
    print(file, "Downloaded Successfully")

async def main():
    await asyncio.gather(
        download("File1"),
        download("File2"),
        download("File3")
    )

asyncio.run(main())
