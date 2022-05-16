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
        self.bullet_width = 30
        self.bullet_height = 3
        self.bullet_color = (255, 20, 57)
        self.bullets_allowed = 3

        # target_direction of 1 represents up; -1 represents down.
        self.direction = 1

        # Game rulles.
        self.miss_limit = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # After every levelup_hits, level up the difficulty.
        self.levelup_hits = 1
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.bullet_speed = 3.0
        self.target_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.bullet_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale
