"""

Evil jeff Game.

Authours:  Kasin Onprasop
"""

import random
from game import Game


class Player():
    """Holds player data."""

    def __init__(self):
        """Init the player."""
        self.inventory = {}
        self.health = 100

    def has_item(self, item):
        """Check for item."""
        item_count = self.inventory.get(item, 0)
        if item_count > 0:
            return True
        else:
            return False

    def add_item(self, item):
        """Add item to player."""
        item_count = self.inventory.get(item, 0)
        self.inventory[item] = item_count + 1

    def remove_item(self, item):
        """Remove item from the player."""
        if self.has_item(item):
            item_count = self.inventory.get(item, 0)
            self.inventory[item] = item_count - 1

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


class Event():
    """Event base class."""

    def __init__(self, bot):
        """Init the event with times event occured."""
        self.times_event_occured = 0
        self.bot = bot

    def say(self, message):
        """Pass saying onto bot."""
        self.bot.say(message)

    def choose(self, message, options, callbacks):
        """Pass choices onto bot."""
        self.bot.choice(message, options, callbacks)

    def enter(self, player):
        """Enter the room handelled by child classes."""
        raise NotImplementedError


class NothingMuch(Event):
    """Nothing happends event."""

    def enter(self, player):
        """Enter the event."""
        self.say("You keep walking in the hallway of the Evil"
                 + " Jeff’s Castle")
        self.say("You saw nothing but doors, which you don’t"
                 + " know what’s inside")
        self.say("However, you can only keep walking, and hope"
                 + " for the princess’s safeness")
        self.times_event_occured += 1
        return "CONTINUE"


class LootboxKey(Event):
    """Find a lootable box."""

    def enter(self, player):
        """Enter the event."""
        if not player.has_item("Lootbox Key"):
            self.say("You went into a room full of monsters and a loot box")
            self.say("However, you are the hero so defeat all of them")
            self.say("You found the key inside the loot box!")
            player.add_item("Lootbox Key")
        else:
            self.say("You went into a room full of monsters.")
            self.say("You defeat them all!")
            self.say("You continue with your journey to save the princess…")
        self.times_event_occured += 1
        return "CONTINUE"


class SwordofMirai(Event):
    """Find the sword of Mirai."""

    def enter(self, player):
        """Enter the event."""
        if player.has_item("Lootbox Key"):
            player.remove_item("Lootbox Key")
            player.add_item("Sword of Mirai")
            self.say("You founded the Sword of Mirai in the"
                     + " locked loot chest!")
            self.say("This is the only sword that can be used"
                     + " to defeat Evil Jeff!")
            self.say("Only you can defeat Evil Jeff and save"
                     + " the princess!")
        else:
            self.say("You keep walking.")
        self.times_event_occured += 1
        return "CONTINUE"


class MonsterRoom1(Event):
    """A monster room."""

    def enter(self, player):
        """Enter the event."""
        self.say("You have entered a room full of monsters!")
        self.say("You was able to defeat all monsters!")
        self.say("However, you suffer from major damage!")
        player.get_damaged(20)
        self.times_event_occured += 1
        return "CONTINUE"


class MonsterRoom2(Event):
    """A monster room."""

    def enter(self, player):
        """Enter the event."""
        self.say("You have entered a room full of monsters!")
        self.say("You was able to defeat all monsters!")
        self.say("However, you suffer from minor damage!")
        player.get_damaged(10)
        self.times_event_occured += 1
        return "CONTINUE"


class MonsterRoom3(Event):
    """A monster room."""

    def enter(self, player):
        """Enter the event."""
        self.say("You have entered a room full of monsters!")
        self.say("You was able to defeat all monsters!")
        self.say("You did not suffer any damage!")
        self.times_event_occured += 1
        return "CONTINUE"


class Healing(Event):
    """A monster room."""

    def enter(self, player):
        """Enter the event."""
        self.say("On your way, you found the fountain of youth.")
        self.say("You drank the water from the fountain and gain"
                 + " some healing!")
        self.say("You continue with your journey feeling refresh.")
        player.get_healed(40)
        self.times_event_occured += 1
        return "CONTINUE"


