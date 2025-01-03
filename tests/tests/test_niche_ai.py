#!/usr/bin/env python3
"""
Basic tests for Niche-Aii functionality.
"""

import unittest
from src.leonardo import LeonardoAI

class TestNicheAI(unittest.TestCase):
    def test_leonardo_creation(self):
        leo = LeonardoAI("Leonardo")
        self.assertEqual(leo.ai_id, "Leonardo")
        self.assertEqual(leo.art_counter, 0)

if __name__ == '__main__':
    unittest.main()
