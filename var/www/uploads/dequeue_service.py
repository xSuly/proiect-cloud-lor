from azure.storage.queue import (
        QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)

import os, uuid
from base64 import b64decode

connect_str = "-"

queue_name = "queue-lorcti-proj"
queue_client = QueueClient.from_connection_string(connect_str, queue_name)

messages = queue_client.receive_messages()
for message in messages:
    message_content = message.content

    # Daca ati adaugat mesaje din browser, implicit este selectata
    # optiunea "Encode the message body in Base64". Pentru decodare
    # folositi linia de mai jos
    # message_content = b64decode(message.content).decode("utf-8")

    print("Dequeueing message: " + message_content)
    queue_client.delete_message(message.id, message.pop_receipt)
