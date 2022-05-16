class Settings:
    """A class to store all settings for Sideway shooter."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 4.5

         # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 150
        self.bullet_color = (255, 20, 57)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 2.0
        self.alien_frequency = 0.020