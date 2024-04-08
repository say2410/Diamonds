import pygame, sys
from settings import *
from cards import Card
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE_STRING)
        self.cards = []
        self.score = 0  # Initialize score
        self.computer_cards = []  # List of computer's cards (hidden)
        self.current_turn = "Player 1"  # Whose turn it is
        self.diamond_deck = []  # List to store diamond cards
        self.load_diamonds()  # Load diamond cards (function below)
        width_value = 100
        height_value = 100
        width = 200
        height = 600

        for suit in ['Clubs']:
            for card_value in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']:
                image_path = f"images/{suit}/{card_value}{suit[0]}.png"
                position = (width + width_value, height)
                width_value += 100
                card = Card(image_path, position, suit)
                self.cards.append(card)
            width = 300
            width_value = 100
            height += height_value

    def load_diamonds(self):
        """Loads diamond cards from a separate deck."""
        diamond_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for card_value in diamond_values:
            image_path = f"images/Diamonds/{card_value}D.png"  # Adjust image path format
            # Assuming diamond cards are in a separate "Diamonds" folder
            position = (0, 0)  # Dummy position (will be updated later)
            diamond_card = Card(image_path, position, "Diamonds")
            self.diamond_deck.append(diamond_card)

    def diamond(self):
        """Returns a random diamond card."""
        if self.diamond_deck:
            diamond_card = random.choice(self.diamond_deck)
            self.diamond_deck.remove(diamond_card)
            return diamond_card
        else:
            return None  # No diamonds left

    def computers_choice(self):
        """Returns the value of the computer's chosen card and removes it from their deck."""
        if self.computer_cards:
            chosen_value = random.choice(self.computer_cards)
            self.computer_cards.remove(chosen_value)
            return chosen_value
        else:
            return None
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.current_turn == "Player 1":
                    mouse_pos = pygame.mouse.get_pos()

                    for card in self.cards:
                        if card.rect.collidepoint(mouse_pos):
                            self.cards.remove(card)
                            computer_choice = self.computers_choice()

                            if computer_choice is not None:
                                # Award points based on chosen cards and diamond value
                                diamond_card = self.diamond()
                                if diamond_card is not None:
                                    diamond_value = diamond_card.get_value()
                                    if card.get_value() > computer_choice:
                                        self.score += diamond_value
                                        self.current_turn = "Computer"
                                    else:
                                        self.current_turn = "Player 1"
                                else:
                                    # No diamonds left, no turn change
                                    pass
                            else:
                                # Computer has no cards left, player 1 keeps their turn
                                pass
                            break  # Only remove one card per click

            self.screen.fill(BG_COLOR)

            # Draw player one's cards
            for card in self.cards:
                self.screen.blit(card.image, card.rect)

            # Display score and current turn
            self.display_score(self.current_turn)

            pygame.display.flip()

    def update_score(self, card_value):
        pass

    def display_score(self, current_turn):
    # Define score rectangle properties (adjust as needed)
        score_rect_x = 100
        score_rect_y = 100
        score_rect_width = WIDTH - 1625
        score_rect_height = 80

    # Create the score rectangle
        score_rect = pygame.Rect(score_rect_x, score_rect_y, score_rect_width, score_rect_height)

    # Set rectangle color (optional)
        pygame.draw.rect(self.screen, (255, 255, 255), score_rect)  # White rectangle

    # Define font and text color
        font = pygame.font.Font(None, 24)  # Adjust font size as needed
        text_color = (0, 0, 0)  # Black text

    # Create text surfaces for heading, score and player labels
        heading_text = font.render("Scoreboard", True, text_color)
        score_text = font.render(f"Player 1: {self.score}", True, text_color)
        turn_text = font.render(f"Turn: {current_turn}", True, text_color)

    # Calculate text position within the rectangle
        INCREASED_OFFSET = 15  # Adjust spacing as needed
        heading_text_rect = heading_text.get_rect(center=(score_rect.centerx, score_rect.top + INCREASED_OFFSET))
        score_text_rect = score_text.get_rect(centerx=score_rect.centerx, y=score_rect.centery - score_text.get_height() // 2)
        turn_text_rect = turn_text.get_rect(centerx=score_rect.centerx, y=score_rect.bottom - turn_text.get_height() - INCREASED_OFFSET)

    # Blit the text surfaces onto the screen
        self.screen.blit(heading_text, heading_text_rect)
        self.screen.blit(score_text, score_text_rect)
        self.screen.blit(turn_text, turn_text_rect)


if __name__ == '__main__':
    game = Game()
    game.run()
