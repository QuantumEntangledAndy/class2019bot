"""
Module handels basic setup for all games.

Licence: AGPL v3
"""

from telegram import ReplyKeyboardMarkup, KeyboardButton


def build_menu(buttonTexts, cols):
    """Build a menu of options from a list."""
    for idx, buttonText in enumerate(buttonTexts):
        if not buttonText.startswith('/'):
            buttonTexts[idx] = '/' + buttonText

    result = []
    for i in range(0, len(buttonTexts), cols):
        result.append([KeyboardButton(s) for s in buttonTexts[i:i+cols]])
    return result


def make_keyboard(replies):
    """Create a user keyboard."""
    return ReplyKeyboardMarkup(build_menu(replies, 2))


class Game():
    """Base class for the game."""

    def __init__(self):
        """Create the class by storing the chat ID."""
        self.current_replies = []

    def say(self, message, update):
        """Say something in the chat."""
        update.message.reply_text(message)

    def choice(self, options, callbacks, update,
               message="What do you choose?"):
        """Give the player some choices."""
        self.current_replies = []
        keyboard = make_keyboard(list(options))
        update.message.reply_text(message, reply_markup=keyboard)

        if len(options) != len(callbacks):
            raise ValueError("Length of options not the same as length of"
                             + "callbacks")

        for idx, choice in enumerate(options):
            self.current_replies.append({
                'command': choice,
                'callback': callbacks[idx]
            })

    def recieve_command(self, command):
        """Handel the recieved command."""
        if command == '/play':
            self.play()
            return True
        for current_reply in self.current_replies:
            if '/' + current_reply['command'] == command:
                if callable(current_reply['callback']):
                    current_reply['callback']()
                    return False

    @classmethod
    def game_name(self):
        """Get unique game name used for selection no spaces."""

    @classmethod
    def description(self):
        """Get the game description."""

    def welcome(self):
        """Get a welcome message."""

    def play(self):
        """Start playing."""
        self.current_replies = []
