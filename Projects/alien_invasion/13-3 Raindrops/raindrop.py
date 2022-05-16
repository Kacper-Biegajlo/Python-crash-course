import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop in the sky."""
    def __init__(self, rd_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings
        
        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()
        
        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
 
        # Store the raindrops's exact horizontal position. 
        self.y = float(self.rect.y)

    def update(self):
        """Move the raindrop down the screen."""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y