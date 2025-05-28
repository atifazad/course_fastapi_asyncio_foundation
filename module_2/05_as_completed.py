# Thi script demonstrates the use of `asyncio.as_completed()`
# to run multiple asynchronous tasks concurrently and process their results as they complete.
# This is useful when you want to handle results in the order of completion rather than the order of submission.

import asyncio
import time


async def coro_1():
    print("Coro 1 started.")
    await asyncio.sleep(5)
    print("Coro 1 completed.")
    return "Coro 1 result"


async def coro_2():
    print("Coro 2 started.")
    await asyncio.sleep(1)
    print("Coro 2 completed.")
    return "Coro 2 result"


async def coro_3():
    print("Coro 3 started.")
    await asyncio.sleep(3)
    print("Coro 3 completed.")
    return "Coro 3 result"


async def main():
    print("Running tasks concurrently with as_completed:")

    start_time = time.perf_counter()

    tasks = [
        asyncio.create_task(coro_1()),
        asyncio.create_task(coro_2()),
        asyncio.create_task(coro_3()),
    ]

    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        print(f"Task completed with result: {result}")

    end_time = time.perf_counter()

    print(f"All tasks completed in {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
