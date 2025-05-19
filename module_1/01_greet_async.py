import asyncio


# Coroutine (async / non-blocking function)
async def greet_async():
    print("Starting async greet...")
    await asyncio.sleep(2)  # Non-blocking call
    print("Hello, Async World!")

if __name__ == "__main__":
    asyncio.run(greet_async())
