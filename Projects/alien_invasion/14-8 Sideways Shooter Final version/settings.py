class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Ship settings
        self.ship_speed = 4.5

         # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 100
        self.bullet_color = (255, 20, 57)
        self.bullets_allowed = 5

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        # How much target score raises
        self.target_score_scale = 10

        self.difficulty_level = 'medium'   
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        if self.difficulty_level == 'easy':
            self.ship_limit = 5
            self.bullets_allowed = 10
            self.ship_speed = 1.5
            self.bullet_speed = 1.5
            self.alien_speed = 0.5
            self.alien_frequency = 0.015        
        elif self.difficulty_level == 'medium':
            self.ship_limit = 3
            self.bullets_allowed = 5
            self.ship_speed = 2.5
            self.bullet_speed = 3.0
            self.alien_speed = 1.0
            self.alien_frequency = 0.015
        elif self.difficulty_level == 'hard':
            self.ship_limit = 2
            self.bullets_allowed = 3
            self.ship_speed = 3.0
            self.bullet_speed = 6.0
            self.alien_speed = 2.0
            self.alien_frequency = 0.025

        # Scoring
        self.alien_points = 50
        self.target_score = 1000

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_frequency *= self.speedup_scale

        self.target_score = int(self.target_score * self.target_score_scale)
        self.alien_points = int(self.alien_points * self.score_scale)
