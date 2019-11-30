#! /usr/bin/env python3
"""
Botty.py for the class of 2019.

This program will attempt to play our games made in class over telegram.

Licence: AGPL v3
"""

from pathlib import Path

from games.testgame import TestGame
from games.abyss import Abyss
from games.jeff import Jeff
from games.love import Love
from games.rng import Rng
from games.jungle import Jungle
from games.apocalypse import Apocalypse
from games.mathspirit import MathSpirit
from games.momma import Momma

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardRemove

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s'
                           + '- %(message)s')

logger = logging.getLogger(__name__)

users = {}

games = [
    TestGame,
    Abyss,
    Jeff,
    Love,
    Rng,
    Jungle,
    Apocalypse,
    MathSpirit,
    Momma,
]


def no_keyboard():
    """Get the setting required to disable the keyboard."""
    return {"reply_markup": ReplyKeyboardRemove()}


def pick_a_game(update, context):
    """Pick a game from a list and init the class."""
    for game in games:
        message = '/' + game.game_name() + '\n' + game.description()
        update.message.reply_text(message, **no_keyboard())


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi we should pick a game!',
                              **no_keyboard())
    chat_id = update.message.chat_id
    users[chat_id] = None
    pick_a_game(update, context)


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!', **no_keyboard())


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def command_recieved(update, context):
    """Send command to appropiate game."""
    chat_id = update.message.chat_id
    command = update.message.text
    if chat_id in users:
        game = users[chat_id]
    else:
        game = None

    if game:
        if not game.recieve_command(command):
            logger.warning(f'Unhandelled command recieved {command}')
    else:
        # Starting a new game
        for game_i in games:
            if '/' + game_i.game_name() == command:
                users[chat_id] = game_i(context.bot, chat_id)
                game = users[chat_id]
                message = "You have chosen to play..\n"
                message += '\n==================\n'
                message += game.welcome()
                message += '\n==================\n'
                message += '\nTo begin use /play'
                message += '\nTo select another use /start'
                update.message.reply_text(message,
                                          **no_keyboard())


def text_recieved(update, context):
    """Send text to appropiate game."""
    chat_id = update.message.chat_id
    text = update.message.text
    if chat_id in users:
        game = users[chat_id]
    else:
        game = None

    if game:
        game.recieve_text(text)


def main():
    """Run the actual program."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    token_file = Path("token")
    token = token_file.read_text().strip()
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # General command handeller for game options
    dp.add_handler(MessageHandler(Filters.command, command_recieved))
    dp.add_handler(MessageHandler(Filters.text, text_recieved))

    # log all errors
    # dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()


if __name__ == '__main__':
    main()
