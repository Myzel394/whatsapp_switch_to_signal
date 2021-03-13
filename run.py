import logging
import time
from datetime import datetime

from constants import driver
from observer import ReplyObserver
from settings import ACTIVATE_LOGGING
from utils import log


def run():
    if ACTIVATE_LOGGING:
        logging.root.setLevel(logging.INFO)
    
    log("Initializing bot")

    driver.subscribe_new_messages(ReplyObserver())
    
    log("Waiting for new messages...")

    # Locks the main thread while the subscription in running
    while True:
        time.sleep(60)


if __name__ == "__main__":
    run()
