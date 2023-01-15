from azure.storage.queue import (
        QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)

import os, uuid

connect_str = "-"

queue_name = "queue-lorcti-proj"
queue_client = QueueClient.from_connection_string(connect_str, queue_name)

messages = [
        "Un videoclip a fost incarcat cu succes!"
]

for message in messages:
    print("Adding message: " + message)
    queue_client.send_message(message)