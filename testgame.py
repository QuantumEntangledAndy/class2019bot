"""
A simple test game.

Licence: AGPL v3
"""

from game import Game


class TestGame(Game):
    """A simple test game."""

    def __init__(self):
        """Create the test game."""
        super().__init__()

    @classmethod
    def game_name(self):
        """Get unique game name used for selection."""
        return "testgame"

    @classmethod
    def description(self):
        """Get the game description."""
        return "A Simple test game"

    def welcome(self):
        """Get a welcome message."""
        return """Welcome to the test game
        Created by AWK to test the system."""
