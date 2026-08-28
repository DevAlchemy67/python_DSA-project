"""
Deck class for Blackjack game
Manages a deck of 52 playing cards with shuffling and dealing functionality.
"""

import random
from card import Card


class Deck:
    """
    Represents a deck of 52 playing cards.
    
    Methods:
        shuffle(): Shuffle the deck
        deal_card(): Remove and return the top card
        reset(): Reset the deck to full and shuffle
        remaining(): Return number of cards remaining
    """
    
    def __init__(self, num_decks=1):
        """
        Initialize a deck with the specified number of decks.
        
        Args:
            num_decks (int): Number of decks to use (default: 1)
        """
        self.cards = []
        self.num_decks = num_decks
        self.reset()
    
    def reset(self):
        """Reset the deck to full and shuffle."""
        self.cards = []
        for _ in range(self.num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    self.cards.append(Card(suit, rank))
        self.shuffle()
    
    def shuffle(self):
        """Shuffle the deck using Fisher-Yates algorithm."""
        random.shuffle(self.cards)
    
    def deal_card(self):
        """
        Remove and return the top card from the deck.
        
        Returns:
            Card: The top card, or None if deck is empty
        """
        if len(self.cards) == 0:
            self.reset()  # Auto-reset if deck is empty
        return self.cards.pop()
    
    def remaining(self):
        """Return the number of cards remaining in the deck."""
        return len(self.cards)
    
    def is_empty(self):
        """Check if the deck is empty."""
        return len(self.cards) == 0
    
    def __len__(self):
        return len(self.cards)
    
    def __str__(self):
        return f"Deck with {len(self)} cards remaining"
