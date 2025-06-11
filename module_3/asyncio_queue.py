import asyncio


queue = asyncio.Queue()


async def producer():
    for i in range(5):
        item = f"Item {i}"
        await asyncio.sleep(0.5)    # Simulate work delay
        print(f"Producer: produced {item}")
        await queue.put(item)

    print("Producer finished producing items.")


async def consumer():
    try:
        while True:
            item = await queue.get()
            print(f"Consumer: consumed {item}")
            queue.task_done()
    except asyncio.CancelledError:
        print("Consumer cancelled, exiting...")


async def main():

    consumer_task = asyncio.create_task(consumer())

    await producer()
    await queue.join()    # Wait until all items are consumed/processed
    print("All items have been processed.")

    consumer_task.cancel()


if __name__ == '__main__':
    asyncio.run(main())
