"""
The apocalypse game.

Authours: Surawat Chukaew
"""

# Protoype 2.2 final
import time
import random

TPP = '\033[32m'  # Purple Text
TBlue = '\033[34m'  # Blue Text
TYL = '\033[33m'  # Yellow Text
TRED = '\033[31m'  # Red Text


class Player():
    """The player class."""

    def __init__(self):
        """Create the player."""
        self.health = 100
        self.hungry = 4
        self.inventory = {}
        self.day = 1

    @property
    def health(self):
        """Get players health."""
        return self._health

    @property
    def hungry(self):
        """Get players hunger."""
        return self.hungry

    @hungry.setter
    def hungry(self, new_value):
        """Set players hunger."""
        self.hungry = new_value
        if self.hungry < 0:
            self.hungry = 0

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
        print(f'Your hungry is {self.hungry}')
        print(f'Your health is {self.health}')
        print("Your items are...")
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
            print("Youv'e got nothing")
        else:
            for item in self.inventory:
                count = self.inventory[item]
                print(f"You have {count} {item}(s)")


lazy = False


class Event():
    """The base event class."""

    def __init__(self):
        """Init the event."""
        self.times_event_occured = 0

    def say(self, message):
        """Say something to the player."""
        time.sleep(0)
        print(message)

    def choose(self, msg, options):
        """Select a choice."""
        if lazy:
            return list(options)[0]
        while True:
            print(msg)
            for idx, option in enumerate(options):
                print(f"{idx+1}: {option}")
            choice = input()
            for idx, option in enumerate(options):
                if choice == str(idx+1) or choice.lower() == option.lower():
                    return option

    def enter(self, player):
        """Enter the event."""
        raise NotImplementedError

    def ask_if_player_want_to_use_item(self, player):
        """Use an item."""
        msg = 'Do you want to use item?'
        answer = self.choose(msg, ['yes', 'no'])
        if answer == 'yes':
            msg = 'Which item?'

            if len(player.inventory) == 0:
                print("NO ITEMS YOU FOOL")
            else:
                answer = self.choose(msg, player.inventory.keys())
                if answer == 'food':
                    print("You ate it")
                    print("Yum")
                    player.remove_item('food')
                    player.hungry += 1
                    return "CONTINUE"
                elif answer == 'cat':
                    print("You petted the cat, it helped calm you down")
                    return "CONTINUE"
                elif answer == 'radio':
                    print("This sound good")
                    return "CONTINUE"
                elif answer == 'first aid kit':
                    print("You use first aid kit")
                    player.remove_item('first aid kit')
                    player.get_healed(90)
                    return "CONTINUE"


class Preparing(Event):
    """Event for preparing pre apocalypse."""

    def set_up(self):
        """Do the Intro."""
        print(TPP + "Today is apocalypse day")
        print("You have to choose your option wisely ")
        print("You have to survive for 7 days to win tihs")
        print("now")
        print("You hve to pick 3 item out of 7")
        print("which is food, video game, cat, gun, first aid kit, radio"
              + ", bird")

    def get_user_choice(self, person):
        """Ask player what they want."""
        msg = "What 1 item you want to choose?"

        start_item1 = self.choose(msg, ['food', 'video game', 'cat', 'gun',
                                        'first aid kit', 'radio', 'bird'])
        person.add_item(start_item1)

        msg = "What 2 item you want to choose?"

        start_item2 = self.choose(msg, ['food', 'video game', 'cat', 'gun',
                                        'first aid kit', 'radio', 'bird'])
        person.add_item(start_item2)
        print("")

        msg = "What 3 item you want to choose?"
        start_item3 = self.choose(msg, ['food', 'video game', 'cat', 'gun',
                                        'first aid kit', 'radio', 'bird'])

        person.add_item(start_item3)


class EveryDay(Event):
    """The dailty event."""

    def __init__(self):
        """Init the possibilites."""
        self.possible_events = [RobberyTurn(),
                                RadioactiveTurn(),
                                ZombieTurn(),
                                StressTurn(),
                                AndrewTurn(),
                                SendhelpTurn(),
                                MiceinvadeTurn()]
        self.explore_events = [Luckyday(),
                               Hopelessday(),
                               AttackedbyBandit()]

    def enter(self, player):
        """Do the event."""
        player.show_status()
        random_event = random.choice(self.possible_events)
        result = random_event.enter(player)
        if result == "DIED":
            return "YOU ARE DEAD"

        self.ask_if_player_want_to_use_item(player)
        answer = self.choose("Do you want to explore ?", ['yes', 'no'])
        if answer == 'yes':
            random_event = random.choice(self.explore_events)
            result = random_event.enter(player)
        elif answer == 'no':
            pass
        self.choose("You should sleep", ['sleep'])
        player.day += 1
        return "CONTINUE"


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
            return "CONTINUE"


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
        return "CONTINUE"


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
        return "CONTINUE"


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
        return "CONTINUE"


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
            return "VICTORY"
        else:
            self.say("He just come for visit and left")
        return "CONTINUE"


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
        return "CONTINUE"


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
        return "CONTINUE"


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
        return "CONTINUE"


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
        return "CONTINUE"


class AttackedbyBandit(Event):
    """Not so much attack more like free food day."""

    def enter(self, player):
        """Play the event."""
        self.say(TBlue + "You going to search in the forest behide"
                 + " your bunker")
        self.say("You look around and found a food can in the trash")
        player.add_item("food")
        player.add_item("food")


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


def game():
    """Run main game loop."""
    player = Player()
    event = Preparing()
    everyday = EveryDay()

    print(f"Day ... {player.day}")
    event.set_up()
    event.get_user_choice(player)

    for i in [1, 2, 3, 4, 5, 6]:
        player.get_hungry()
        result = everyday.enter(player)
        if result == "DIED":
            print("YOU ARE DEAD")
            return
        elif player.hungry == 0:
            Death_By_Hunger().enter(player)
            return

        elif player.health <= 0:
            Death_By_Health().enter(player)
            return

        print(f"Day ... {player.day}")
    print(TYL + "YOU WON")
