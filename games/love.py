"""
The Dating Game.

Authours:  Nattamon Panichakul,
"""

from game import Game


class Player():
    """Holds player data."""

    def __init__(self):
        """Create the player."""
        self.current_point = 0
        self.name = ""

    def add_point(self, amount):
        """Gain some points."""
        self.current_point += amount


class Situation():
    """Handles the various situations."""

    def __init__(self, situation, first_option, first_outcome,
                 first_point, second_option, second_outcome, second_point):
        """Create the situation."""
        self.situation = situation
        self.first_option = first_option
        self.first_outcome = first_outcome
        self.first_point = first_point
        self.second_option = second_option
        self.second_outcome = second_outcome
        self.second_point = second_point

    def condition(self, selection, player):
        """Apply the outcome of the choice."""
        if selection == "1":
            player.add_point(self.first_point)
            return self.first_outcome
        if selection == "2":
            player.add_point(self.second_point)
            return self.second_outcome
        else:
            raise ValueError("Not a valid choice, please try again.")

    def final_condition(self, selection, player):
        """Apply the outcode of THE FINAL QUESTION."""
        if selection == "1":
            player.add_point(self.first_point)
        if selection == "2":
            player.add_point(self.second_point)

        if player.current_point >= 41:
            return self.first_outcome
        if player.current_point <= 40:
            return self.second_outcome


class Love(Game):
    """The Love Game."""

    @classmethod
    def game_name(self):
        """Get unique game name used for selection no spaces."""
        return "love"

    @classmethod
    def description(self):
        """Get the game description."""
        return "Win the heart of that special lady in your life."

    def welcome(self):
        """Get a welcome message."""
        return ("Love, the dating game.\n"
                + "This game was created by...\n"
                + "Nattamon Panichakul,\n"
                + "We hope you enjoy it")

    def play(self):
        """Start playing."""
        self.player = Player()
        self.open_answer("Enter your name: ", self.stage1)

    def stage1(self, name):
        """Play stage 1."""
        self.player.name = name

        print("The objective of this game is to find a girl, date her, and"
              + " get her to say yes on your marriage proposal")

        self.situations = []

        self.situations.append(Situation("\n You need to choose a place to"
                                         + " find that girl.",
                                         "Walk into a pub",
                                         "You found a girl", -5,
                                         "Walk along a busy street",
                                         "You found a girl", 10))

        self.situations.append(Situation("What should you do to her?",
                                         "Buy her a drink",
                                         "She is pleased", 20,
                                         "Throw her some pick-up lines",
                                         "Things got awkward", -8))

        self.situations.append(Situation("Choose what you're going to wear"
                                         + " to the amusement park.",
                                         "A suit",
                                         "When she sees you, She says"
                                         + " 'Looks handsome, you’re making"
                                         + " my clothes look lacking.''", 13,
                                         "Dress casually.",
                                         "When sees you, she says,"
                                         + " ‘Wow…(blush), lets go.’", 20))

        self.situations.append(Situation("You get to talk to each other,"
                                         + " spend some quality time and"
                                         + " played lots of roller coasters."
                                         + " When the sun set, you looked"
                                         + " into her eyes and mustered"
                                         + " my courage to confess your"
                                         + " love for her. Her answer is"
                                         + " ‘Yes!’. She becomes"
                                         + " my girlfriend, you kept in"
                                         + " touch and planned for your"
                                         + " next date. \n \n On a next date,"
                                         + " you want to buy her a present."
                                         + " What should it be?",
                                         "A flower you decorated yourself",
                                         "She likes it a lot", 20,
                                         "An expensive ring and flower",
                                         "She feels uneasy and got confused. ",
                                         10))

        self.situations.append(Situation("After a year of dating, you decided"
                                         + " to ask her to marry you.",
                                         "Promised her that you'll love"
                                         + " her forever.",
                                         "SHE SAID YES", 10,
                                         "I will give you everything that"
                                         "you desires, I love you.",
                                         "SHE SAID NO", 15))
        self.play_next_situation(0)

    def play_next_situation(self, i):
        """Play the situation."""
        self.say("", self.situations[i].situation, "\n")
        self.say("1.", self.situations[i].first_option)
        self.say("2.", self.situations[i].second_option, "\n")
        self.say("What do you choose")
        self.i = i
        self.choice("What do you choose", ["1", "2"], self.situation_result)

    def situation_result(self, reply):
        """Play the result of a situation."""
        i = self.i

        if i == 4:
            outcome = self.situations[i].final_condition(reply,
                                                         self.player)
        else:
            outcome = self.situations[i].condition(reply,
                                                   self.player)
        self.say("Outcome: ", outcome, "\n")

        if i == 4:
            self.final_scores()
        else:
            self.play_next_situation(i+1)

    def final_scores(self):
        """Play the final scores bit."""
        if self.player.current_point >= 41:
            print('CONGRATULATIONS!!!')
        if self.player.current_point <= 40:
            print('Oopsie...')
