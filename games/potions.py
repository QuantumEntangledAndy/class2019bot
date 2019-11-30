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

class Player():

    def __init__(self):
        self.money = 10
        self.inventory = {}

    def has_item(self, item_name):
        if item_name in self.inventory:
            return True
        else:
            return False
    def add_item(self, name):
        item_count = self.inventory.get(name, 0)
        item_count += 1
        self.inventory[name] = item_count
    def remove_item(self, name):
        if self.has_item(name):
            item_count = self.inventory.get(name, 0)
            item_count -= 1
            self.inventory[name] = item_count
    def get_money(self, amount):
#        money_count = self.money.get(0)
        self.money += amount

    def loose_money(self, amount):
        self.money -= amount


import time
def say(message):
    time.sleep(0.0)
    print(message)
    pass

def get_player_choice(player):
    valid_choice = False
    while not valid_choice:
        choice = input()
        lower_case_choice = choice.lower()
        if lower_case_choice in ['mint']:
                player.add_item('mint')
                player.loose_money(2)
                print("Great choice!.")
                print("+Mint in your inventory")
                return False
        elif lower_case_choice in ['sage']:
                player.loose_money(2)
                player.add_item('sage')
                print("Great choice!.")
                print("+Sage in your inventory")
                return False
        elif lower_case_choice in ['thyme']:
                player.loose_money(2)
                player.add_item('thyme')
                print("Great choice!.")
                print("+Thyme in your inventory")
                return False
        else:
                print("Woah! seems like there is no such plant you choose in the option. Please select again.")

def get_player_choice2(player):
    valid_choice = False
    while not valid_choice:
        choice1 = input()
        lower_case_choice1 = choice1.lower()
        if lower_case_choice1 in ['yes']:
                print("Plants ($2): Mint, Sage, Thyme")
                get_player_choice(player)
                return False
        else:
                print("Okay! Seems like you are ready for making a potion.")
                return False

def potion_choice(player):
    p_choice = False
    while not p_choice:
        choice2 = input()
        lower_case_choice2 = choice2.lower()
        if lower_case_choice2 in ['red potion']:
            player.has_item('sage')
            player.add_item('red potion')
            player.remove_item('sage')
            print("+Red Potion in your inventory")
            print("Nice job!")
            return False
        elif lower_case_choice2 in ['blue potion']:
            player.has_item('mint')
            player.add_item('blue potion')
            player.remove_item('mint')
            print("+Blue Potion in your inventory")
            print("Nice job!")
            return False
        elif lower_case_choice2 in ['yellow potion']:
            player.has_item('thyme')
            player.add_item('yellow potion')
            player.remove_item('thyme')
            print("+Yellow Potion in your inventory")
            print("Nice job!")
            return False
        elif lower_case_choice2 in ['black potion']:
            player.has_item('sage')
            player.has_item('mint')
            player.has_item('thyme')
            player.add_item('black potion')
            player.remove_item('sage')
            player.remove_item('mint')
            player.remove_item('thyme')
            print("+Black Potion in your inventory")
            print("Nice job!")
            win_game(player)
            return False
        else:
            print("Uh oh, seems like you are lacking of ingredient. Please select or try again.")
            return True

def win_game(player):
    win = False
    while not win:
        if player.has_item('black potion'):
            print('Congratulations! You have beat the game and create the most rare potion, Black potion!')
            return False
        else:
            return True

player = Player()
say("You are the only human living in magical village named 'Odel'. You are planing to start a potion company eventhough you known you have a stronger competitor which are witches.")
say("Witches's potions are very tasty that people in the village dying to buy for. You want to stand out in this village too.")
say("Soon later, you open up your first company.")
say("You named your company as Gemini Potion.")
say("First, you need to pick a plant to create your potion.")
say("You have $10 as your first start.")
say("Plants ($2): Mint, Sage, Thyme")
say("Now, which plants will you select?")
get_player_choice(player)
say("Do you wish to buy more plant?")
say("Yes or No?")
get_player_choice2(player)
say("Now which potions do you want to make? The cost of potion that you could sell is shown after the potion name.")
say("Red potion $5 (ingredient required: Sage)")
say("Blue potion $5 (ingredient required: Mint)")
say("Yellow potion $5 (ingredient required: Thyme)")
say("Black potion $10 (ingredients required: Sage + Mint + Thyme)")
potion_choice(player)
