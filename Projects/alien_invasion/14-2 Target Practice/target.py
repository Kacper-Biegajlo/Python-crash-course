import pygame
from pygame.sprite import Sprite

class Target(Sprite):
    """A class to represent target."""
    def __init__(self, tp_game):
        """Initialize the target and set its starting position."""
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = tp_game.screen.get_rect()
        
        # Load the target image and set its rect attribute.
        self.image = pygame.image.load('images/target.png')
        self.rect = self.image.get_rect()
        
        # Start target at middle right of the screen.
        self.rect.midright = self.screen_rect.midright  
 
        # Store the targets's exact horizontal position. 
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if target is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom <= screen_rect.bottom:
            self.settings.direction *= -1
        if self.rect.top >= screen_rect.top:
            self.settings.direction *= -1

    def update(self):
        """Move the target top and right."""
        self.y += (self.settings.target_speed * self.settings.direction)
        self.rect.y = self.y

    def center_target(self):
        """Center the target on the right side of the screen."""
        self.rect.midright = self.screen_rect.midright
        
        # Store the target's position as a decimal value.
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the target at its current location."""
        self.screen.blit(self.image, self.rect)