class HealthPotion(Event):
    """Find health potion."""

    def enter(self, player):
        """Enter the event."""
        if not player.has_item("Health potion"):
            self.say("You found a health potion on the floor!")
            self.say("You pick it up and save it for later.")
            self.say("You continue your journey with hope.")
            player.add_item("Health potion")
        else:
            self.say("You found a health potion on the floor!")
            self.say("But you already have it, so you won't need it.")
            self.say("You continue walking.")
        self.times_event_occured += 1
        return "CONTINUE"


class UseHealthPotion(Event):
    """Use the health potion."""

    def enter(self, player):
        """Enter the event."""
        if player.has_item("Health potion"):
            player.remove_item("Health potion")
            player.get_healed(20)
            self.say("You drank the health potion and you felt revive!")
            self.say("You continue your journey feeling refresh!")
        else:
            self.say("You feel tired but you don't have any health potion.")
            self.say("You keep walking along the hallway.")
        self.times_event_occured += 1
        return "CONTINUE"


class MiniBoss(Event):
    """A miniboss fight."""

    def enter(self, player):
        """Enter the event."""
        if not player.has_item("Boss room key"):
            self.say("You have entered a \'Mini Boss\' room!")
            self.say("You was able to defeat the mini boss!")
            self.say("However, you suffer from major damage!")
            player.get_damaged(50)
            player.add_item("Boss room key")
            self.say("You continue with your journey to save the princess...")
        else:
            self.say("You went into a room full of monsters!")
            self.say("You defeat them all!")
            self.say("You continue with your journey to save the princess...")
        self.times_event_occured += 1
        return "CONTINUE"


class EvilJeff(Event):
    """The final showdown."""

    def enter(self, player):
        """Enter the event."""
        self.say("You've confronted with a big, scary door!")
        self.say("It must be where Evil Jeff kept the princess!")
        self.say("However, the door is locked!")
        if player.has_item("Boss room key"):
            self.say("Luckily, you,ve already found the key to open it.")
            self.player = player
            self.choice("Do you wish to enter the boss room?", ["Yes", "No"],
                        self.stage2)
        else:
            self.say("You don't have the key to enter the room.")
            self.say("You continue searching.")
            self.times_event_occured += 1
            return "CONTINUE"

    def stage2(self, answer):
        """Play stage 2 after the question."""
        player = self.player
        if answer == "Yes":
            self.say("WeLcOmE hErO oF tHe HuMaN tRiBe, My NaMe Is JeFf!")
            self.say("YoU cAn’T dEfEaT mE cAuSe YoU aRe NoObs.")
            if player.has_item("Sword of Mirai"):
                player.remove_item("Sword of Mirai")
                self.say("Bob the hero says \'Omae wa mou shindeiru\'")
                self.say("Evil Jeff says \'Nani!?\'")
                self.say("Bob the hero says \'Ora ora ora ora"
                         + " ora ora ora ora ora ora ora\'")
                self.say("Evil Jeff says \'AHHHHHHH   XP\'")
                player.get_damaged(60)
                if player.health > 0:
                    self.times_event_occured += 1
                    self.handle_results("HAPPY ENDING")
                else:
                    self.times_event_occured += 1
                    self.handle_results("GOOD ENDING")
            else:
                player.get_damaged(75)
                self.handle_results("BAD ENDING")
        elif answer == "No":
            self.say("You better searching around first.")
            self.times_event_occured += 1
            self.handle_results("CONTINUE")


