import time


# A regular function (synchronous / blocking)
def greet_sync():
    print("Starting sync greet...")
    time.sleep(2)  # Blocking call
    print("Hello, Sync World!")


if __name__ == "__main__":
    greet_sync()
