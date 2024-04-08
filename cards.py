import pygame

class Card(pygame.sprite.Sprite):
    def __init__(self, image_path, position, suit: str):  # suits could be Clubs or Hearts
        super().__init__()
        self.card_name = suit[0]  # can take values C or H

        # Load the image using the provided path
        self.image = pygame.image.load(image_path)
        self.image_path = image_path

        # Scale the image if needed (optional)
        # self.image = pygame.transform.scale(self.image, (card_img.get_width() * 4, card_img.get_height() * 4))

        # Create the rect based on the loaded image
        self.rect = self.image.get_rect()
        self.rect.topleft = position  # Set position

    def get_value(self):
        """
        Returns the value of the card based on its rank.
        """

        # Define a dictionary to map rank to value
        card_values = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,  # Ace can have a value of 1 or 11 depending on the game
        }

        # Extract the rank from the image filename (assuming rank is before suit letter)
        rank = self.image_path.split("/")[-1].split(self.card_name)[0]

        # Return the value from the dictionary
        return card_values.get(rank)
