# Consider that we have to scrape data from three websites.
# Data from three websites can be scraped independent of each other.
# Additionally, we want to process the data as soon as
# data is retrieved from one of the website without waiting for the rest of the batch to complete.
# This is a usecase for asyncio.as_completed()

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
    print("Running tasks concurrently with as_completed:")

    start_time = time.perf_counter()

    tasks = [
        asyncio.create_task(scrape_data_from_website_1()),
        asyncio.create_task(scrape_data_from_website_2()),
        asyncio.create_task(scrape_data_from_website_3()),
    ]

    print("\nResults:")
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        print(f"{result}")

    end_time = time.perf_counter()

    print(f"Total time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
