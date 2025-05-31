# Some of the operations are naturally sequential. Take this example...
#
# 1. Retrieve the product data from an API
# 2. Validate the data
# 3. Save the data into database
#
# We must execute these steps in order as every next step depends on the previous one.
# Code below demostrates how to perform such operations with asyncio.


import asyncio
import time


async def get_data(url):
    print("get_data started")
    await asyncio.sleep(.5)
    print("get_data completed")

    return "response_data_from_url"


async def validate(data):
    print("validate started.")
    await asyncio.sleep(.2)
    print("validate completed.")

    return data     # return the validated_data


async def save_in_db(validated_data):
    print("save_in_db started.")
    await asyncio.sleep(.3)
    print("save_in_db completed.")

    return True


async def main():
    print("Retrieving, validating and saving product data sequentially...")

    start_time = time.perf_counter()

    # Sequentially retrieve, validate and save data.
    data = await get_data(url="http:api.example.com/product/1")
    validated_data = await validate(data)
    await save_in_db(validated_data)

    end_time = time.perf_counter()

    print(f"Product saved in {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())


# OUTPUT:
# Retrieving, validating and saving product data sequentially...
# get_data started
# get_data completed
# validate started.
# validate completed.
# save_in_db started.
# save_in_db completed.
# Product saved in 1.00 seconds


# NOTE: Due to the sequential execution of async tasks,
# the total execution time is the sum of the individual task durations.
