"""
Math spirit.

Why ghosts should not like math.

Adapted to play on telegram by Andrew W King
"""


__author__ = "Atiwit Intarasorn"
__copyright__ = "Copyright 2019, Chulalongkorn University"
__credits__ = ["Atiwit Intarasorn"]
__license__ = "AGPL"
__version__ = "1.0.0"
__maintainer__ = "Dr Andrew King"
__email__ = "sheepchaan@gmail.com"
__status__ = "Production"

from game import Game


class MathSpirit(Game):
    """The math spirit game."""

    @classmethod
    def game_name(self):
        """Get unique game name used for selection no spaces."""
        return "math_spirit"

    @classmethod
    def description(self):
        """Get the game description."""
        return (
            "What happens if your math class is haunted... Better not"
            + " to know"
        )

    def welcome(self):
        """Get a welcome message."""
        return (
            "Math Spirit\nThe worse type of spirit is one that loves"
            + " math\n"
            + "Created by "
            + __author__
        )

    def question(self, level, prob):
        """Display a question to the user."""
        self.say(f"Level {level:d}: {prob} = ?")

    def bonus(self, next_question):
        """Do the bonus question."""
        q = ["(120/6)+78", "(91-25)/11", "(34+47)/9"]
        c = [
            ["A: 95", "B: 96", "C: 97", "D: 98"],
            ["A: 5", "B: 6", "C: 7", "D: 8"],
            ["A: 9", "B: 10", "C: 11", "D: 12"],
        ]
        if self.bonus_num < 3 and self.bonus_num >= 0:
            self.say(f"Bonus {self.bonus_num:d}: {q[self.bonus_num]} = ?")
            for i in range(4):
                self.say(c[self.bonus_num][i])
            self.next_question = next_question
            self.choice("Answer?", ["a", "b", "c", "d"], self.bonus_answer)
        else:
            self.say("There are no more bonus questons!")
            next_question()

    def bonus_answer(self, ch):
        """Handle the bonus answer."""
        ans = ["d", "b", "a"]
        if str(ch) == ans[self.bonus_num]:
            self.hp += 1
            self.say(f"Congrats, you won a bonus question. HP : {self.hp:d}")
        else:
            self.hp -= 1
        self.bonus_num += 1
        self.next_question()

    def alive(self):
        """Check if player is alive."""
        if self.hp == 0:
            return False
        return True

    def show_choice(self, a, b, c, d):
        """Display the choices."""
        self.say("A: " + str(a))
        self.say("B: " + str(b))
        self.say("C: " + str(c))
        self.say("D: " + str(d))

    def check(self, ch, ans, next_question):
        """Check for correct answer."""
        if str(ch) == ans:
            self.say(f"Congrats HP : {self.hp:d}")
        else:
            self.hp -= 1
            self.say(f"Wrong! You have {self.hp:d} HP left")
        if self.hp == 1 and self.bonus_num < 3:
            self.bonus(next_question)
        else:
            next_question()

    def play(self):
        """Play the game."""
        self.say(
            "In the middle of the town they was a very old school"
            + " with a magical look. One day in late night one boy"
            + " he forgets his bag in the class so he have to go"
            + " back to the school .When the boy arrived to the"
            + " school he went up to his class but there was"
            + " something wrong with the school’s atmosphere."
            + " The air was cold, the lights was blinking,the place"
            + " was very quite so he can  here his heartbeat he"
            + " keep walking through the hallway till he see his"
            + " class and he went in. The boy was in the class with"
            + " a weird feeling. He thinks that school in daytime"
            + " and in nighttime was completely different suddenly"
            + " the door was close with a very loud noise. At that"
            + " time they are the mist around the blackboard after"
            + " the mist disappear they have something written on"
            + " the board. “If you want to be out of this class you"
            + " have to answer 10 questions.” The boy read it in his"
            + " mind and when he glanced back up to the board the"
            + " letter was changed. “You have 5 chance. After you"
            + " answer it wrong your chance will be deduct.” After"
            + " reading the boy thinks that what if his chance runs"
            + " out what will be happen. The letter on the board"
            + " change again. “If your chance goes to 1 we will"
            + " have an extra help for you so let’s start.” After"
            + " that letter on the board disappears all the locks"
            + " from door and windows start to lock by itself. The"
            + " boy was shocked. “The first question is ...”"
        )
        self.say(
            "You have 5 lives if you anwer wrong your live will be"
            + " deduct."
        )
        self.say(
            "The game is not that hard, you will have a chance to"
            + " answer bonus question if your lives = 1"
        )
        self.say("Good Luck")
        self.choice(
            "Type /begin to begin a game: ", ["begin"], self.post_rules
        )

    def post_rules(self, reply=None):
        """Play post rules."""
        self.say("------BEGIN------")
        self.hp = 5
        self.bonus_num = 0
        self.question(1, "59+87+48")
        self.show_choice(174, 184, 194, 204)
        self.choice("Answer?", ["a", "b", "c", "d"], self.answer1)

    def answer1(self, ch):
        """Reply to question 1."""
        self.check(ch, "d", self.question2)

    def question2(self):
        """Question2."""
        if not self.alive():
            self.say("You died!")
            self.choice(
                "Do you want to restart(y/n) ? ",
                ["yes", "no"],
                [self.post_rules, self.end_game],
            )
            return
        self.question(2, "62-19+37")
        self.show_choice(70, 80, 90, 100)
        self.choice("Answer?", ["a", "b", "c", "d"], self.answer2)

    def answer2(self, ch):
        """Reply to question2."""
        self.check(ch, "b", self.question3)

    def question3(self):
        """Question3."""
        if not self.alive():
            self.say("You died!")
            self.choice(
                "Do you want to restart(y/n) ? ",
                ["yes", "no"],
                [self.post_rules, self.end_game],
            )
            return
        self.question(3, "85+48-56")
        self.show_choice(76, 77, 87, 97)
        self.choice("Answer?", ["a", "b", "c", "d"], self.answer3)

    def answer3(self, ch):
        """Reply to question3."""
        self.check(ch, "b", self.question4)

    def question4(self):
        """Question4."""
        if not self.alive():
            self.say("You died!")
            self.choice(
                "Do you want to restart(y/n) ? ",
                ["yes", "no"],
                [self.post_rules, self.end_game],
            )
            return
        self.question(4, "83-45+37")
        self.show_choice(75, 76, 85, 86)
        self.choice("Answer?", ["a", "b", "c", "d"], self.answer4)

    def answer4(self, ch):
        """Reply to question4."""
        self.check(ch, "a", self.question5)

    def question5(self):
        """Question5."""
        if not self.alive():
            self.say("You died!")
            self.choice(
                "Do you want to restart(y/n) ? ",
                ["yes", "no"],
                [self.post_rules, self.end_game],
            )
            return
        self.question(5, "91-47-18")
        self.show_choice(25, 26, 35, 36)
        self.choice("Answer?", ["a", "b", "c", "d"], self.answer5)

    def answer5(self, ch):
        """Reply to question5."""
        self.check(ch, "b", self.question6)

    def question6(self):
        """Question6."""
        if not self.alive():
            self.say("You died!")
            self.choice(
                "Do you want to restart(y/n) ? ",
                ["yes", "no"],
                [self.post_rules, self.end_game],
            )
            return
        self.question(6, "82-15+78")
        self.show_choice(125, 135, 145, 155)
        self.choice("Answer?", ["a", "b", "c", "d"], self.answer6)

    def answer6(self, ch):
        """Reply to question6."""
        self.check(ch, "c", self.question7)

    def question7(self):
        """Question7."""
        if not self.alive():
            self.say("You died!")
            self.choice(
                "Do you want to restart(y/n) ? ",
                ["yes", "no"],
                [self.post_rules, self.end_game],
            )
            return
        self.question(7, "36+78-58")
        self.show_choice(46, 56, 66, 76)
        self.choice("Answer?", ["a", "b", "c", "d"], self.answer7)

    def answer7(self, ch):
        """Reply to question7."""
        self.check(ch, "b", self.question8)

    def question8(self):
        """Question8."""
        if not self.alive():
            self.say("You died!")
            self.choice(
                "Do you want to restart(y/n) ? ",
                ["yes", "no"],
                [self.post_rules, self.end_game],
            )
            return
        self.question(8, "61-36+48")
        self.show_choice(71, 73, 75, 77)
        self.choice("Answer?", ["a", "b", "c", "d"], self.answer8)

    def answer8(self, ch):
        """Reply to question8."""
        self.check(ch, "b", self.question9)

    def question9(self):
        """Question2."""
        if not self.alive():
            self.say("You died!")
            self.choice(
                "Do you want to restart(y/n) ? ",
                ["yes", "no"],
                [self.post_rules, self.end_game],
            )
            return
        self.question(9, "45+68+37")
        self.show_choice(150, 160, 170, 180)
        self.choice("Answer?", ["a", "b", "c", "d"], self.answer9)

    def answer9(self, ch):
        """Reply to question9."""
        self.check(ch, "a", self.question10)

    def question10(self):
        """Question10."""
        if not self.alive():
            self.say("You died!")
            self.choice(
                "Do you want to restart(y/n) ? ",
                ["yes", "no"],
                [self.post_rules, self.end_game],
            )
            return
        self.question(10, "91-23+15")
        self.show_choice(80, 81, 82, 83)
        self.choice("Answer?", ["a", "b", "c", "d"], self.answer10)

    def answer10(self, ch):
        """Reply to question10."""
        self.check(ch, "d", self.victory)

    def victory(self):
        """Do the last stretch."""
        if not self.alive():
            self.say("You died!")
            self.choice(
                "Do you want to restart(y/n) ? ",
                ["yes", "no"],
                [self.post_rules, self.end_game],
            )
            return
        self.say("Congratulations! You made it out of the room!")
        self.goodbye()

    def end_game(self, reply=None):
        """When they quit do this."""
        self.say(
            "Some one will come and help you escape from the math"
            + " eventually... right.... right????"
        )
        self.goodbye()
