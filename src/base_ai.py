#!/usr/bin/env python3
"""
base_ai.py

Provides a base class (AIBase) for all AI agents.
"""

import queue
import time

class Message:
    """
    Represents a communication between AIs.
    """

    def __init__(self, sender_id, recipient_id, content):
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.content = content
        self.timestamp = time.time()

    def __str__(self):
        return (
            f"[Message] From {self.sender_id} to {self.recipient_id} | "
            f"Content: {self.content} | "
            f"Time: {self.timestamp}"
        )


class AIBase:
    """
    Base AI class with common logic for message handling.
    """

    def __init__(self, ai_id):
        self.ai_id = ai_id
        self.inbox = queue.Queue()
        self.log = []

    def receive_message(self, message):
        self.inbox.put(message)

    def process_inbox(self):
        while not self.inbox.empty():
            msg = self.inbox.get()
            self.log_message(msg)
            self.handle_message(msg)

    def handle_message(self, message):
        """
        Default action on receiving a message. 
        Override in subclasses for custom behavior.
        """
        print(f"[{self.ai_id}] Received: {message}")

    def send_message(self, recipient_ai, content):
        msg = Message(self.ai_id, recipient_ai.ai_id, content)
        recipient_ai.receive_message(msg)
        print(f"[{self.ai_id}] Sent to {recipient_ai.ai_id}: '{content}'")

    def log_message(self, message):
        self.log.append((message.sender_id, message.recipient_id, message.content))

    def run_cycle(self, ai_list):
        """
        Process messages once per 'hour' or simulation step.
        """
        self.process_inbox()
