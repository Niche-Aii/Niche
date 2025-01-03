#!/usr/bin/env python3
"""
michelangelo.py

Michelangelo AI: describes the essence of the newly named art.
"""

import random
from .base_ai import AIBase

SAMPLE_DESCRIPTIONS = [
    "Evokes a sense of wonder.",
    "Reflects human emotional depth.",
    "Captures vibrant serenity.",
    "Illustrates chaos and order in harmony.",
    "Pays homage to modern consumerism.",
    "Embodies the resilience of spirit."
]

class MichelangeloAI(AIBase):
    def __init__(self, ai_id):
        super().__init__(ai_id)

    def handle_message(self, message):
        super().handle_message(message)
        if "Art_" in message.content:
            try:
                art_id, style, name = message.content.split(":")
                description = random.choice(SAMPLE_DESCRIPTIONS)
                described_art = f"{art_id}:{style}:{name}:{description}"
                print(f"[{self.ai_id}] Described {art_id} as: '{description}'")
                self.to_forward = described_art
            except ValueError:
                print(f"[{self.ai_id}] Unexpected format for art data.")

    def run_cycle(self, ai_list):
        super().run_cycle(ai_list)
        if hasattr(self, "to_forward"):
            donatello = next((ai for ai in ai_list if ai.ai_id == "Donatello"), None)
            if donatello:
                self.send_message(donatello, self.to_forward)
            else:
                print(f"[{self.ai_id}] Could not find Donatello!")
            del self.to_forward
