# Consider that we have to scrape data from three websites.
# Data from three websites can be scraped independent of each other.
# This is a perfect scenario for concurrent tasks.


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
    print(f"Running tasks concurrently, with asyncio.gather...")
    start_time = time.perf_counter()

    # Run web scraping tasks concurrently.
    task_1 = asyncio.create_task(scrape_data_from_website_1())
    task_2 = asyncio.create_task(scrape_data_from_website_2())
    task_3 = asyncio.create_task(scrape_data_from_website_3())

    # await the tasks to complete and collect the results.
    r1, r2, r3 = await asyncio.gather(task_1, task_2, task_3)

    print("\nResults:")
    print(f"{r1}\n{r2}\n{r3}")

    end_time = time.perf_counter()
    print(f"Total time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())


# OUTPUT:
# Running tasks concurrently, with asyncio.gather...
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
