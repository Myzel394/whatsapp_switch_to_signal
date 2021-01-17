import time

from constants import driver
from observer import ReplyObserver


def run():
    print("Waiting for QR")
    print("Bot started")

    driver.subscribe_new_messages(ReplyObserver())
    print("Waiting for new messages...")

    # Locks the main thread while the subscription in running
    while True:
        time.sleep(60)


if __name__ == "__main__":
    run()
