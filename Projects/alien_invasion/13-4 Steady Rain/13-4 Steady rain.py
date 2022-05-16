import sys
import pygame

from settings import Settings
from raindrop import Raindrop

class RainGame:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Raindrops")
        
        self.raindrops = pygame.sprite.Group()
        self._create_raindrops()
 
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_raindrops(self):
        """Create the row of raindrops."""
        # Create an raindrop and find the number of raindrops in a row.
        # Spacing between each raindrop is equal to one raindrop width.
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.settings.screen_width - raindrop_width

        # Determine the number of rows of raindrops that fit on the screen.
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (1 * raindrop_height)

        # We'll need this number again to make new rows.
        self.number_raindrops_x = available_space_x // (2 * raindrop_width)

        #Create the full sky of raindrops.
        for row_number in range(number_rows):
            self._create_row(row_number)

    def _create_row(self, row_number):
        """Create a single row of raindrops."""
        for raindrop_number in range(self.number_raindrops_x):
            self._create_raindrop(raindrop_number, row_number)

    def _create_raindrop(self, raindrop_number, row_number):
        """Create an raindrop and place it in the row."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.rect.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.y = 2 * raindrop.rect.height * row_number
        raindrop.rect.y = raindrop.y
        self.raindrops.add(raindrop)

    def _update_raindrops(self):
        """
        update position of raindrops on the screen
        """
        self.raindrops.update()

        # Assume we won't make new drops.
        make_new_raindrops = False
        for raindrop in self.raindrops.copy():
            if raindrop.check_fallen_raindrops():
                # Remove this drop, and we'll need to make new drops.
                self.raindrops.remove(raindrop)
                make_new_raindrops = True

        # Make a new row of drops if needed.
        if make_new_raindrops:
            self._create_row(0)
 
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    rg_game = RainGame()
    rg_game.run_game()