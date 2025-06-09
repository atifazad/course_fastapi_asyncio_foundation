import asyncio

sem = asyncio.Semaphore(5)  # Limit to N concurrent tasks


async def access_resource(id):
    async with sem:
        print(f"Task {id} is using the resource")
        await asyncio.sleep(2)
        print(f"Task {id} is done")


async def main():
    tasks = [asyncio.create_task(access_resource(i)) for i in range(10)]
    await asyncio.gather(*tasks)

asyncio.run(main())
