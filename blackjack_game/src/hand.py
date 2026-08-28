"""
Hand class for Blackjack game
Manages a hand of cards and calculates the score.
"""

from card import Card


class Hand:
    """
    Represents a hand of cards held by a player or dealer.
    
    Methods:
        add_card(card): Add a card to the hand
        calculate_score(): Calculate the total score (Ace = 1 or 11)
        is_bust(): Check if the hand score exceeds 21
        is_blackjack(): Check if the hand is a blackjack (Ace + 10-value card)
        get_cards(): Return the list of cards
        clear(): Clear all cards from the hand
    """
    
    def __init__(self):
        """Initialize an empty hand."""
        self.cards = []
    
    def add_card(self, card):
        """
        Add a card to the hand.
        
        Args:
            card (Card): The card to add
        """
        self.cards.append(card)
    
    def get_cards(self):
        """Return the list of cards in the hand."""
        return self.cards.copy()
    
    def clear(self):
        """Clear all cards from the hand."""
        self.cards = []
    
    def calculate_score(self):
        """
        Calculate the total score of the hand.
        Aces are worth 11 unless that would cause a bust, then they're worth 1.
        
        Returns:
            int: The total score of the hand
        """
        score = 0
        aces = 0
        
        for card in self.cards:
            if card.rank == 'ace':
                score += 11
                aces += 1
            else:
                score += card.value
        
        # Adjust for aces if score is over 21
        while score > 21 and aces > 0:
            score -= 10  # Change ace from 11 to 1
            aces -= 1
        
        return score
    
    def is_bust(self):
        """
        Check if the hand score exceeds 21.
        
        Returns:
            bool: True if hand is bust, False otherwise
        """
        return self.calculate_score() > 21
    
    def is_blackjack(self):
        """
        Check if the hand is a blackjack (Ace + 10-value card with 2 cards).
        
        Returns:
            bool: True if hand is blackjack, False otherwise
        """
        if len(self.cards) != 2:
            return False
        
        score = self.calculate_score()
        has_ace = any(card.rank == 'ace' for card in self.cards)
        has_ten_value = any(card.value == 10 for card in self.cards)
        
        return has_ace and has_ten_value and score == 21
    
    def num_cards(self):
        """Return the number of cards in the hand."""
        return len(self.cards)
    
    def __str__(self):
        if not self.cards:
            return "Empty hand"
        return ", ".join(str(card) for card in self.cards)
    
    def __len__(self):
        return len(self.cards)
