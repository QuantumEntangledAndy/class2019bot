"""
A simple test game.

Licence: AGPL v3
"""

from game import Game


class TestGame(Game):
    """A simple test game."""

    def __init__(self, bot, chat_id):
        """Create the test game."""
        super().__init__(bot, chat_id)

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

    def play(self):
        """Start playing, shoud reset too."""
        self.say("The test game starts")
        self.choice("You have to decide what to do", ['left', 'right'],
                    [self.turn, self.turn])

    def turn(self, input):
        """Take the turn."""
        if input == 'left':
            self.say("You turn left... it feels wrong")
        elif input == 'right':
            self.say("You turn right... it feels right")
        self.choice("You have to decide what to do", ['left', 'right'],
                    [self.turn, self.turn])
