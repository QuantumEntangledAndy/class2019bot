"""
The apocalypse game.

Authours: Surawat Chukae,  Watcharaphol Vongnoi, Narutchai Arunrattananukul,
          Peemapat Jumrusprasert

Adapted to play on telegram by Andrew W King
"""

__author__ = ("Surawat Chukae,  Watcharaphol Vongnoi,"
              + " Narutchai Arunrattananukul and Peemapat Jumrusprasert")
__copyright__ = "Copyright 2019, Chulalongkorn University"
__credits__ = ["Surawat Chukae",  "Watcharaphol Vongnoi",
               "Narutchai Arunrattananukul", "Peemapat Jumrusprasert"]
__license__ = "AGPL"
__version__ = "2.2.0"
__maintainer__ = "Dr Andrew King"
__email__ = "sheepchaan@gmail.com"
__status__ = "Production"

# Protoype 2.2 final
import random
from game import Game

TPP = ''  # Purple Text
TBlue = ''  # Blue Text
TYL = ''  # Yellow Text
TRED = ''  # Red Text


class Player():
    """The player class."""

    def __init__(self, bot):
        """Create the player."""
        self.health = 100
        self.hungry = 4
        self.inventory = {}
        self.day = 1
        self.bot = bot

    def say(self, message):
        """Pass saying onto bot."""
        self.bot.say(message)

    def choose(self, message, options, callbacks):
        """Pass choices onto bot."""
        self.bot.choice(message, options, callbacks)

    @property
    def health(self):
        """Get players health."""
        return self._health

    @property
    def hungry(self):
        """Get players hunger."""
        return self._hungry

    @hungry.setter
    def hungry(self, new_value):
        """Set players hunger."""
        self._hungry = new_value
        if self._hungry < 0:
            self._hungry = 0

    @health.setter
    def health(self, new_value):
        """Set player health."""
        self._health = new_value
        if self._health > 100:
            self._health = 100
        elif self._health < 0:
            self._health = 0

    def has_item(self, item_name):
        """Check if player has an item."""
        if item_name in self.inventory:
            return True
        else:
            return False

    def add_item(self, name):
        """Add an item to the player."""
        item_count = self.inventory.get(name, 0)
        item_count += 1
        self.inventory[name] = item_count

    def remove_item(self, name):
        """Remove an item from the player."""
        if self.has_item(name):
            item_count = self.inventory.get(name, 0)
            item_count -= 1
            self.inventory[name] = item_count
            if item_count == 0:
                del self.inventory[name]

    def get_item(self, name):
        """Get players item count."""
        item_count = self.inventory.get(name, 0)
        return item_count

    def show_status(self):
        """Show players stats."""
        self.say(f'Your hungry is {self.hungry}')
        self.say(f'Your health is {self.health}')
        self.say("Your items are...")
        self.show_inventory()

    def get_damaged(self, amount):
        """Damage the player."""
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def get_healed(self, amount):
        """Heal the player."""
        self.health += amount
        if self.health > 100:
            self.health = 100

    def day_pass(self):
        """Make a day pass."""
        self.day += 1

    def get_hungry(self):
        """Get the players hunger."""
        self.hungry -= 1

    def show_inventory(self):
        """Show the player's inventory."""
        if not self.inventory:
            self.say("Youv'e got nothing")
        else:
            for item in self.inventory:
                count = self.inventory[item]
                self.say(f"You have {count} {item}(s)")


