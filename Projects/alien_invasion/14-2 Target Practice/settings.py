class Settings:
    """A class to store all settings for Target Practice."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 4.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 30
        self.bullet_height = 3
        self.bullet_color = (255, 20, 57)
        self.bullets_allowed = 3

        # Target settings
        self.target_speed = 4.0

        # target_direction of 1 represents up; -1 represents down.
        self.direction = 1

        # Game rulles.
        self.miss_limit = 3
