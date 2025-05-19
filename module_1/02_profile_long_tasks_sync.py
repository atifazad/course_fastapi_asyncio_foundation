# This script demonstrates how synchronous (blocking) functions execute long-running tasks sequentially.
# It profiles the total time taken to run multiple tasks one after another using time.sleep to simulate work.
# Compare this with the asynchronous version in `02_profile_long_tasks_async.py` where tasks are run concurrently.

import time


# Synchronous function to simulate a long-running task
def long_task(task_id: int):
    print(f"Task {task_id} started.")
    # Simulate a blocking long-running task
    time.sleep(2)
    print(f"Task {task_id} completed.")


def main():
    start_time = time.perf_counter()
    long_task(1)
    long_task(2)
    end = time.perf_counter()
    print(f"Sync function completed in {end - start_time:.2f} seconds")


if __name__ == "__main__":
    main()


# OUTPUT:
# **With a single task:**
# Task 1 started.
# Task 1 completed.
# Sync function completed in 2.00 seconds

# **With two tasks:**
# Task 1 started.
# Task 1 completed.
# Task 2 started.
# Task 2 completed.
# Sync function completed in 4.00 seconds
#
# **With four tasks:**
# Task 1 started.
# Task 1 completed.
# Task 2 started.
# Task 2 completed.
# Task 3 started.
# Task 3 completed.
# Task 4 started.
# Task 4 completed.
# Sync function completed in 8.00 seconds

# In this case, the tasks are run sequentially (one after the other),
# and the total time taken is the sum of the time taken by each task.
