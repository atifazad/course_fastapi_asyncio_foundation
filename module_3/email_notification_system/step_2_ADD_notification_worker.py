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

        await notification_queue.put(job)
        print(
            f"[JobService] New job relevant to {job["user"]}")


async def message_service():
    while True:
        await asyncio.sleep(random.uniform(2, 4))
        message = {"type": "recruiter_message",
                   "user": random.choice(user_emails)}

        await notification_queue.put(message)
        print(
            f"[MessageService] Recruiter sent a message to {message["user"]}")


async def application_service():
    while True:
        await asyncio.sleep(random.uniform(3, 5))
        update = {"type": "application_status_change",
                  "user": random.choice(user_emails)}

        await notification_queue.put(update)
        print(
            f"[ApplicationService] Application status changed for {update["user"]}")


def format_notification(event):
    if event["type"] == "job_posted":
        return {
            "to": event["user"],
            "subject": "New Job Posted",
            "body": "A new job matching your interests was posted."
        }
    elif event["type"] == "recruiter_message":
        return {
            "to": event["user"],
            "subject": "You have a new message from a recruiter",
            "body": "A recruiter has contacted you regarding a new opportunity."
        }
    elif event["type"] == "application_status_change":
        return {
            "to": event["user"],
            "subject": "Application Status Updated",
            "body": "Your job application status has been updated."
        }
    else:
        return None


async def send_email(notification, worker_id):
    print(
        f"[Worker {worker_id}] Sending email to {notification['to']}: {notification['subject']}")
    await asyncio.sleep(random.uniform(0.5, 1.5))  # simulate sending delay
    print(f"[Worker {worker_id}] Email sent to {notification['to']}")


async def notification_worker(worker_id):
    while True:
        event = await notification_queue.get()
        notification = format_notification(event)
        if notification:
            await send_email(notification, worker_id)
        notification_queue.task_done()


async def main():
    producers = [
        asyncio.create_task(job_service()),
        asyncio.create_task(message_service()),
        asyncio.create_task(application_service()),
    ]

    workers = [
        asyncio.create_task(notification_worker(i)) for i in range(3)
    ]

    await asyncio.gather(*producers, *workers)


if __name__ == "__main__":
    asyncio.run(main())
