# This script demonstrates how to run multiple asynchronous tasks sequentially using `await`.
# Compare this with the concurrent execution in `02_concurrent_with_tasks.py`and 03_concurrent_with_gather.py

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
    print("Running tasks sequentially with await:")

    start_time = time.perf_counter()
    r1 = await coro_1()
    r2 = await coro_2()
    r3 = await coro_3()
    end_time = time.perf_counter()

    print(f"Results: \n {r1}\n {r2}\n {r3}")
    print(f"All tasks completed in {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())


# OUTPUT:
# Running tasks sequentially with await:
# Task 1 started.
# Task 1 completed.
# Task 2 started.
# Task 2 completed.
# Task 3 started.
# Task 3 completed.
# All tasks completed in 9.00 seconds


# NOTE: Due to the sequential execution of async tasks,
# the total execution time is the sum of the individual task durations.
