# This script demonstrates how to manage multiple concurrent asynchronous tasks using asyncio.TaskGroup.
# TaskGroup was introduced in Python 3.11.

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

    # Simulating an error
    # raise ValueError("An error occurred in coro_2")

    return "Coro 2 result"


async def coro_3():
    print("Coro 3 started.")
    await asyncio.sleep(3)
    print("Coro 3 completed.")

    return "Coro 3 result"


async def main():
    print("Running tasks concurrently with TaskGroup:")

    start_time = time.perf_counter()
    tasks = []
    try:
        async with asyncio.TaskGroup() as tg:
            tasks.append(tg.create_task(coro_1()))
            tasks.append(tg.create_task(coro_2()))
            tasks.append(tg.create_task(coro_3()))
    except* ValueError as e:
        print(f"An error occurred: {e}")

    end_time = time.perf_counter()

    for task in tasks:
        result = await task
        print(f"{result}")

    print(f"All tasks completed in {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())


# OUTPUT:
# Running tasks concurrently with TaskGroup:
# Coro 1 started.
# Coro 2 started.
# Coro 3 started.
# Coro 2 completed.
# Coro 3 completed.
# Coro 1 completed.
# Coro 1 result
# Coro 2 result
# Coro 3 result
# All tasks completed in 5.00 seconds
