#!/usr/bin/env python3
"""
leonardo.py

Leonardo AI: creates or "posts" new art each hour.
"""

import time
import random
from .base_ai import AIBase

SAMPLE_ART_STYLES = [
    "Cubist portrait",
    "Surrealist dreamscape",
    "Minimalist line art",
    "Impressionist landscape",
    "Abstract collage",
    "Pop art illustration"
]

class LeonardoAI(AIBase):
    def __init__(self, ai_id):
        super().__init__(ai_id)
        self.art_counter = 0

    def handle_message(self, message):
        super().handle_message(message)
        # If there's a request to create art, we can handle it here if desired.
        # For now, we just acknowledge it.

    def run_cycle(self, ai_list):
        super().run_cycle(ai_list)
        self.art_counter += 1
        art_id = f"Art_{self.art_counter:03}"
        style = random.choice(SAMPLE_ART_STYLES)
        new_art = f"{art_id}:{style}"
        print(f"[{self.ai_id}] Created new art: {new_art}")

        # Forward the art to Raphael (who names it)
        raphael = next((ai for ai in ai_list if ai.ai_id == "Raphael"), None)
        if raphael:
            self.send_message(raphael, new_art)
        else:
            print("[Leonardo] Could not find Raphael to send the art to!")