class Event():
    """The base event class."""

    def __init__(self, bot):
        """Init the event."""
        self.times_event_occured = 0
        self.bot = bot

    def say(self, message):
        """Pass saying onto bot."""
        self.bot.say(message)

    def choose(self, message, options, callbacks):
        """Pass choices onto bot."""
        self.bot.choice(message, options, callbacks)

    def enter(self, player):
        """Enter the event."""
        raise NotImplementedError

    def ask_if_player_want_to_use_item(self, player, callback):
        """Use an item."""
        msg = 'Do you want to use item?'
        self.player = player
        self.callback = callback
        self.choose(msg, ['yes', 'no'], self.use_that_item_result)

    def use_that_item_result(self, answer):
        """Act on user's reply."""
        if answer == 'yes':
            msg = 'Which item?'

            if len(self.player.inventory) == 0:
                self.say("NO ITEMS YOU FOOL")
                self.callback("CONTINUE")
            else:
                items = [item.replace(" ", "_") for item in
                         self.player.inventory.keys()]
                self.choose(msg, items,
                            self.the_chosen_item)
        else:
            self.callback("CONTINUE")

    def the_chosen_item(self, answer):
        """Actual use it already."""
        answer = answer.replace("_", " ")
        if answer == 'food':
            self.say("You ate it")
            self.say("Yum")
            self.player.remove_item('food')
            self.player.hungry += 1
            self.callback("CONTINUE")
            return
        elif answer == 'cat':
            self.say("You petted the cat, it helped calm you down")
            self.callback("CONTINUE")
            return
        elif answer == 'radio':
            self.say("This sound good")
            self.callback("CONTINUE")
            return
        elif answer == 'first aid kit':
            self.say("You use first aid kit")
            self.player.remove_item('first aid kit')
            self.get_healed(90)
            self.callback("CONTINUE")
            return


class Preparing(Event):
    """Event for preparing pre apocalypse."""

    def set_up(self):
        """Do the Intro."""
        self.say(TPP + "Today is apocalypse day")
        self.say("You have to choose your option wisely ")
        self.say("You have to survive for 7 days to win tihs")
        self.say("now")
        self.say("You hve to pick 3 item out of 7")
        self.say("which is food, video game, cat, gun, first aid kit, radio"
                 + ", bird")

    def get_user_choice(self, person):
        """Ask player what they want."""
        msg = "What 1 item you want to choose?"
        self.person = person
        items = ['food', 'video_game', 'cat', 'gun', 'first_aid_kit', 'radio',
                 'bird']
        self.choose(msg, items, self.get_start_item1)

    def get_start_item1(self, start_item1):
        """Add the results item."""
        start_item1 = start_item1.replace("_", " ")
        self.person.add_item(start_item1)

        msg = "What 2 item you want to choose?"

        items = ['food', 'video_game', 'cat', 'gun', 'first_aid_kit', 'radio',
                 'bird']
        self.choose(msg, items, self.get_start_item2)

    def get_start_item2(self, start_item2):
        """Add the second item."""
        start_item2 = start_item2.replace("_", " ")
        self.person.add_item(start_item2)

        msg = "What 3 item you want to choose?"
        items = ['food', 'video_game', 'cat', 'gun', 'first_aid_kit', 'radio',
                 'bird']
        self.choose(msg, items, self.get_start_item3)

    def get_start_item3(self, start_item3):
        """Add the third item."""
        start_item3 = start_item3.replace("_", " ")
        self.person.add_item(start_item3)
        self.bot.post_get_user_choice("CONTINUE")


class EveryDay(Event):
    """The dailty event."""

    def __init__(self, bot):
        """Init the possibilites."""
        self.bot = bot
        self.possible_events = [RobberyTurn(self),
                                RadioactiveTurn(self),
                                ZombieTurn(self),
                                StressTurn(self),
                                AndrewTurn(self),
                                SendhelpTurn(self),
                                MiceinvadeTurn(self)]
        self.explore_events = [Luckyday(self),
                               Hopelessday(self),
                               AttackedbyBandit(self)]

    def enter(self, player):
        """Do the event."""
        player.show_status()
        self.player = player
        random_event = random.choice(self.possible_events)
        random_event.enter(player)

    def post_random_event(self, result):
        """Handle post random events here."""
        if result == "DIED":
            self.bot.post_everyday("DIED")
            return
        elif result == "VICTORY":
            self.bot.post_everyday("VICTORY")
            return

        self.ask_if_player_want_to_use_item(self.player, self.post_use_items)

    def post_use_items(self, result):
        """After using item."""
        self.choose("Do you want to explore ?", ['yes', 'no'], self.post_ask)

    def post_ask(self, answer):
        """Act on the reply."""
        player = self.player
        if answer == 'yes':
            random_event = random.choice(self.explore_events)
            random_event.enter(player)
        elif answer == 'no':
            self.post_explore("CONTINUE")

    def post_explore(self, result):
        """Do post explore event."""
        self.choose("You should sleep", ['sleep'], self.post_sleep)

    def post_sleep(self, result):
        """Do post sleep."""
        self.player.day += 1
        self.bot.post_everyday("CONTINUE")


