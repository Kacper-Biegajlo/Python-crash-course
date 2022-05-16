# wanted to make a fleet but took a look at random version and it is more fun
# also had fun with the settings in that game
import sys
import pygame

from game_stats import GameStats
from button import Button
from settings import Settings
from ship import Ship
from bullet import Bullet
from target import Target

class TargetPractice:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Target Practice")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)

        # Make the Play button.
        self.play_button = Button(self, "Play")
 
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_target()
                
            self._update_screen()

    def _start_game(self):
        """Starts a new game with mouse click or key 'P'."""
        # Reset the game statistics.
        self.stats.reset_stats() 
        self.stats.game_active = True

        # Get rid of any remaining bullets.
        self.bullets.empty()

        # Create a new target and center the ship.
        self.target.center_target()
        self.ship.center_ship()

        # Hide the mouse cursor. 
        pygame.mouse.set_visible(False)
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
               mouse_pos = pygame.mouse.get_pos()
               self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p and not self.stats.game_active:
            self._start_game()
   
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that missed and remove 1 life for each.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                 self.bullets.remove(bullet)
                 self._add_miss()
            
            self._check_bullet_alien_collisions()

    def _update_target(self):
        """
        Check if the target is at an edge,
          then change it's direction.
        """
        self.target.check_edges()
        self.target.update()

    def _add_miss(self):
        """Increment the number of misses, and check if the game should end."""
        self.stats.num_misses += 1
        if self.stats.num_misses >= self.settings.miss_limit:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets that hit the target.
        collisions = pygame.sprite.spritecollide(
                self.target, self.bullets, True)
            
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.target.blitme()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()


        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    tp = TargetPractice()
    tp.run_game()