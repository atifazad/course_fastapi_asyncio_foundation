# THIS SHOULD BE AVOIDED
# This example demonstrates how a blocking task can block the event loop,
# preventing other asynchronous tasks from running concurrently.

import time
import asyncio


# A blocking function that simulates a long-running task
def blocking_task():
    time.sleep(5)  # Simulate a blocking task


# Asynchronous function that calls the blocking task
async def async_task_1():
    print("Task 1 started.")
    blocking_task()
    print("Task 1 completed.")


# Asynchronous function - non-blocking
async def async_task_2():
    print("Task 2 started.")
    await asyncio.sleep(2)  # Simulate a non-blocking task
    print("Task 2 completed.")


# Asynchronous function - non-blocking
async def async_task_3():
    print("Task 3 started.")
    await asyncio.sleep(2)  # Simulate a non-blocking task
    print("Task 3 completed.")


async def main():
    # Run all tasks concurrently
    # Note: The blocking_task will block the event loop
    # async_task_2 and async_task_3 will not run until blocking_task is completed
    await asyncio.gather(
        async_task_1(),
        async_task_2(),
        async_task_3(),
    )

if __name__ == "__main__":
    start_time = time.perf_counter()
    # debug=True is used to enable debug mode in asyncio
    # This helps in identifying issues with the event loop
    asyncio.run(main(), debug=True)
    end_time = time.perf_counter()
    print(f"Async function completed in {end_time - start_time:.2f} seconds")


# OUTPUT:
# Task 1 started.
# Task 1 completed.
# Task 2 started.
# Task 3 started.
# Task 2 completed.
# Task 3 completed.
# Async function completed in 7.01 seconds

# Had we not used the blocking_task, the output would have been:
# Task 1 started.
# Task 2 started.
# Task 3 started.
# Task 1 completed.
# Task 2 completed.
# Task 3 completed.
# Async function completed in 5.00 seconds