# eventdaily
class RobberyTurn(Event):
    """A robber."""

    def enter(self, player):
        """Play the event."""
        self.times_event_occured += 1
        self.say("A robber knocks on the door and DEMANDS food or your LIFE")
        if player.has_item("food"):
            self.say("They force you to give them your food")
            self.say("you have no choice but give them food")
            player.remove_item("food")
        else:
            rand_event = random.randint(1, 3)
            if rand_event == 1:
                self.say("The robber cant find any hidden food so they"
                         + " shoot gun at you")
                player.get_damaged(40)
            elif rand_event == 2:
                self.say("They angry and punch you in the face")
                player.get_damaged(20)
            else:
                self.say("Today is your lucky day! They said")
        self.bot.post_random_event("CONTINUE")


class RadioactiveTurn(Event):
    """Adding insult to injury."""

    def enter(self, player):
        """Play the event."""
        self.say("The military drop the radioactive bomb around the city")
        self.say("The effect of the bomb made you sick ")
        if player.has_item("first aid kit"):
            self.say("You have pick up a first aid kit to heal from swallow"
                     + " the radioactive")
            player.remove_item("first aid kit")
            self.say("You safe for now")
        else:
            rand_event = random.randint(1, 3)
            if rand_event == 1:
                self.say("You swallow too much")
                player.get_damaged(40)
            elif rand_event == 2:
                self.say("You swallow too much")
                player.get_damaged(20)
            else:
                self.say("You lucky enough to not get hurt")
        self.bot.post_random_event("CONTINUE")


class ZombieTurn(Event):
    """I blame umbrella inc."""

    def enter(self, player):
        """Play the event."""
        self.say("A mass of zombie run to your basement")
        if player.has_item("gun"):
            self.say("You have pick up a gun to defend yourself")
            player.remove_item("gun")
            self.say("You safe for now")
        else:
            rand_event = random.randint(1, 3)
            if rand_event == 1:
                self.say("Zombie bite you")
                player.get_damaged(40)
            elif rand_event == 2:
                self.say("You swallow too much")
                player.get_damaged(20)
            else:
                self.say("You fight with your bare hand and defend"
                         + " your basement")
        self.bot.post_random_event("CONTINUE")


class StressTurn(Event):
    """Gaming will save your life."""

    def enter(self, player):
        """Play the event."""
        self.say("You have being stress too much because you are alone")
        if player.has_item("video game"):
            self.say("You have pick up a video game to get the stress out")
            player.remove_item("video game")
            self.say("You happy now ")
        else:
            rand_event = random.randint(1, 3)
            if rand_event == 1:
                self.say("you hurt yourself")
                player.get_damaged(20)
            elif rand_event == 2:
                self.say("You sad enough to get sick")
                player.get_damaged(10)
            else:
                self.say("you think about good thing noting happend")
        self.bot.post_random_event("CONTINUE")


class AndrewTurn(Event):
    """Cat's are the best."""

    def enter(self, player):
        """Play the event."""
        self.say("Andrew came with a shotgun and knock the door")
        self.say("Andrew ask for cat")
        if player.has_item("cat"):
            self.say("You give him a cat")
            player.remove_item("cat")
            self.say("Andrew love that you give him a cat so he give"
                     + "you A grade")
            self.bot.post_random_event("VICTORY")
        else:
            self.say("He just come for visit and left")
        self.bot.post_random_event("CONTINUE")


class SendhelpTurn(Event):
    """Pigion mail."""

    def enter(self, player):
        """Play the event."""
        self.say("You think about asking for help using bird")
        if player.has_item("bird"):
            self.say("You have pick up a bird to take a letter"
                     + " to ask for help")
            player.remove_item("bird")
            self.say("Someone knock your door and give you food")
            player.add_item("food")
        else:
            self.say("But you dont have bird")
        self.bot.post_random_event("CONTINUE")


