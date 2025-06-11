import asyncio


# Shared counters
unsafe_counter = 0
safe_counter = 0


async def unsafe_increment(task_id):
    global unsafe_counter
    current = unsafe_counter
    print(f"Task {task_id} read counter: {current}")
    await asyncio.sleep(.5)   # Simulate processing time
    unsafe_counter = current + 1
    print(f"Task {task_id} incremented counter to: {unsafe_counter}")


async def safe_increment(task_id, lock):
    global safe_counter
    async with lock:  # Acquire the lock
        current = safe_counter
        print(f"Task {task_id} read counter: {current}")
        await asyncio.sleep(.5)   # Simulate processing time
        safe_counter = current + 1
        print(f"Task {task_id} incremented counter to: {safe_counter}")


async def main():
    lock = asyncio.Lock()

    print("Unsafe incrementing:")
    unsafe_increment_tasks = [asyncio.create_task(
        unsafe_increment(i)) for i in range(10)]
    await asyncio.gather(*unsafe_increment_tasks)
    print(f"\nFinal UNSAFE counter value: {unsafe_counter}")

    print("\n\nSafe incrementing:")
    safe_increment_tasks = [asyncio.create_task(
        safe_increment(i, lock)) for i in range(10)]
    await asyncio.gather(*safe_increment_tasks)
    print(f"\nFinal SAFE counter value: {safe_counter}")

if __name__ == "__main__":
    asyncio.run(main())
