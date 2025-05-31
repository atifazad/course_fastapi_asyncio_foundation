# Consider that we have to scrape data from three websites.
# Data from three websites can be scraped independent of each other.
# This is a perfect scenario for concurrent tasks.


import asyncio
import time


async def scrape_data_from_website_1():
    print(f"Starting to scrape website 1")
    await asyncio.sleep(.9)
    print(f"Done scraping website 1")


async def scrape_data_from_website_2():
    print(f"Starting to scrape website 2")
    await asyncio.sleep(.5)
    print(f"Done scraping website 2")


async def scrape_data_from_website_3():
    print(f"Starting to scrape website 3")
    await asyncio.sleep(.6)
    print(f"Done scraping website 3")


async def main():
    print(f"Running tasks concurrently...")
    start_time = time.perf_counter()

    task_1 = asyncio.create_task(scrape_data_from_website_1())
    task_2 = asyncio.create_task(scrape_data_from_website_2())
    task_3 = asyncio.create_task(scrape_data_from_website_3())

    await task_1
    await task_2
    await task_3

    end_time = time.perf_counter()
    print(
        f"Total time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())


# OUTPUT:
# Running tasks concurrently...
# Starting to scrape website 1
# Starting to scrape website 2
# Starting to scrape website 3
# Done scraping website 2
# Done scraping website 3
# Done scraping website 1
# Total time: 0.90 seconds
