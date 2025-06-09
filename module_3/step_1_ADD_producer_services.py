import asyncio
import random


notification_queue = asyncio.Queue()    # A shared queue

user_emails = [
    "alice@example.com",
    "bob@example.com",
    "carol@example.com",
    "dave@example.com"
]


async def job_service():
    while True:
        await asyncio.sleep(random.uniform(1, 3))
        job = {"type": "job_posted", "user": random.choice(user_emails)}
        print(f"[JobService] New job relevant to {job["user"]}")
        await notification_queue.put(job)


async def message_service():
    while True:
        await asyncio.sleep(random.uniform(2, 4))
        message = {"type": "recruiter_message",
                   "user": random.choice(user_emails)}
        print(
            f"[MessageService] Recruiter sent a message to {message["user"]}")
        await notification_queue.put(message)


async def application_service():
    while True:
        await asyncio.sleep(random.uniform(3, 5))
        update = {"type": "application_status_change",
                  "user": random.choice(user_emails)}
        print(
            f"[ApplicationService] Application status changed for {update["user"]}")
        await notification_queue.put(update)


async def main():
    producers = [
        asyncio.create_task(job_service()),
        asyncio.create_task(message_service()),
        asyncio.create_task(application_service()),
    ]

    await asyncio.gather(*producers)

if __name__ == "__main__":
    asyncio.run(main())
