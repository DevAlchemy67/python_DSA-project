#!/usr/bin/env python3
"""
Script to generate placeholder card images for the Blackjack game.
Run this script to create all 52 card images in the cards directory.
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Card dimensions
CARD_WIDTH = 80
CARD_HEIGHT = 120

# Colors
COLORS = {
    'hearts': '#ff4444',
    'diamonds': '#ff4444',
    'clubs': '#000000',
    'spades': '#000000'
}

SUIT_SYMBOLS = {
    'hearts': '♥',
    'diamonds': '♦',
    'clubs': '♣',
    'spades': '♠'
}

# Use the actual rank names from Card class
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
SUITS = ['hearts', 'diamonds', 'clubs', 'spades']

def create_card_image(rank, suit, output_path):
    """Create a card image with the given rank and suit."""
    # Create a white background
    img = Image.new('RGB', (CARD_WIDTH, CARD_HEIGHT), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw border
    draw.rectangle([(0, 0), (CARD_WIDTH-1, CARD_HEIGHT-1)], outline='black', width=2)
    
    # Draw corners
    corner_size = 15
    
    # Top-left corner
    draw.rectangle([(0, 0), (corner_size, corner_size)], fill=COLORS[suit])
    # Top-right corner
    draw.rectangle([(CARD_WIDTH-corner_size, 0), (CARD_WIDTH, corner_size)], fill=COLORS[suit])
    # Bottom-left corner
    draw.rectangle([(0, CARD_HEIGHT-corner_size), (corner_size, CARD_HEIGHT)], fill=COLORS[suit])
    # Bottom-right corner
    draw.rectangle([(CARD_WIDTH-corner_size, CARD_HEIGHT-corner_size), (CARD_WIDTH, CARD_HEIGHT)], fill=COLORS[suit])
    
    # Try to use a font (fallback to default if not available)
    try:
        font = ImageFont.truetype("arial.ttf", 12)
    except:
        font = ImageFont.load_default()
    
    # Map rank to display text
    rank_display = rank[0].upper() if rank != '10' else '10'
    suit_symbol = SUIT_SYMBOLS[suit]
    text = f"{rank_display}{suit_symbol}"
    
    # Top-left
    draw.text((5, 5), text, fill='black', font=font)
    # Top-right
    text_width = draw.textlength(text, font=font)
    draw.text((CARD_WIDTH - text_width - 5, 5), text, fill='black', font=font)
    # Bottom-left
    draw.text((5, CARD_HEIGHT - 20), text, fill='black', font=font)
    # Bottom-right
    draw.text((CARD_WIDTH - text_width - 5, CARD_HEIGHT - 20), text, fill='black', font=font)
    
    # Draw suit symbol in center
    center_text = SUIT_SYMBOLS[suit]
    try:
        center_font = ImageFont.truetype("arial.ttf", 24)
    except:
        center_font = ImageFont.load_default()
    
    text_width = draw.textlength(center_text, font=center_font)
    draw.text((CARD_WIDTH // 2 - text_width // 2, CARD_HEIGHT // 2 - 12), 
              center_text, fill=COLORS[suit], font=center_font)
    
    # Save the image
    img.save(output_path)
    print(f"Created: {output_path}")

def main():
    """Generate all 52 card images."""
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create the cards directory if it doesn't exist
    if not os.path.exists(script_dir):
        os.makedirs(script_dir, exist_ok=True)
    
    # Generate all cards
    for suit in SUITS:
        for rank in RANKS:
            # Use the actual rank name for the filename
            filename = f"{rank}_of_{suit}.png"
            output_path = os.path.join(script_dir, filename)
            
            create_card_image(rank, suit, output_path)
    
    # Create card back image
    card_back = Image.new('RGB', (CARD_WIDTH, CARD_HEIGHT), color='#1e3a8a')
    draw = ImageDraw.Draw(card_back)
    draw.rectangle([(0, 0), (CARD_WIDTH-1, CARD_HEIGHT-1)], outline='gold', width=2)
    
    # Draw diagonal lines
    for i in range(0, CARD_WIDTH, 10):
        draw.line([(i, 0), (0, i)], fill='gold', width=2)
    for i in range(0, CARD_HEIGHT, 10):
        draw.line([(CARD_WIDTH, i), (i, CARD_HEIGHT)], fill='gold', width=2)
    
    card_back.save(os.path.join(script_dir, "card_back.png"))
    print("Created: card_back.png")
    
    print("\nAll card images generated successfully!")

if __name__ == "__main__":
    main()
