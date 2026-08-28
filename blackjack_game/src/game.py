"""
Main Blackjack game class
Manages the game logic, player actions, and win/loss detection.
"""

from deck import Deck
from hand import Hand
from card import Card


class BlackjackGame:
    """
    Main game class that manages the Blackjack game flow.
    
    Game Rules:
    - Dealer stands on 17 or higher
    - Blackjack pays 3:2
    - Player can hit or stand
    - Ace is worth 1 or 11
    
    Methods:
        start_game(): Initialize the game with a new deck and deal initial cards
        player_hit(): Deal a card to the player
        player_stand(): End player's turn
        dealer_play(): Dealer draws cards according to house rules
        determine_winner(): Determine the game outcome
        get_player_hand(): Return player's current hand
        get_dealer_hand(): Return dealer's current hand
    """
    
    def __init__(self, num_decks=1):
        """
        Initialize a new Blackjack game.
        
        Args:
            num_decks (int): Number of decks to use (default: 1)
        """
        self.deck = Deck(num_decks)
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.game_state = "idle"  # idle, dealing, player_turn, dealer_turn, game_over
        self.bet = 0
        self.player_chips = 1000
        self.result = None
    
    def start_game(self, bet=10):
        """
        Start a new game with the specified bet.
        
        Args:
            bet (int): The amount to bet (default: 10)
        
        Returns:
            bool: True if game started successfully, False otherwise
        """
        if self.game_state != "idle":
            return False
        
        if bet > self.player_chips:
            return False
        
        self.bet = bet
        self.player_chips -= bet
        self.player_hand.clear()
        self.dealer_hand.clear()
        self.game_state = "dealing"
        self.result = None
        
        # Deal initial cards
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        
        # Check for blackjack
        if self.player_hand.is_blackjack():
            if self.dealer_hand.is_blackjack():
                # Push
                self.player_chips += self.bet
                self.game_state = "game_over"
                self.result = "push"
            else:
                # Player wins with blackjack
                self.player_chips += self.bet + int(self.bet * 1.5)
                self.game_state = "game_over"
                self.result = "player_blackjack"
        else:
            self.game_state = "player_turn"
        
        return True
    
    def player_hit(self):
        """
        Deal a card to the player.
        
        Returns:
            bool: True if card was dealt, False if game is not in player_turn state
        """
        if self.game_state != "player_turn":
            return False
        
        self.player_hand.add_card(self.deck.deal_card())
        
        if self.player_hand.is_bust():
            self.game_state = "game_over"
            self.result = "player_bust"
        
        return True
    
    def player_stand(self):
        """
        End player's turn and start dealer's turn.
        
        Returns:
            bool: True if player stood, False if game is not in player_turn state
        """
        if self.game_state != "player_turn":
            return False
        
        self.game_state = "dealer_turn"
        self.dealer_play()
        return True
    
    def dealer_play(self):
        """
        Dealer draws cards according to house rules (stand on 17+).
        """
        if self.game_state != "dealer_turn":
            return
        
        while self.dealer_hand.calculate_score() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
        
        self.determine_winner()
    
    def determine_winner(self):
        """
        Determine the game outcome and update player chips.
        """
        player_score = self.player_hand.calculate_score()
        dealer_score = self.dealer_hand.calculate_score()
        
        if dealer_score > 21:
            # Dealer busts, player wins
            self.player_chips += self.bet * 2
            self.result = "dealer_bust"
        elif player_score > dealer_score:
            # Player wins
            self.player_chips += self.bet * 2
            self.result = "player_win"
        elif player_score < dealer_score:
            # Dealer wins
            self.result = "dealer_win"
        else:
            # Push
            self.player_chips += self.bet
            self.result = "push"
        
        self.game_state = "game_over"
    
    def get_player_hand(self):
        """Return player's current hand."""
        return self.player_hand
    
    def get_dealer_hand(self):
        """Return dealer's current hand."""
        return self.dealer_hand
    
    def get_player_score(self):
        """Return player's current score."""
        return self.player_hand.calculate_score()
    
    def get_dealer_score(self):
        """Return dealer's current score."""
        return self.dealer_hand.calculate_score()
    
    def get_game_state(self):
        """Return the current game state."""
        return self.game_state
    
    def get_result(self):
        """Return the game result."""
        return self.result
    
    def get_player_chips(self):
        """Return player's current chip count."""
        return self.player_chips
    
    def get_bet(self):
        """Return the current bet."""
        return self.bet
    
    def can_double_down(self):
        """Check if player can double down (has 2 cards and enough chips)."""
        return (self.game_state == "player_turn" and 
                len(self.player_hand) == 2 and 
                self.player_chips >= self.bet)
    
    def double_down(self):
        """
        Double the bet and deal one more card to player.
        
        Returns:
            bool: True if double down was successful, False otherwise
        """
        if not self.can_double_down():
            return False
        
        self.player_chips -= self.bet
        self.bet *= 2
        self.player_hand.add_card(self.deck.deal_card())
        
        if self.player_hand.is_bust():
            self.game_state = "game_over"
            self.result = "player_bust"
        else:
            self.game_state = "dealer_turn"
            self.dealer_play()
        
        return True
    
    def reset_game(self):
        """Reset the game to idle state."""
        self.game_state = "idle"
        self.result = None
