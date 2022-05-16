import pygame
from random import randint
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien."""
    def __init__(self, ss_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien on random postion at right of the screen.
        self.rect.left = self.screen.get_rect().right

        alien_top_max = self.settings.screen_height - (3 * self.rect.height)
        self.rect.top = randint(0, alien_top_max)
 
        # Store the alien's exact horizontal position. 
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien right or left."""
        self.x -= self.settings.alien_speed
        self.rect.x = self.x
