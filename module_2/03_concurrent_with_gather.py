# This script demonstrates how to run multiple asynchronous tasks sequentially using `asyncio.gether`.

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
    print("Running tasks concurrently with gather:")

    start_time = time.perf_counter()
    task_1 = asyncio.create_task(coro_1())
    task_2 = asyncio.create_task(coro_2())
    task_3 = asyncio.create_task(coro_3())
    r1, r2, r3 = await asyncio.gather(
        task_1, task_2, task_3
    )
    end_time = time.perf_counter()

    print(f"Results: \n {r1}\n {r2}\n {r3}")
    print(f"All tasks completed in {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())


# OUTPUT:
# Running tasks concurrently with gather:
# Coro 1 started.
# Coro 2 started.
# Coro 3 started.
# Coro 2 completed.
# Coro 3 completed.
# Coro 1 completed.
# Results:
#  Coro 1 result
#  Coro 2 result
#  Coro 3 result
# All tasks completed in 5.00 seconds

# The total execution time is determined by the longest task (coro_1),
# which runs concurrently with the other tasks.
