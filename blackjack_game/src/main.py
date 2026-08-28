#!/usr/bin/env python3
"""
Main entry point for the Blackjack game
Run this file to start the game with GUI.
"""

import os
import sys

# Add the src directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gui import main

if __name__ == "__main__":
    main()