class MiceinvadeTurn(Event):
    """Again cat's are the best."""

    def enter(self, player):
        """Play the event."""
        self.say("A mass of mice came out from the drain")
        if player.has_item("cat"):
            self.say("You have pick up a cat to chase the mice")
            player.remove_item("cat")
            self.say("cat fight a mice for you")
        else:
            rand_event = random.randint(1, 3)
            if rand_event == 1:
                self.say("you really hate mice and it attack you while"
                         + " you sleeping")
                player.get_damaged(90)
            elif rand_event == 2:
                self.say("it bite your finger when you try to pet it")
                player.get_damaged(20)
            else:
                self.say("mice leave after they find your basement is boiring")
        self.bot.post_random_event("CONTINUE")


# expolre
class Luckyday(Event):
    """Are you feeling lucky..."""

    def enter(self, player):
        """Play the event."""
        self.say(TBlue + "You are going to explore the police station near"
                 + " your bunker")
        self.say("You noticed that there were a armory and supplies under"
                 + " the police station")
        self.say("When you have reached there you have found a gun, radio,"
                 + " first aid kit, food")
        player.add_item("food")
        player.add_item("gun")
        player.add_item("radio")
        player.add_item("first aid kit")
        self.bot.post_explore("CONTINUE")


class Hopelessday(Event):
    """Today is not your day."""

    def enter(self, player):
        """Play the event."""
        self.say(TBlue + "There are the mall in the east of your bunker")
        self.say("When you arrived there, you walk around and"
                 + " looking for food")
        self.say("You keep searching for food")
        self.say("But nothing there")
        self.say("You decided to go back home woth empty bag")
        self.bot.post_explore("CONTINUE")


class AttackedbyBandit(Event):
    """Not so much attack more like free food day."""

    def enter(self, player):
        """Play the event."""
        self.say(TBlue + "You going to search in the forest behide"
                 + " your bunker")
        self.say("You look around and found a food can in the trash")
        player.add_item("food")
        player.add_item("food")
        self.bot.post_explore("CONTINUE")


class Death_By_Hunger(Event):
    """This is why you need to eat."""

    def enter(self, player):
        """Play the event."""
        self.say(TRED + "You look to eat, but find that you have no food...")
        self.say("Death is inevitable now")


class Death_By_Health(Event):
    """You should have gotten the cat."""

    def enter(self, player):
        """Play the event."""
        self.say(TRED + "You die")


class Apocalypse(Game):
    """The Apocalypse game."""

    @classmethod
    def game_name(self):
        """Get unique game name used for selection no spaces."""
        return "apocalypse"

    @classmethod
    def description(self):
        """Get the game description."""
        return "Can you survive the end of the world?"

    def welcome(self):
        """Get a welcome message."""
        return ("Apocalypse\nThe end of the world. Zombies included\n"
                + "Created by " + __author__)

    def play(self):
        """Start playing."""
        self.game()

    def game(self):
        """Run main game."""
        self.player = Player(self)
        self.event = Preparing(self)
        self.everyday = EveryDay(self)
        self.i = 1

        self.say(f"Day ... {self.player.day}")
        self.event.set_up()
        self.event.get_user_choice(self.player)

    def post_get_user_choice(self, result):
        """Do post setup."""
        if self.i < 7:
            self.i += 1
            self.player.get_hungry()
            self.everyday.enter(self.player)
            return
        else:
            self.say(TYL + "YOU WON")

    def post_everyday(self, result):
        """Do post everyday stuff."""
        if result == "DIED":
            self.say("YOU ARE DEAD")
            return
        elif result == "VICTORY":
            self.i = 100
            self.post_get_user_choice("CONTINUE")
        elif self.player.hungry == 0:
            Death_By_Hunger().enter(self.player)
            return

        elif self.player.health <= 0:
            Death_By_Health().enter(self.player)
            return

        self.say(f"Day... {self.player.day}")
        self.post_get_user_choice("CONTINUE")
