"""
Potions.

Try and be the best potion brewer.
"""

__author__ = "Arraya Tanyanurak"
__copyright__ = "Copyright 2019, Chulalongkorn University"
__credits__ = ["Arraya Tanyanurak"]
__license__ = "AGPL"
__version__ = "1.0.0"
__maintainer__ = "Dr Andrew King"
__email__ = "sheepchaan@gmail.com"
__status__ = "Production"

from game import Game


class Player():
    """Holds player data."""

    def __init__(self):
        """Create the player."""
        self.money = 10
        self.inventory = {}

    def has_item(self, item_name):
        """Check if player has item."""
        if item_name in self.inventory:
            return True
        else:
            return False

    def add_item(self, name):
        """Add item to the player."""
        item_count = self.inventory.get(name, 0)
        item_count += 1
        self.inventory[name] = item_count

    def remove_item(self, name):
        """Remove item from the player."""
        if self.has_item(name):
            item_count = self.inventory.get(name, 0)
            item_count -= 1
            self.inventory[name] = item_count

    def get_money(self, amount):
        """Add money to the player."""
        self.money += amount

    def loose_money(self, amount):
        """Make the player loose money."""
        self.money -= amount


class Potions(Game):
    """The potions game itself."""

    @classmethod
    def game_name(self):
        """Get unique game name used for selection no spaces."""
        return "potions"

    @classmethod
    def description(self):
        """Get the game description."""
        return ("Be the best potion brewer in your village.")

    def welcome(self):
        """Get a welcome message."""
        return ("Potions\nCan you impress the village with your potion"
                + " brewing skills.\n"
                + "Created by " + __author__)

    def get_player_choice(self):
        """Get the players choice of plant."""
        self.choice("What will you pick?", ['mint', 'sage', 'thyme'],
                    self.act_player_choice)

    def act_player_choice(self, choice):
        """Act on players plant choice."""
        player = self.player
        lower_case_choice = choice.lower()
        if lower_case_choice in ['mint']:
            player.add_item('mint')
            player.loose_money(2)
            self.say("Great choice!.")
            self.say("+Mint in your inventory")
        elif lower_case_choice in ['sage']:
            player.loose_money(2)
            player.add_item('sage')
            self.say("Great choice!.")
            self.say("+Sage in your inventory")
        elif lower_case_choice in ['thyme']:
            player.loose_money(2)
            player.add_item('thyme')
            self.say("Great choice!.")
            self.say("+Thyme in your inventory")
        self.callback()

    def get_player_choice2(self):
        """Get the players next choice."""
        self.choice("Will you?", ['yes', 'no'], self.act_player_choice2)

    def act_player_choice2(self, choice1):
        """Act on asking to buy more."""
        lower_case_choice1 = choice1.lower()
        if lower_case_choice1 in ['yes']:
            self.say("Plants ($2): Mint, Sage, Thyme")
            self.callback = self.get_player_choice2
            self.get_player_choice()
        else:
            self.say("Okay! Seems like you are ready for making a potion.")
            self.callback2()

    def potion_choice(self):
        """Get players potion choice."""
        self.choice("What do you want to make?", ['red potion', 'blue potion',
                                                  'yellow potion',
                                                  'black potion'],
                    self.act_potion_choice)

    def act_potion_choice(self, choice2):
        """Act on chosen potion."""
        lower_case_choice2 = choice2.lower()
        if lower_case_choice2 in ['red potion']:
            self.player.has_item('sage')
            self.player.add_item('red potion')
            self.player.remove_item('sage')
            self.say("+Red Potion in your inventory")
            self.say("Nice job!")
            self.loose_game()
        elif lower_case_choice2 in ['blue potion']:
            self.player.has_item('mint')
            self.player.add_item('blue potion')
            self.player.remove_item('mint')
            self.say("+Blue Potion in your inventory")
            self.say("Nice job!")
            self.loose_game()
        elif lower_case_choice2 in ['yellow potion']:
            self.player.has_item('thyme')
            self.player.add_item('yellow potion')
            self.player.remove_item('thyme')
            self.say("+Yellow Potion in your inventory")
            self.say("Nice job!")
            self.loose_game()
        elif lower_case_choice2 in ['black potion']:
            self.player.has_item('sage')
            self.player.has_item('mint')
            self.player.has_item('thyme')
            self.player.add_item('black potion')
            self.player.remove_item('sage')
            self.player.remove_item('mint')
            self.player.remove_item('thyme')
            self.say("+Black Potion in your inventory")
            self.say("Nice job!")
            self.win_game()

    def win_game(self):
        """Win the game, or not."""
        self.say('Congratulations! You have impressed the village by'
                 + ' createing the most rare potion, Black potion!'
                 + ' You have  beaten the game')

    def loose_game(self):
        """Loose the game."""
        self.say("Unfortunatly this potion was not good enough to"
                 + " impress the village")

    def play(self):
        """Play the game."""
        self.player = Player()
        self.say("You are the only human living in magical village named"
                 + " 'Odel'. You are planing to start a potion company even"
                 + " though you known you have a stronger competitor which"
                 + " are witches.")
        self.say("Witches's potions are very tasty that people in the"
                 + " village dying to buy for. You want to stand out in this"
                 + " village too.")
        self.say("Soon later, you open up your first company.")
        self.say("You named your company as Gemini Potion.")
        self.say("First, you need to pick a plant to create your potion.")
        self.say("You have $10 as your first start.")
        self.say("Plants ($2): Mint, Sage, Thyme")
        self.say("Now, which plants will you select?")
        self.callback = self.stage2
        self.get_player_choice()

    def stage2(self, result=None):
        """Play stage 2."""
        self.say("Do you wish to buy more plant?")
        self.say("Yes or No?")
        self.callback2 = self.stage3
        self.get_player_choice2()

    def stage3(self, result=None):
        """Play stage3."""
        self.say("Now which potions do you want to make? The cost of potion"
                 + " that you could sell is shown after the potion name.")
        self.say("Red potion $5 (ingredient required: Sage)")
        self.say("Blue potion $5 (ingredient required: Mint)")
        self.say("Yellow potion $5 (ingredient required: Thyme)")
        self.say("Black potion $10 (ingredients required: Sage + Mint +"
                 + " Thyme)")
        self.potion_choice()
