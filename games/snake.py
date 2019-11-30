"""
A game of snake.

This is a simple branching path story.

"""

__author__ = "Pakhin Pawornwitoon"
__copyright__ = "Copyright 2019, Chulalongkorn University"
__credits__ = ["Pakhin Pawornwitoon"]
__license__ = "AGPL"
__version__ = "1.0.0"
__maintainer__ = "Dr Andrew King"
__email__ = "sheepchaan@gmail.com"
__status__ = "Production"


from game import Game


class Event():
    """The base event class."""

    def __init__(self, parent):
        """Crate the event."""
        self.time_event_occured = 0
        self.parent = parent

    def say(self, message):
        """Message the player."""
        self.parent.say(message)

    def choose(self, message, options, callbacks):
        """Make a choice."""
        self.parent.choice(message, options, callbacks)

    def enter(self):
        """Enter the event."""
        pass


class Start(Event):
    """The intro event."""

    def enter(self, callback):
        """Enter the event."""
        self.say("Jason wakes up in the forest with vague memory")
        self.say("He stands up and looks around himself")
        self.say("He looks to the left and find an axe and to the right a"
                 + " compass")
        self.callback = callback
        self.choose("What do you pick up?", ["axe", "compass"],
                    self.post_question)

    def post_question(self, answer):
        """Do the action on picking up the item."""
        if answer == "axe":
            self.say("iI got an axe")
            self.callback("axe")
        elif answer == "compass":
            self.say("It is gonna br useful, isn't it?")
            self.callback("compass")


class Anaconda(Event):
    """The Anaconda event."""

    def enter(self, callback):
        """Enter the event."""
        self.say("After walking for a while, he hears the flow of water")
        self.say("He feels very thirsty, so he walks steadily toward the"
                 + " sound")
        self.say("Suddenly, Anaconda jumps out of the river!!!")
        self.callback = callback
        self.choose("What do you do?", ["runaway", "fight"],
                    self.post_question)

    def post_question(self, answer):
        """Do the action based on player reply."""
        if answer == "runaway":
            self.say("Oh no!, it is faster than I expected")
            self.callback("GAME OVER")
        elif answer == "fight":
            self.say("I can endure its agrassive attack, helppppp")
            self.callback("GAME OVER")


class Tiger(Event):
    """The tiger event."""

    def enter(self, callback):
        """Enter the event."""
        self.say("After walking for along time, Jason feels extremly"
                 + " exhuasted")
        self.say("The sky is getting darker and derker")
        self.say("Heyyy, there is a cave ahead!!, I'm gonna take a nap there")
        self.say("In the cave, there are red eyes appearing in the dark")
        self.say("Then, the creature rush out of the dark, RRRRRRR")
        self.say("That's a huge tiger!!!")
        self.say("Jason see a big tall tree not far away")
        self.callback = callback
        self.choose("What do you do?", ["fight", "climb the tree"],
                    self.post_question)

    def post_question(self, answer):
        """Do the action based on player reply."""
        if answer == "fight":
            self.say("OUCHHH!!!, Mommmmmmm, I wanna go homeeee")
            self.callback("GAME OVER")
        elif answer == "climb the tree":
            self.say("He could get away from the tiger")
            self.say("He fell asleep, until tiger got bored and went away")
            self.say("He gets down from the tree and uses the compass to"
                     + " guid him out of the forest")
            self.callback("Yayyy, VICTORY")
        else:
            raise ValueError(f"Not handelled {answer}")


class Death(Event):
    """What happens when you die."""

    def enter(self):
        """Enter the event."""
        self.say("GAME OVER")


class Victory(Event):
    """What heppens when you win."""

    def enter(self):
        """Enter the event."""
        self.say("congratulation!! You are able to to get out")


class Snake(Game):
    """The snake game."""

    @classmethod
    def game_name(self):
        """Get unique game name used for selection no spaces."""
        return "snake"

    @classmethod
    def description(self):
        """Get the game description."""
        return ("Get out of the Anaconda and Tiger infested forest.")

    def welcome(self):
        """Get a welcome message."""
        return ("Snake\nA simple branching story with lovable Anaconda's"
                + " and Tigers\n"
                + "Created by " + __author__)

    def play(self):
        """Start the actual game."""
        event = Start(self)
        event.enter(self.intro_done)

    def intro_done(self, result):
        """Play stage after intro."""
        if result == 'axe':
            event = Anaconda(self)
            event.enter(self.anaconda_path)
            return
        elif result == 'compass':
            event = Tiger(self)
            event.enter(self.tiger_path)
            return
        else:
            raise ValueError(f"RESULT NOT HANDELLED {result}")

    def anaconda_path(self, result):
        """Do post anaconda stuff."""
        self.say("YOU DIED")
        Death(self).enter()

    def tiger_path(self, result):
        """Do post tiger stuff."""
        if result == 'GAME OVER':
            self.say("YOU DIED")
            Death(self).enter()
            return
        else:
            self.say("YOU WON")
            Victory(self).enter()
            return
