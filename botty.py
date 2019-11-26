#! /usr/bin/env python3
"""
Botty.py for the class of 2019.

This program will attempt to play our games made in class over telegram.
"""

from testgame import TestGame

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s'
                           + '- %(message)s')

logger = logging.getLogger(__name__)

users = {}

games = [
    TestGame
]


def pick_a_game(update, context):
    """Pick a game from a list and init the class."""
    for game in games:
        message = '/' + game.game_name + '\n' + game.description
        update.message.reply_text(message)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi we should pick a game!')
    chat_id = context.chat_id
    users[chat_id] = None
    game = pick_a_game(update, context)
    users[chat_id] = game


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def command_recieved(self, update, context):
    """Send command to appropiate game."""
    chat_id = context.chat_id
    command = update.message.text
    if chat_id in users:
        game = users[chat_id]
    else:
        game = None

    if game:
        game.recieve_command(command)
    else:
        # Starting a new game
        for game_i in games:
            if game_i.game_name == command:
                users[chat_id] = game_i()
                game = users[chat_id]
                message = "You choose to play..\n"
                message += game.welcome()
                update.message.reply_text(message)


def main():
    """Run the actual program."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # General command handeller for game options
    dp.add_handler(MessageHandler(Filters.command, command_recieved))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()


if __name__ == '__main__':
    main()
