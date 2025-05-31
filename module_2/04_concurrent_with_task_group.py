# Consider that we have to scrape data from three websites.
# Data from three websites can be scraped independent of each other.
# However, after data retrieval we want to merge analytics data from each website.
# This is a use case for concurrent tasks but if one of the task fails,
# it makes sense to cancel the rest of the tasks as well.
# asyncio.TaskGourp() provides this kind of task management out of the box.


import asyncio
import time


async def scrape_data_from_website_1():
    print(f"Starting to scrape website 1")
    await asyncio.sleep(.9)
    print(f"Done scraping website 1")

    return "website_1_data"


async def scrape_data_from_website_2():
    print(f"Starting to scrape website 2")
    await asyncio.sleep(.5)
    print(f"Done scraping website 2")

    return "website_2_data"


async def scrape_data_from_website_3():
    print(f"Starting to scrape website 3")
    await asyncio.sleep(.6)
    print(f"Done scraping website 3")

    return "website_3_data"


async def main():
    print("Running tasks concurrently with TaskGroup:")

    start_time = time.perf_counter()
    # Run web scraping tasks concurrently as a batch with TaskGroup.
    tasks = []
    try:
        async with asyncio.TaskGroup() as tg:
            tasks.append(tg.create_task(scrape_data_from_website_1()))
            tasks.append(tg.create_task(scrape_data_from_website_2()))
            tasks.append(tg.create_task(scrape_data_from_website_3()))
    except* ValueError as e:
        print(f"An error occurred: {e}")

    # await tasks to collect the results.
    print("\nResults:")
    for task in tasks:
        result = await task
        print(f"{result}")

    end_time = time.perf_counter()
    print(f"Total time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())


# OUTPUT:
# Running tasks concurrently with TaskGroup:
# Starting to scrape website 1
# Starting to scrape website 2
# Starting to scrape website 3
# Done scraping website 2
# Done scraping website 3
# Done scraping website 1

# Results:
# website_1_data
# website_2_data
# website_3_data
# Total time: 0.90 seconds
