"""
Card class for Blackjack game
Represents a playing card with suit, rank, and value.
"""

class Card:
    """
    Represents a playing card with suit, rank, and image.
    
    Attributes:
        suit (str): The suit of the card (hearts, diamonds, clubs, spades)
        rank (str): The rank of the card (2-10, jack, queen, king, ace)
        value (int): The point value of the card (1-11)
        image_path (str): Path to the card image
    """
    
    SUITS = ['hearts', 'diamonds', 'clubs', 'spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    
    # Unicode symbols for suits
    SUIT_SYMBOLS = {
        'hearts': '♥',
        'diamonds': '♦',
        'clubs': '♣',
        'spades': '♠'
    }
    
    # Card values for Blackjack
    RANK_VALUES = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'jack': 10, 'queen': 10, 'king': 10, 'ace': 11
    }
    
    def __init__(self, suit, rank):
        """
        Initialize a card with suit and rank.
        
        Args:
            suit (str): One of 'hearts', 'diamonds', 'clubs', 'spades'
            rank (str): One of '2'-'10', 'jack', 'queen', 'king', 'ace'
        """
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}. Must be one of {self.SUITS}")
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}. Must be one of {self.RANKS}")
        
        self.suit = suit
        self.rank = rank
        self.value = self.RANK_VALUES[rank]
        self.image_path = f"assets/cards/{rank}_of_{suit}.png"
    
    def get_display_name(self):
        """Return a human-readable name for the card."""
        return f"{self.rank.capitalize()} of {self.suit.capitalize()}"
    
    def get_unicode_symbol(self):
        """Return a Unicode representation of the card."""
        rank_symbol = self.rank[0].upper() if self.rank != '10' else '10'
        suit_symbol = self.SUIT_SYMBOLS[self.suit]
        return f"[{rank_symbol}{suit_symbol}]"
    
    def __str__(self):
        return self.get_display_name()
    
    def __repr__(self):
        return f"Card('{self.suit}', '{self.rank}')"
    
    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.suit == other.suit and self.rank == other.rank
    
    def __hash__(self):
        return hash((self.suit, self.rank))
