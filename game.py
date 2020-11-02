"""
Module handels basic setup for all games.

Licence: AGPL v3
"""

from telegram import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def build_menu(buttonTexts, cols):
    """Build a menu of options from a list."""
    for idx, buttonText in enumerate(buttonTexts):
        if not buttonText.startswith("/"):
            buttonTexts[idx] = "/" + buttonText

    result = []
    for i in range(0, len(buttonTexts), cols):
        result.append([KeyboardButton(s) for s in buttonTexts[i : i + cols]])
    return result


def make_keyboard(replies):
    """Create a user keyboard."""
    return ReplyKeyboardMarkup(build_menu(replies, 2))


class Game:
    """Base class for the game."""

    def __init__(self, bot, chat_id):
        """Create the class by storing the chat ID."""
        self.possible_replies = []
        self.bot = bot
        self.chat_id = chat_id
        self.the_open_answer = None

    def say(self, message):
        """Say something in the chat."""
        if message.strip():  # Check the message is not whitespace/blank
            self.bot.send_message(
                self.chat_id, message, reply_markup=ReplyKeyboardRemove()
            )

    def choice(self, message="What do you choose?", options=[], callbacks=[]):
        """Give the player some choices."""
        self.possible_replies = []
        if callable(callbacks):
            for idx, choice in enumerate(options):
                self.possible_replies.append(
                    {"command": choice, "callback": callbacks}
                )
        else:
            if len(options) != len(callbacks):
                raise ValueError(
                    "Length of options not the same as length of" + "callbacks"
                )

            for idx, choice in enumerate(options):
                self.possible_replies.append(
                    {"command": choice, "callback": callbacks[idx]}
                )

        keyboard = make_keyboard(list(options))
        self.bot.send_message(self.chat_id, message, reply_markup=keyboard)

    def open_answer(self, message="What say you?", callback=None):
        """Set next text they give us will be used for an open answer."""
        self.the_open_answer = callback
        self.say(message)

    def recieve_command(self, command):
        """Handel the recieved command."""
        if command == "/play":
            self.possible_replies = []
            self.play()
            return True
        for possible_reply in self.possible_replies:
            if "/" + possible_reply["command"] == command:
                if callable(possible_reply["callback"]):
                    possible_reply["callback"](possible_reply["command"])
                    return True
        return False

    def recieve_text(self, message):
        """Handle open answer replies."""
        if self.the_open_answer:
            callback = self.the_open_answer
            self.the_open_answer = None
            if callable(callback):
                callback(message)

    @classmethod
    def game_name(self):
        """Get unique game name used for selection no spaces."""

    @classmethod
    def description(self):
        """Get the game description."""

    def welcome(self):
        """Get a welcome message."""

    def play(self):
        """Start playing, shoud reset too."""

    def goodbye(self):
        """Send the goodbye message."""
        self.say(
            "==================================\n"
            + "That is the end of this game.\n"
            + "You can play again with /play\n"
            + "Or choose another game with /start"
        )
