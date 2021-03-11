import os

from dotenv import load_dotenv
load_dotenv()

__all__ = [
    "RESPOND_TO_GROUP_CHATS", "RESPOND_TO_GROUP_CHATS_PRIVATE", "REPLY_TO_GROUP_WHEN_MENTIONED",
    "RECOMMENDED_YOUTUBE_VIDEOS", "MY_PHONE_NUMBER", "RESPOND_TO_UNKNOWN",
]

RESPOND_TO_GROUP_CHATS = False  # Respond to group chats
# Respond to group chats privately - If False, responds in group chat to the person; If True, responds privately to
# the person.
RESPOND_TO_GROUP_CHATS_PRIVATE = False
# REPLY_TO_GROUP_WHEN_MENTIONED DOESN'T WORK!!! Please submit an idea or solution to this problem
REPLY_TO_GROUP_WHEN_MENTIONED = False  # Only reply if mentioned in a message
RESPOND_TO_UNKNOWN = False  # Respond to non-saved users

RECOMMENDED_YOUTUBE_VIDEOS = [
    "https://youtu.be/DKlUPmdxyp0",  # So Many Tabs
    "https://youtu.be/hCut9HiQKl0",  # Algorithmen verstehen
    "https://youtu.be/rO37rz1dhkQ",  # The Morpheus Vlogs
]

# Your phone number (without spaces and prefixes, example: 4917612345678)
MY_PHONE_NUMBER = os.getenv("WA_PHONE_NUMBER")