class Start(Event):
    """The start event."""

    def enter(self, player):
        """Enter the event."""
        self.say("In a far far away land, Ayaka, a well beloved princess of"
                 + " the human tribe, live happily in her kingdom.")
        self.say("Princess Ayaka is a noble young lady who carries herself"
                 + " with poise and dignity.")
        self.say("She listens attentively. And when she speaks, she"
                 + " carefully chooses her words.")
        self.say("Gentle, generous, compassionate, patient, good-natured"
                 + " and forgiving are all words to describe her.")

        self.say("Unfortunately, Evil Jeff, the dark evil lord of the"
                 + " dark world, has attacked the kingdom.")
        self.say("Evil jeff has kidnapped Princess Ayaka and return"
                 + " to his castle.")
        self.say("The kingdom could not stand the loss of their"
                 + " beloved princess.")
        self.say("YOU, a hero named Bob, offers to save the princess"
                 + " because you are strong and handsome.")

        self.say("After the journey to the west, you finally arrive"
                 + " at Evil Jeff’s castle!")
        self.say("Entered the castle, you venturing off into the unknown...")
        return "CONTINUE"


class End(Event):
    """The good end."""

    def enter(self, player):
        """Enter the event."""
        self.times_event_occured += 1
        self.say("You has defeated Evil Jeff and save Princess Ayaka!")
        self.say("You married Princess Ayaka and live happy ever after…")
        return "VICTORY"


class Death(Event):
    """Death by Jeff."""

    def enter(self, player):
        """Enter the event."""
        self.times_event_occured += 1
        self.say("You got defeated by Evil jeff!")
        self.say("The world is in chaos after your defeat")
        return "GAME OVER"


class Jeff(Game):
    """The Jeff Game."""

    @classmethod
    def game_name(self):
        """Get unique game name used for selection no spaces."""
        return "jeff"

    @classmethod
    def description(self):
        """Get the game description."""
        return "Save the fair princess from the evil Jeff"

    def welcome(self):
        """Get a welcome message."""
        return "Welcome to Jeff!\nThe most fearsome name imaginable!"

    def play(self):
        """Start the game."""
        """Init the game by making the events."""
        self.events = [
            NothingMuch(self),
            LootboxKey(self),
            SwordofMirai(self),
            MonsterRoom1(self),
            MonsterRoom2(self),
            MonsterRoom3(self),
            Healing(self),
            HealthPotion(self),
            UseHealthPotion(self),
            MiniBoss(self),
            EvilJeff(self)
        ]

        self.start = Start(self)
        self.end = End(self)

        self.death = Death(self)

        player = Player()
        self.player = player

        start = self.start
        # end = self.end

        start.enter(player)
        self.ask_choice()

    def ask_choice(self):
        """Ask the critical choice."""
        self.choice("You are confronted with a choice of paths",
                    ["Left", "Forward", "Right"], self.the_choice)

    def the_choice(self, choice):
        """Repeating post choice."""
        death = self.death
        events = self.events
        player = self.player

        paths = list(range(0, len(events)))
        random.shuffle(paths)
        three_path = paths[0:3]
        if choice == "Left":
            idx = three_path[0]
        elif choice == "Forward":
            idx = three_path[1]
        elif choice == "Right":
            idx = three_path[2]

        my_path = events[idx]
        event_result = my_path.enter(player)
        if player.health <= 0:
            event_result = death.enter(player)
        self.handle_results(event_result)

    def handle_results(self, event_result):
        """Handel the handle results."""
        if event_result == "BAD ENDING":
            self.say("""
            =================
            You got defeated by Evil Jeff!
            No one could defeat Evil Jeff!
            The world is in chaos!

            GAME OVER

            =================
            """)
            return
        elif event_result == "HAPPY ENDING":
            self.say("""
            ================
            Congratulations!
            You have defeated Evil Jeff!
            You married the princess and lived happily ever after
            Fin...
            ================
            """)
            return
        elif event_result == "GOOD ENDING":
            self.say("""
            ================
            Congratulations!
            You have defeated Evil Jeff but with the cost of your life!
            The kingdom will not forget your sacrifice!
            Fin...
            ================
            """)
            return
        elif event_result == "GAME OVER":
            self.say("""
            ================

            You died...

            GAME OVER

            ================
            """)
            return
        self.ask_choice()

    def stats(self):
        """Print some stats."""
        for event in self.events:
            event_type = type(event)
            event_name = event_type.__name__
            self.say(f"You run into {event_name},"
                     + f" {event.times_event_occured} time(s)")
