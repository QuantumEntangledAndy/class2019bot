"""
The Jungle Survial Game.

Authours:  Thitaporn Petchpadoong
"""

from game import Game


class Jungle(Game):
    """The jungle game."""

    @classmethod
    def game_name(self):
        """Get unique game name used for selection no spaces."""
        return "jungle"

    @classmethod
    def description(self):
        """Get the game description."""
        return "Brave all the trials the jungle has to throw at you."

    def welcome(self):
        """Get a welcome message."""
        return ("Jungle!\nWhere monkies are the least of your worries\n"
                + "Authours:  Thitaporn Petchpadoong")

    def play(self):
        """Get the party started."""
        self.stage1()

    def gameOver(self):
        """End of the game."""
        self.say("Game Over. Start Again.")
        self.say("=" * 95)

    def stage1(self):
        """Play stage 1."""
        self.say("=" * 95)
        self.say("Welcome to the Jungle!!!")
        self.say("There are many dangerous creatures such as monkeys,"
                 + " hippos, tigers, and cannibals.")
        self.say("In order to survive in this jungle, you need to build"
                 + " a house to protect yourself from them.")
        self.score = 0
        self.say("Level 1: Build a house that will keep you away from"
                 + " the dangerous monkeys.")
        self.say("1. wood")
        self.say("2. hay")
        self.say("3. clay")
        self.choice("Your material?", ['wood', 'hay', 'clay'], self.answer1)

    def answer1(self, answer):
        """Answer for stage1."""
        answer = answer.lower()
        if answer == "wood":
            self.score += 3
        elif answer == "hay":
            self.score += 1
        elif answer == "clay":
            self.score += 2
        else:
            self.score += 0

        if self.score == 3:
            self.stage2()
        else:
            self.gameOver()

    def stage2(self):
        """Play stage2."""
        self.score = 0
        self.say("Level 2: Build a house that will keep you away"
                 + " from the aggressive hippos.")
        self.say("1. brick")
        self.say("2. wood")
        self.say("3. rock")
        self.choice("Your material?", ['brick', 'wood', 'rock'], self.answer2)

    def answer2(self, answer):
        """Answer to stage2."""
        if answer == "brick":
            self.score += 3
        elif answer == "wood":
            self.score += 1
        elif answer == "rock":
            self.score += 2
        else:
            self.score += 0

        if self.score == 3:
            self.stage3()
        else:
            self.gameOver()

    def stage3(self):
        """Play stage3."""
        self.score = 0
        self.say("Level 3.1 Build a house that will keep you away"
                 + " from the hungry tigers.")
        self.say("1. stainless steel")
        self.say("2. brick")
        self.say("3. concrete")
        self.say("4. gold")
        self.choice("Your material?", ['stainless_steel', 'brick',
                                       'concrete', 'gold'], self.answer3_1)

    def answer3_1(self, answer):
        """Answer for stage3.1."""
        if answer == "stainless_steel":
            self.score += 4
        elif answer == "brick":
            self.score += 1
        elif answer == "concrete":
            self.score += 2
        elif answer == "gold":
            self.score += 3
        else:
            self.score += 0
        self.say("Level 3.2 In order to survive from these hungry tigers,"
                 + "you need to choose your weapon.")
        self.say("1. saucepan")
        self.say("2. spears")
        self.say("3. bacon")
        self.choice("Your weapon?", ['saucepan', 'spears', 'bacon'],
                    self.answer3_2)

    def answer3_2(self, answer):
        """Answer for stage 3.2."""
        if answer == "spears":
            self.score += 3
        elif answer == "saucepan":
            self.score += 1
        elif answer == "bacon":
            self.score += 10
        else:
            self.score += 0

        if self.score >= 7:
            self.stage4()
        else:
            self.gameOver()

    def stage4(self):
        """Play stage4."""
        self.score = 0
        self.say("Level 4.1 Build a house that will keep you away from the"
                 + " savage cannibals")
        self.say("1. concrete")
        self.say("2. glass")
        self.say("3. stainless steel")
        self.say("4. gold")
        self.choice("Your material?", ['concrete', 'glass', 'stainless_steel',
                                       'gold'], self.answer4_1)

    def answer4_1(self, answer):
        """Answer for 4.1."""
        if answer == "concrete":
            self.score += 2
        elif answer == "glass":
            self.score += 1
        elif answer == "gold":
            self.score += 3
        elif answer == "stainless_steel":
            self.score += 4
        else:
            self.score += 0

        self.say("Level 4.2 In order to survive from these save cannibals,"
                 + " you need to choose your weapon.")
        self.say("1. carrots")
        self.say("2. shotguns")
        self.say("3. tennis bat")
        self.choice("Your weapon?", ['carrots', 'shotguns', 'tennis_bat'],
                    self.answer4_2)

    def answer4_2(self, answer):
        """Answer for 4.2."""
        if answer == "carrots":
            self.score += 1
        elif answer == "shotguns":
            self.score += 10
        elif answer == "tennis_bat":
            self.score += 2
        else:
            self.score += 0
        if self.score >= 6:
            self.say("Congrats! You win")
        else:
            self.gameOver()
