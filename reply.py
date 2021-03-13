import logging

from openwa import Contact
from openwa.objects.chat import Chat, GroupChat
from openwa.objects.message import Message

from settings import *
from settings import ACTIVATE_LOGGING
from store import add_informed_person, should_inform_person
from utils import create_message, am_i_mentioned, format_now, log

__all__ = [
    "to_user_chat", "to_group_chat"
]


def to_user_chat(contact: Contact) -> None:
    user_chat: Chat = contact.get_chat()
    chat_id = user_chat.id
    
    if not should_inform_person(chat_id):
        log(f"Skipping {contact.name} because he/she has already been informed")
        return
    
    add_informed_person(chat_id)
    
    user_chat.send_message(create_message(contact))
    
    log(f"Messaging {contact.name}")


def to_group_chat(chat: GroupChat, unread_messages: list[Message]) -> None:
    if not RESPOND_TO_GROUP_CHATS:
        return

    if RESPOND_TO_GROUP_CHATS_PRIVATE:
        # Get all senders and reply privately
        if REPLY_TO_GROUP_WHEN_MENTIONED:
            senders = {
                message.sender
                for message in unread_messages
                if am_i_mentioned(message)
            }
            
            log(f"Replying privately {len(senders)} users because they mentioned you in group {chat.name}")
            
        else:
            senders = {
                message.sender
                for message in unread_messages
            }
            
            log(f"Replying privately {len(senders)} users because they wrote messages in group {chat.name}")
            
        for user in senders:
            to_user_chat(user)
    else:
        # Reply in group chat
        if REPLY_TO_GROUP_WHEN_MENTIONED:
            # Check if author is mentioned in any message
            for message in unread_messages:
                if am_i_mentioned(message):
                    break
            else:
                return

        log(f"Messaging group {chat.name} because someone mentioned you")
        
        chat.send_message(create_message())
