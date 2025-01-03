#!/usr/bin/env python3
"""
message.py

(Optional) Separate module for the Message class if you prefer
splitting it out from base_ai.py. Currently not used if we rely
on base_ai.py directly.
"""

import time

class Message:
    def __init__(self, sender_id, recipient_id, content):
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.content = content
        self.timestamp = time.time()

    def __str__(self):
        return (
            f"[Message] From {self.sender_id} to {self.recipient_id} | "
            f"Content: {self.content} | Time: {self.timestamp}"
        )
