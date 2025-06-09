import asyncio


async def waiter(event: asyncio.Event, id: int) -> None:
    print(f"Waiter-{id}: waiting for signal...")
    await event.wait()  # Suspends here until event is set
    print(f"Waiter-{id}: got the signal! Proceeding...")


async def signaler(event: asyncio.Event) -> None:
    print("Signaler: preparing something...")
    await asyncio.sleep(2)  # Simulate work delay
    print("Signaler: done! Sending signal.")
    event.set()  # Wakes up all waiters


async def main() -> None:
    event = asyncio.Event()

    # Start 3 waiters (they will pause on event.wait())
    waiters = [asyncio.create_task(waiter(event, i)) for i in range(3)]

    # Start the signaler
    await signaler(event)

    # Wait for all waiters to finish after signal
    await asyncio.gather(*waiters)

if __name__ == "__main__":
    asyncio.run(main())
