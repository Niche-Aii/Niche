#!/usr/bin/env python3
"""
main.py

Entry point for the Niche-Aii simulation. Creates all four AIs:
Leonardo, Raphael, Michelangelo, Donatello, then runs them for
multiple steps.
"""

import time
from .leonardo import LeonardoAI
from .raphael import RaphaelAI
from .michelangelo import MichelangeloAI
from .donatello import DonatelloAI

SIMULATION_STEPS = 5
STEP_DELAY = 0.5  # seconds

def run_simulation():
    # Instantiate the AI agents
    leonardo = LeonardoAI("Leonardo")
    raphael = RaphaelAI("Raphael")
    michelangelo = MichelangeloAI("Michelangelo")
    donatello = DonatelloAI("Donatello")

    all_ais = [leonardo, raphael, michelangelo, donatello]

    # Optionally, send a kickoff message to Leonardo (or do nothing)
    raphael.send_message(leonardo, "Please create art this hour.")

    print("\n--- Starting Niche-Aii Simulation ---\n")

    # Run the simulation for a certain number of steps (e.g., 5 hours)
    for step in range(1, SIMULATION_STEPS + 1):
        print(f"=== Hour {step} ===\n")
        for ai in all_ais:
            ai.run_cycle(all_ais)
        time.sleep(STEP_DELAY)

    print("\n--- Simulation Complete ---\n")
    print("Valuation Records in Donatello:")
    for record in donatello.valuation_records:
        print("  ", record)

if __name__ == "__main__":
    run_simulation()
