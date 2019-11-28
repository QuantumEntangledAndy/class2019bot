"""
The Dating Game.

Authours:  Nattamon Panichakul,
"""

class Player():
    def __init__(self):
        self.current_point = 0
        self.name = ""

    def add_point(self, amount):
        self.current_point += amount

class Situation():
    def __init__(self, situation, first_option, first_outcome, first_point, second_option, second_outcome, second_point):
        self.situation = situation
        self.first_option = first_option
        self.first_outcome = first_outcome
        self.first_point = first_point
        self.second_option = second_option
        self.second_outcome = second_outcome
        self.second_point = second_point

    def condition(self, selection, player):
        if selection == "1":
            player.add_point(self.first_point)
            return self.first_outcome
        if selection == "2":
            player.add_point(self.second_point)
            return self.second_outcome
        else:
            raise ValueError("Not a valid choice, please try again.")

    def final_condition(self, selection, player):
        if selection == "1":
            player.add_point(self.first_point)
        if selection == "2":
            player.add_point(self.second_point)

        if player.current_point >= 41:
            return self.first_outcome
        if player.current_point <= 40:
            return self.second_outcome

player = Player()
player.name = input("Enter your name: ")

print("The objective of this game is to find a girl, date her, and get her to say yes on your marriage proposal")

situations = []

situations.append(Situation("\n You need to choose a place to find that girl.", "Walk into a pub", "You found a girl", -5,"Walk along a busy street", "You found a girl", 10))

situations.append(Situation("What should you do to her?", "Buy her a drink", "She is pleased", 20,"Throw her some pick-up lines", "Things got awkward", -8))

situations.append(Situation("Choose what you're going to wear to the amusement park.", "A suit", "When she sees you, She says 'Looks handsome, you’re making my clothes look lacking.''", 13,"Dress casually.", "When sees you, she says, ‘Wow…(blush), lets go.’", 20))

situations.append(Situation("You get to talk to each other, spend some quality time and played lots of roller coasters. When the sun set, you looked into her eyes and mustered my courage to confess your love for her. Her answer is ‘Yes!’. She becomes my girlfriend, you kept in touch and planned for your next date. \n \n On a next date, you want to buy her a present. What should it be?", "A flower you decorated yourself", "She likes it a lot", 20,"An expensive ring and flower", "She feels uneasy and got confused. ", 10))

situations.append(Situation("After a year of dating, you decided to ask her to marry you.", "Promised her that you'll love her forever.", "SHE SAID YES", 10,"I will give you everything that you desires, I love you.", "SHE SAID NO", 15))

for i in range(0,5):
    print("",situations[i].situation,"\n")
    print("1.",situations[i].first_option)
    print("2.",situations[i].second_option, "\n")
    print("You choose: ", end = '')

    if i == 4:
         outcome = situations[i].final_condition(input(""),player)
    else:
        outcome = situations[i].condition(input(""),player)
    print("Outcome: ", outcome, "\n")



if player.current_point >= 41:
    print('CONGRATULATIONS!!!')
if player.current_point <= 40:
    print('Oopsie...')
