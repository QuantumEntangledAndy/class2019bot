"""
Quiz.

A simple quiz game with bonuses too.

Adapted to play on telegram by Andrew W King
"""

__author__ = "Tania Saisod and Suchujnun Uparipahk"
__copyright__ = "Copyright 2019, Chulalongkorn University"
__credits__ = ["Tania Saisod", "Suchujnun Uparipahk"]
__license__ = "AGPL"
__version__ = "1.0.0"
__maintainer__ = "Dr Andrew King"
__email__ = "sheepchaan@gmail.com"
__status__ = "Production"

from game import Game


class Quiz(Game):
    """The quiz game."""

    @classmethod
    def game_name(self):
        """Get unique game name used for selection no spaces."""
        return "quiz"

    @classmethod
    def description(self):
        """Get the game description."""
        return ("Play a simple quiz.")

    def welcome(self):
        """Get a welcome message."""
        return ("Quiz\nA simple quiz to test your brain.\n"
                + "Created by " + __author__)

    def question(self, level, prob):
        """self.say the question."""
        self.say("Level " + str(level) + ": " + prob + " = ?")

    def bonus(self):
        """Do the bonus question."""
        if self.bonus_num >= 0 and self.bonus_num < 3:
            q = ["What is the capital city of Thailand?",
                 "What clothing is always sad?",
                 "What two words contain thousands of letters?"]
            c = [["a: Bangkok ", "b: Phuket", "c: Krabi", "d:Pattaya"],
                 ["a:pajamas", "b:blue jean", "c:skirt", "d:socks"],
                 ["a: let ter", "b: thou sand", "c:post office", "d:good luck"]
                 ]
            self.say(f"Bonus {self.bonus_num+1:d}: {q[self.bonus_num]} = ?")
            for i in range(4):
                self.say(c[self.bonus_num][i])
            self.choice("Answer?", ['a', 'b', 'c', 'd'], self.bonus_check)
        else:
            self.next_question()

    def bonus_check(self, ch):
        """Check the bonus for correctness."""
        ans = ['a', 'b', 'c']
        if str(ch) == ans[self.bonus_num]:
            self.hp += 1
            self.say(f"Congrats, you won a bonus question. HP : {self.hp}")
        else:
            self.hp -= 1
        self.bonus_num += 1
        self.next_question()

    def alive(self):
        """Check if player is still here."""
        if (self.hp == 0):
            return False
        return True

    def show_choice(self, a, b, c, d):
        """Show the self.show_choices."""
        self.say("A: " + str(a))
        self.say("B: " + str(b))
        self.say("C: " + str(c))
        self.say("D: " + str(d))

    def check(self, ch, ans):
        """Check the correct answer."""
        if str(ch) == ans:
            self.say(f"Congrats HP : {self.hp}")
        else:
            self.hp -= 1
            self.say(f"Wrong! You have {self.hp} HP left")
        if self.hp == 1 and self.bonus_num < 3:
            self.bonus()
        else:
            self.next_question()

    def play(self):
        """Play the quiz."""
        self.say("(Instructions)")
        self.say("1.You have 5 chances")
        self.say("2.If your live is 3, you will have chance to answer"
                 + " bonus question")
        self.say("3.If your live is 0 = GAME OVER")
        self.choice("Type /begin to begin the game", ['begin'], self.begin)

    def begin(self, result=None):
        """Begin the quiz."""
        self.hp = 5
        self.bonus_num = 0
        self.question1()

    def question1(self, result=None):
        """Ask question 1."""
        self.question(1, "Which country produce most copper?")
        self.show_choice('China', 'Thailand', 'Brazil', 'USA')
        self.choice("Answer: ", ['a', 'b', 'c', 'd'], self.answer1)

    def answer1(self, ch):
        """Answer this question."""
        self.next_question = self.question2
        self.check(ch, 'd')

    def question2(self, result=None):
        """Ask question 2."""
        if (not self.alive()):
            self.say('You died!')
            self.choice('Do you want to restart(y/n) ?', ['yes', 'no'],
                        [self.begin, self.give_up])
            return
        self.question(2, "62-19+37")
        self.show_choice(70, 80, 90, 100)
        self.choice("Answer: ", ['a', 'b', 'c', 'd'], self.answer2)

    def answer2(self, ch):
        """Answer this question."""
        self.next_question = self.question3
        self.check(ch, 'b')

    def question3(self, result=None):
        """Ask question 1."""
        if (not self.alive()):
            self.say('You died!')
            self.choice('Do you want to restart(y/n) ?', ['yes', 'no'],
                        [self.begin, self.give_up])
            return
        self.question(3, "85+48-56")
        self.show_choice(76, 77, 87, 97)
        self.choice("Answer: ", ['a', 'b', 'c', 'd'], self.answer3)

    def answer3(self, ch):
        """Answer this question."""
        self.next_question = self.question4
        self.check(ch, 'b')

    def question4(self, result=None):
        """Ask question 1."""
        if (not self.alive()):
            self.say('You died!')
            self.choice('Do you want to restart(y/n) ?', ['yes', 'no'],
                        [self.begin, self.give_up])
            return
        self.question(4, "83-45+37")
        self.show_choice(75, 76, 85, 86)
        self.choice("Answer: ", ['a', 'b', 'c', 'd'], self.answer4)

    def answer4(self, ch):
        """Answer this question."""
        self.next_question = self.question5
        self.check(ch, 'a')

    def question5(self, result=None):
        """Ask question 1."""
        if (not self.alive()):
            self.say('You died!')
            self.choice('Do you want to restart(y/n) ?', ['yes', 'no'],
                        [self.begin, self.give_up])
            return
        self.question(5, "91-47-18")
        self.show_choice(25, 26, 35, 36)
        self.choice("Answer: ", ['a', 'b', 'c', 'd'], self.answer5)

    def answer5(self, ch):
        """Answer this question."""
        self.next_question = self.question6
        self.check(ch, 'b')

    def question6(self, result=None):
        """Ask question 1."""
        if (not self.alive()):
            self.say('You died!')
            self.choice('Do you want to restart(y/n) ?', ['yes', 'no'],
                        [self.begin, self.give_up])
            return
        self.question(6, "82-15+78")
        self.show_choice(125, 135, 145, 155)
        self.choice("Answer: ", ['a', 'b', 'c', 'd'], self.answer6)

    def answer6(self, ch):
        """Answer this question."""
        self.next_question = self.question7
        self.check(ch, 'c')

    def question7(self, result=None):
        """Ask question 1."""
        if (not self.alive()):
            self.say('You died!')
            self.choice('Do you want to restart(y/n) ?', ['yes', 'no'],
                        [self.begin, self.give_up])
            return
        self.question(7, "36+78-58")
        self.show_choice(46, 56, 66, 76)
        self.choice("Answer: ", ['a', 'b', 'c', 'd'], self.answer7)

    def answer7(self, ch):
        """Answer this question."""
        self.next_question = self.question8
        self.check(ch, 'b')

    def question8(self, result=None):
        """Ask question 1."""
        if (not self.alive()):
            self.say('You died!')
            self.choice('Do you want to restart(y/n) ?', ['yes', 'no'],
                        [self.begin, self.give_up])
            return
        self.question(8, "61-36+48")
        self.show_choice(71, 73, 75, 77)
        self.choice("Answer: ", ['a', 'b', 'c', 'd'], self.answer8)

    def answer8(self, ch):
        """Answer this question."""
        self.next_question = self.question9
        self.check(ch, 'b')

    def question9(self, result=None):
        """Ask question 1."""
        if (not self.alive()):
            self.say('You died!')
            self.choice('Do you want to restart(y/n) ?', ['yes', 'no'],
                        [self.begin, self.give_up])
            return
        self.question(9, "45+68+37")
        self.show_choice(150, 160, 170, 180)
        self.choice("Answer: ", ['a', 'b', 'c', 'd'], self.answer9)

    def answer9(self, ch):
        """Answer this question."""
        self.next_question = self.question10
        self.check(ch, 'a')

    def question10(self, result=None):
        """Ask question 1."""
        if (not self.alive()):
            self.say('You died!')
            self.choice('Do you want to restart(y/n) ?', ['yes', 'no'],
                        [self.begin, self.give_up])
            return
        self.question(10, "91-23+15")
        self.show_choice(80, 81, 82, 83)
        self.choice("Answer: ", ['a', 'b', 'c', 'd'], self.answer10)

    def answer10(self, ch):
        """Answer this question."""
        self.next_question = self.final
        self.check(ch, 'd')

    def final(self, result=None):
        """Do the final stretch."""
        if (not self.alive()):
            self.say('You died!')
            self.choice('Do you want to restart(y/n) ?', ['yes', 'no'],
                        [self.begin, self.give_up])
            return
        self.say('Congratulations! Game Completed!')
        self.goodbye()

    def give_up(self, result=None):
        """Do this on qive up."""
        self.say("Too bad, you can try again with /play")
        self.goodbye()
