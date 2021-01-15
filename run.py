import textwrap
import time

from openwa import WhatsAPIDriver
from openwa.objects.chat import Chat
from openwa.objects.message import Message

driver = WhatsAPIDriver()


def run():
    print("Waiting for QR")
    print("Bot started")

    driver.subscribe_new_messages(NewMessageObserver())
    print("Waiting for new messages...")

    """ Locks the main thread while the subscription in running """
    while True:
        time.sleep(60)


class NewMessageObserver:
    def on_message_received(self, new_messages):
        for message in new_messages:  # type: Message
            sender = message.sender
            chat: Chat = sender.get_chat()
            
            msg = f"""
            Hallo {sender.short_name}!
            
            Ab sofort bin ich über Signal erreichbar!
            Bitte schreib mir ab sofort über Signal. Es ist einfach zu benutzen, kann schnell installiert werden und
            trackt dich nicht wie Whatsapp.
            
            Android: https://bit.ly/download-signal
            iPhone: https://bit.ly/signal-app
            
            Schreibe deine Nachricht bei Signal bitte nochmal, da die Whatsapp-Nachrichten ab sofort nur noch sehr
            spät von mir gelesen werden.
            Hier ist auch noch ein Video von jemandem der Experte ist was IT und Hacking angeht: https://youtu.be/rO37rz1dhkQ
            
            Ich freue mich auf dich bei Signal :)
            """
            msg = textwrap.dedent(msg)
            chat.send_message(msg)
            
            print(f"Notified user {sender.formatted_name}")


if __name__ == "__main__":
    run()
