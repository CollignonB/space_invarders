class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game) -> None:
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        #Start ALien Invasion in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize satistics that can change during the game."""
        self.ship_left = self.settings.ship_limit