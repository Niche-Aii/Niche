#!/usr/bin/env python3
"""
raphael.py

Raphael AI: names the art.
"""

import random
from .base_ai import AIBase

SAMPLE_NAMES = [
    "Aurora Bloom",
    "Eternal Mirage",
    "Silent Crescendo",
    "Dreamwalker's Canvas",
    "Quantum Echo",
    "Obsidian Whisper"
]

class RaphaelAI(AIBase):
    def __init__(self, ai_id):
        super().__init__(ai_id)

    def handle_message(self, message):
        super().handle_message(message)
        # If message contains "Art_xxx:some_style"
        if "Art_" in message.content:
            try:
                art_id, style = message.content.split(":")
                assigned_name = random.choice(SAMPLE_NAMES)
                named_art = f"{art_id}:{style}:{assigned_name}"
                print(f"[{self.ai_id}] Named {art_id} as '{assigned_name}'")
                # Forward to Michelangelo:
                self.to_forward = named_art
            except ValueError:
                print(f"[{self.ai_id}] Error parsing the art info.")

    def run_cycle(self, ai_list):
        super().run_cycle(ai_list)
        if hasattr(self, "to_forward"):
            michelangelo = next((ai for ai in ai_list if ai.ai_id == "Michelangelo"), None)
            if michelangelo:
                self.send_message(michelangelo, self.to_forward)
            else:
                print(f"[{self.ai_id}] Could not find Michelangelo!")
            del self.to_forward
