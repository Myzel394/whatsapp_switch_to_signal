from typing import *

from openwa.objects.chat import Chat, GroupChat, UserChat
from openwa.objects.message import Message, MessageGroup

from constants import driver
import reply
from utils import log

__all__ = [
    "ReplyObserver"
]



class ReplyObserver:
    def on_message_received(self, _):
        unread: list[MessageGroup] = driver.get_unread()

        log(f"{len(unread)} new unread messages")
        
        for message_group in unread:
            chat: Union[UserChat, GroupChat] = message_group.chat
            unread_message: list[Message] = message_group.messages
            
            # If group chat, respond to all senders (if necessary)
            if isinstance(chat, GroupChat):
                reply.to_group_chat(chat, unread_message)
            else:
                # Last message must be from user, because the bot replies to it
                message = unread_message[-1]
                contact = message.sender
                
                reply.to_user_chat(contact)
