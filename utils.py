import textwrap
from typing import *

from openwa import Contact
from openwa.objects.message import Message

from settings import *

__all__ = [
    "create_message", "is_phone_number_mentioned", "am_i_mentioned"
]


def create_message(sender: Optional[Contact] = None) -> str:
    if sender:
        hello_message = f"Hallo {sender.short_name}" if sender.short_name else ""
    else:
        hello_message = ""
        
    recommended_videos_list = "* " + "\n* ".join(RECOMMENDED_YOUTUBE_VIDEOS)
    
    message = f"""
    {hello_message}!

    Bitte schreib mir ab sofort über Signal. Es ist einfach zu benutzen, kann schnell installiert werden und
    trackt dich nicht wie Whatsapp.

    Android: https://bit.ly/download-signal
    iPhone: https://bit.ly/signal-app

    Schreibe deine Nachricht bei Signal bitte nochmal, da ich auf Whatsapp verzichte.
    
    Hier sind ein paar Videos von Leuten, die sich sehr gut im Bereich Privatspähre, IT und Technik auskennen:
    
    {recommended_videos_list}

    Ich freue mich auf dich bei Signal :)
    """
    message = textwrap.dedent(message)
    
    return message


def is_phone_number_mentioned(message: Message, user_id: str) -> bool:
    mention_string = f"@{user_id}"
    return mention_string in message.content


def am_i_mentioned(message: Message) -> bool:
    # How to get id from author?
    return is_phone_number_mentioned(message, MY_PHONE_NUMBER)

