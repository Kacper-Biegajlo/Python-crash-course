class GameStats:
    """Track statistics for Target Practice."""
    def __init__(self, tp_game):
        """Initialize statistics."""
        self.settings = tp_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.num_misses = 0
        # Start Target Practice in an active state.
        self.game_active = True