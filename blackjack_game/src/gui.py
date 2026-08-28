"""
GUI for Blackjack game
Graphical user interface using Tkinter with card image display.
"""

import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os
import sys

# Add the parent directory to the path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.game import BlackjackGame
from src.card import Card


class BlackjackGUI:
    """
    Graphical user interface for the Blackjack game.
    
    Features:
        - Player's hand with card images
        - Dealer's hand with card images (one card hidden initially)
        - Current scores
        - Action buttons (Hit, Stand, New Game, Double Down)
        - Chip display
        - Bet controls
    """
    
    # Card dimensions
    CARD_WIDTH = 80
    CARD_HEIGHT = 120
    CARD_SPACING = 20
    
    # Colors
    BG_COLOR = "#0a5c36"
    TABLE_COLOR = "#1a8c4f"
    TEXT_COLOR = "white"
    BUTTON_COLOR = "#2e8b57"
    BUTTON_FG = "white"
    
    def __init__(self, root):
        """
        Initialize the GUI.
        
        Args:
            root (tk.Tk): The root Tkinter window
        """
        self.root = root
        self.game = BlackjackGame()
        self.card_images = {}  # Cache for card images
        
        self.setup_window()
        self.create_widgets()
        self.load_card_images()
    
    def setup_window(self):
        """Set up the main window properties."""
        self.root.title("Blackjack Game")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        self.root.configure(bg=self.BG_COLOR)
        
        # Center the window
        self.root.eval('tk::PlaceWindow . center')
    
    def create_widgets(self):
        """Create all GUI widgets."""
        # Main frame
        main_frame = tk.Frame(self.root, bg=self.TABLE_COLOR, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="BLACKJACK", 
            font=("Arial", 24, "bold"),
            fg="gold",
            bg=self.TABLE_COLOR
        )
        title_label.pack(pady=10)
        
        # Dealer's area
        dealer_frame = tk.Frame(main_frame, bg=self.TABLE_COLOR)
        dealer_frame.pack(fill=tk.X, pady=10)
        
        dealer_label = tk.Label(
            dealer_frame,
            text="Dealer's Hand",
            font=("Arial", 14, "bold"),
            fg=self.TEXT_COLOR,
            bg=self.TABLE_COLOR
        )
        dealer_label.pack()
        
        self.dealer_cards_frame = tk.Frame(dealer_frame, bg=self.TABLE_COLOR)
        self.dealer_cards_frame.pack(pady=10)
        
        self.dealer_score_label = tk.Label(
            dealer_frame,
            text="Score: 0",
            font=("Arial", 12),
            fg=self.TEXT_COLOR,
            bg=self.TABLE_COLOR
        )
        self.dealer_score_label.pack()
        
        # Player's area
        player_frame = tk.Frame(main_frame, bg=self.TABLE_COLOR)
        player_frame.pack(fill=tk.X, pady=10)
        
        player_label = tk.Label(
            player_frame,
            text="Your Hand",
            font=("Arial", 14, "bold"),
            fg=self.TEXT_COLOR,
            bg=self.TABLE_COLOR
        )
        player_label.pack()
        
        self.player_cards_frame = tk.Frame(player_frame, bg=self.TABLE_COLOR)
        self.player_cards_frame.pack(pady=10)
        
        self.player_score_label = tk.Label(
            player_frame,
            text="Score: 0",
            font=("Arial", 12),
            fg=self.TEXT_COLOR,
            bg=self.TABLE_COLOR
        )
        self.player_score_label.pack()
        
        # Bet controls
        bet_frame = tk.Frame(main_frame, bg=self.TABLE_COLOR)
        bet_frame.pack(fill=tk.X, pady=10)
        
        bet_label = tk.Label(
            bet_frame,
            text="Bet:",
            font=("Arial", 12),
            fg=self.TEXT_COLOR,
            bg=self.TABLE_COLOR
        )
        bet_label.pack(side=tk.LEFT, padx=5)
        
        self.bet_entry = tk.Entry(
            bet_frame,
            font=("Arial", 12),
            width=10,
            justify=tk.CENTER
        )
        self.bet_entry.pack(side=tk.LEFT, padx=5)
        self.bet_entry.insert(0, "10")
        
        # Chips display
        self.chips_label = tk.Label(
            bet_frame,
            text=f"Chips: ${self.game.get_player_chips()}",
            font=("Arial", 12),
            fg="gold",
            bg=self.TABLE_COLOR
        )
        self.chips_label.pack(side=tk.RIGHT, padx=10)
        
        # Action buttons
        button_frame = tk.Frame(main_frame, bg=self.TABLE_COLOR)
        button_frame.pack(pady=20)
        
        self.new_game_btn = tk.Button(
            button_frame,
            text="New Game",
            command=self.new_game,
            font=("Arial", 12, "bold"),
            bg=self.BUTTON_COLOR,
            fg=self.BUTTON_FG,
            width=12,
            height=2
        )
        self.new_game_btn.pack(side=tk.LEFT, padx=10)
        
        self.hit_btn = tk.Button(
            button_frame,
            text="Hit",
            command=self.player_hit,
            font=("Arial", 12, "bold"),
            bg=self.BUTTON_COLOR,
            fg=self.BUTTON_FG,
            width=12,
            height=2,
            state=tk.DISABLED
        )
        self.hit_btn.pack(side=tk.LEFT, padx=10)
        
        self.stand_btn = tk.Button(
            button_frame,
            text="Stand",
            command=self.player_stand,
            font=("Arial", 12, "bold"),
            bg=self.BUTTON_COLOR,
            fg=self.BUTTON_FG,
            width=12,
            height=2,
            state=tk.DISABLED
        )
        self.stand_btn.pack(side=tk.LEFT, padx=10)
        
        self.double_down_btn = tk.Button(
            button_frame,
            text="Double Down",
            command=self.double_down,
            font=("Arial", 12, "bold"),
            bg=self.BUTTON_COLOR,
            fg=self.BUTTON_FG,
            width=12,
            height=2,
            state=tk.DISABLED
        )
        self.double_down_btn.pack(side=tk.LEFT, padx=10)
        
        # Result label
        self.result_label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 14, "bold"),
            fg="gold",
            bg=self.TABLE_COLOR
        )
        self.result_label.pack(pady=10)
        
        # Card back image (for dealer's hidden card)
        self.card_back_image = self.create_card_back_image()
    
    def load_card_images(self):
        """Load all card images from the assets folder."""
        cards_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "cards")
        
        # Check if directory exists
        if not os.path.exists(cards_dir):
            os.makedirs(cards_dir, exist_ok=True)
            print(f"Created cards directory at: {cards_dir}")
        
        # Load existing card images
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                image_path = os.path.join(cards_dir, f"{rank}_of_{suit}.png")
                if os.path.exists(image_path):
                    try:
                        img = Image.open(image_path)
                        img = img.resize((self.CARD_WIDTH, self.CARD_HEIGHT), Image.LANCZOS)
                        self.card_images[f"{rank}_of_{suit}"] = ImageTk.PhotoImage(img)
                    except Exception as e:
                        print(f"Error loading {image_path}: {e}")
                        # Create a placeholder
                        self.card_images[f"{rank}_of_{suit}"] = self.create_placeholder_card(rank, suit)
                else:
                    # Create a placeholder if image doesn't exist
                    self.card_images[f"{rank}_of_{suit}"] = self.create_placeholder_card(rank, suit)
    
    def create_placeholder_card(self, rank, suit):
        """Create a placeholder card image with rank and suit text."""
        # Create a blank image
        img = Image.new('RGB', (self.CARD_WIDTH, self.CARD_HEIGHT), color='white')
        
        # Simple placeholder - in a real implementation, you'd use PIL drawing
        # For now, we'll just return a blank image
        return ImageTk.PhotoImage(img)
    
    def create_card_back_image(self):
        """Create an image for the back of a card."""
        # Create a blue card back
        img = Image.new('RGB', (self.CARD_WIDTH, self.CARD_HEIGHT), color='#1e3a8a')
        return ImageTk.PhotoImage(img)
    
    def get_card_image(self, card):
        """Get the image for a specific card."""
        key = f"{card.rank}_of_{card.suit}"
        if key in self.card_images:
            return self.card_images[key]
        
        # Create a placeholder if not found
        self.card_images[key] = self.create_placeholder_card(card.rank, card.suit)
        return self.card_images[key]
    
    def clear_cards(self):
        """Clear all card images from the display."""
        for widget in self.dealer_cards_frame.winfo_children():
            widget.destroy()
        for widget in self.player_cards_frame.winfo_children():
            widget.destroy()
    
    def display_dealer_cards(self, show_all=False):
        """
        Display dealer's cards.
        
        Args:
            show_all (bool): If False, hide the first card
        """
        cards = self.game.get_dealer_hand().get_cards()
        
        for i, card in enumerate(cards):
            if i == 0 and not show_all:
                # Show card back for first card
                card_label = tk.Label(
                    self.dealer_cards_frame,
                    image=self.card_back_image,
                    bg=self.TABLE_COLOR
                )
            else:
                card_label = tk.Label(
                    self.dealer_cards_frame,
                    image=self.get_card_image(card),
                    bg=self.TABLE_COLOR
                )
            card_label.pack(side=tk.LEFT, padx=(0, self.CARD_SPACING))
        
        # Update dealer score (hide if first card is hidden)
        if show_all or len(cards) == 0:
            score = self.game.get_dealer_hand().calculate_score()
            self.dealer_score_label.config(text=f"Score: {score}")
        else:
            # Show only the visible card's value
            visible_card = cards[0] if len(cards) > 0 else None
            if visible_card:
                self.dealer_score_label.config(text=f"Showing: {visible_card.value}")
            else:
                self.dealer_score_label.config(text="Score: 0")
    
    def display_player_cards(self):
        """Display player's cards."""
        cards = self.game.get_player_hand().get_cards()
        
        for card in cards:
            card_label = tk.Label(
                self.player_cards_frame,
                image=self.get_card_image(card),
                bg=self.TABLE_COLOR
            )
            card_label.pack(side=tk.LEFT, padx=(0, self.CARD_SPACING))
        
        score = self.game.get_player_hand().calculate_score()
        self.player_score_label.config(text=f"Score: {score}")
    
    def update_ui(self):
        """Update all UI elements based on game state."""
        self.clear_cards()
        
        # Display cards
        show_all_dealer = self.game.get_game_state() == "game_over"
        self.display_dealer_cards(show_all=show_all_dealer)
        self.display_player_cards()
        
        # Update chips
        self.chips_label.config(text=f"Chips: ${self.game.get_player_chips()}")
        
        # Update buttons
        state = self.game.get_game_state()
        
        if state == "idle":
            self.new_game_btn.config(state=tk.NORMAL)
            self.hit_btn.config(state=tk.DISABLED)
            self.stand_btn.config(state=tk.DISABLED)
            self.double_down_btn.config(state=tk.DISABLED)
        elif state == "player_turn":
            self.new_game_btn.config(state=tk.DISABLED)
            self.hit_btn.config(state=tk.NORMAL)
            self.stand_btn.config(state=tk.NORMAL)
            self.double_down_btn.config(state=tk.NORMAL if self.game.can_double_down() else tk.DISABLED)
        else:
            self.new_game_btn.config(state=tk.NORMAL)
            self.hit_btn.config(state=tk.DISABLED)
            self.stand_btn.config(state=tk.DISABLED)
            self.double_down_btn.config(state=tk.DISABLED)
        
        # Update result
        result = self.game.get_result()
        if result:
            result_text = self.get_result_text(result)
            self.result_label.config(text=result_text)
        else:
            self.result_label.config(text="")
    
    def get_result_text(self, result):
        """Convert result code to display text."""
        messages = {
            "player_blackjack": "BLACKJACK! You win!",
            "player_win": "You win!",
            "dealer_win": "Dealer wins!",
            "push": "Push! It's a tie.",
            "player_bust": "Bust! You lose.",
            "dealer_bust": "Dealer busts! You win!"
        }
        return messages.get(result, "")
    
    def new_game(self):
        """Start a new game."""
        try:
            bet = int(self.bet_entry.get())
            if bet <= 0:
                messagebox.showerror("Error", "Bet must be positive")
                return
            
            if not self.game.start_game(bet):
                messagebox.showerror("Error", "Not enough chips for this bet")
                return
            
            self.update_ui()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid bet amount")
    
    def player_hit(self):
        """Player hits (takes another card)."""
        self.game.player_hit()
        self.update_ui()
        
        # Check if player busted
        if self.game.get_game_state() == "game_over":
            messagebox.showinfo("Result", self.get_result_text(self.game.get_result()))
    
    def player_stand(self):
        """Player stands (ends turn)."""
        self.game.player_stand()
        self.update_ui()
        
        if self.game.get_game_state() == "game_over":
            messagebox.showinfo("Result", self.get_result_text(self.game.get_result()))
    
    def double_down(self):
        """Player doubles down."""
        if self.game.double_down():
            self.update_ui()
            if self.game.get_game_state() == "game_over":
                messagebox.showinfo("Result", self.get_result_text(self.game.get_result()))
    
    def run(self):
        """Run the GUI main loop."""
        self.update_ui()
        self.root.mainloop()


def main():
    """Start the Blackjack GUI."""
    root = tk.Tk()
    gui = BlackjackGUI(root)
    gui.run()


if __name__ == "__main__":
    main()
