from openwa import Contact
from openwa.objects.chat import Chat, GroupChat
from openwa.objects.message import Message

from settings import *
from store import add_informed_person, should_inform_person
from utils import create_message, am_i_mentioned

__all__ = [
    "to_user_chat", "to_group_chat"
]


def to_user_chat(contact: Contact) -> None:
    user_chat: Chat = contact.get_chat()
    chat_id = user_chat.id
    
    if not should_inform_person(chat_id):
        return
    
    add_informed_person(chat_id)
    
    user_chat.send_message(create_message(contact))


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
        else:
            senders = {
                message.sender
                for message in unread_messages
            }
        
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
        
        chat.send_message(create_message())
