filename = ('high_score.txt')

class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, ss_game):
        """Initialize statistics."""
        self.settings = ss_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        with open(filename) as f:
            content = f.read()
            self.high_score = int(content)
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    # Start Alien Invasion in an active state.
        self.game_active = True