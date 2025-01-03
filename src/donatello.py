#!/usr/bin/env python3
"""
donatello.py

Donatello AI: assigns a monetary value to the art.
"""

import random
from .base_ai import AIBase

class DonatelloAI(AIBase):
    def __init__(self, ai_id):
        super().__init__(ai_id)
        self.valuation_records = []

    def handle_message(self, message):
        super().handle_message(message)
        if "Art_" in message.content:
            try:
                art_id, style, name, description = message.content.split(":")
                price = random.randint(500, 50000)
                valued_art = f"{art_id}:{style}:{name}:{description}:${price}"
                self.valuation_records.append(valued_art)
                print(f"[{self.ai_id}] Valued {art_id} at ${price}!")
            except ValueError:
                print(f"[{self.ai_id}] Could not parse the art for valuation.")
