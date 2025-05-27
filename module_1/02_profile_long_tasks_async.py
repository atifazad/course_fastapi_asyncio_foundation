# This script demonstrates how to run multiple long-running tasks concurrently using Python's asyncio library.
# It shows that asynchronous tasks can be executed in parallel, reducing the total execution time compared to running them sequentially.
# Compare this with the synchronous version in `02_profile_long_tasks_sync.py` where tasks are run one after another.

import asyncio
import time


# Asynchronous function to simulate a long-running task
async def long_task(task_id):
    print(f"Task {task_id} started.")
    # Simulate a non-blocking long-running task
    await asyncio.sleep(2)
    print(f"Task {task_id} completed.")


async def main():
    start_time = time.perf_counter()
    await asyncio.gather(
        long_task(1),
        long_task(2),
        long_task(3),
        long_task(4),
    )
    end_time = time.perf_counter()
    print(
        f"Asynchronous function completed in {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())


# OUTPUT:
# **With a single task:**
# Task 1 started.
# Task 1 completed.
# Asynchronous function completed in 2.00 seconds

# **With two tasks:**
# Task 1 started.
# Task 2 started.
# Task 1 completed.
# Task 2 completed.
# Asynchronous function completed in 2.00 seconds

# **With four tasks:**
# Task 1 started.
# Task 2 started.
# Task 3 started.
# Task 4 started.
# Task 1 completed.
# Task 2 completed.
# Task 3 completed.
# Task 4 completed.
# Asynchronous function completed in 2.00 seconds

# Due to the nature of asyncio, the tasks run concurrently,
# and the total time taken is approximately equal to the time taken by the longest task.
# In this case, since all tasks take 2 seconds, the total time is 2 seconds.
