"""
The Trashy RPG Game.

Authours:  Pimsucha Kanjchanapoomi
"""

import yaml
import random

from game import Game


def rng_bless(num):
    """Get the blessed number from the RNG gods."""
    rng = random.randint(0, num)
    return rng


class Player():
    """The player data."""

    def __init__(self, bot):
        """Init the player."""
        self.bot = bot
        self.name = 'gimme a name'
        self.lv = 1
        self.health = 25
        self.str = 5
        self.vit = 5
        self.agi = 5
        self.lck = 5
        self.ducat = 0
        self.exp = 0
        self.stage = 0

    def set_name(self, namey):
        """Set his name."""
        self.name = namey

    @property
    def max_hp(self):
        """Get max hp."""
        return self.vit*5

    @property
    def base_atk(self):
        """Get base atk."""
        return self.str*3

    @property
    def dodge_rate(self):
        """Get dodge rate."""
        d = self.agi
        if d > 90:
            d = 90
        return d

    @property
    def max_exp(self):
        """Get max exp."""
        return self.lv*5

    def damage(self, amount):
        """Damage the player."""
        self.bot.say(f"From your Hp {self.health} you lost {amount}...\n"
                     + f"You have {max([self.health-amount,0])} Hp left")
        self.health = self.health - amount
        if self.health < 0:
            self.health = 0

    def healed(self, amount):
        """Heal the player."""
        self.health += amount
        if self.health > self.max_hp:
            self.health = int(self.max_hp)

    def exp_gain(self, amount):
        """Gain exp."""
        self.exp += amount
        if self.exp > self.max_exp:
            self.exp = self.exp - self.max_exp
            self.lv += 1
            self.str += 1
            self.vit += 1
            self.agi += 1

    def add_str(self):
        """Gain str."""
        if self.ducat >= self.str:
            self.ducat -= self.str
            self.str += 1
            self.bot.say("successfully add strength")

    def add_agi(self):
        """Gain agility."""
        if self.ducat >= self.agi:
            self.ducat -= self.agi
            self.agi += 1
            self.bot.say("successfully add agility")

    def add_vit(self):
        """Gain vitality."""
        if self.ducat >= self.vit:
            self.ducat -= self.vit
            self.vit += 1
            self.bot.say("successfully add vitality")

    def add_lck(self):
        """Gain luck."""
        if self.ducat >= 2*self.lck:
            self.ducat -= self.lck
            self.lck += 1
            self.bot.say("successfully add luck")

    def money_gained(self, amount):
        """Gain money."""
        self.ducat += amount


class Monster():
    """A monster, aka exp farms."""

    def __init__(self, stage):
        """Make that mob."""
        self.name = 'random mob A on the way'
        self.lv = stage + (1 - rng_bless(2))

        self.str = 3+stage+(1-rng_bless(2))
        self.vit = 3+stage+(1-rng_bless(2))
        self.agi = 3+stage+(1-rng_bless(2))
        self.health = self.max_hp
        self.lck = 3+stage+(1-rng_bless(2))

    @property
    def max_hp(self):
        """Get max HP."""
        return self.vit*4

    @property
    def base_atk(self):
        """Get base attack."""
        return self.str*2

    @property
    def dodge_rate(self):
        """Get dodge rate."""
        d = int(self.agi/2)
        if d > 90:
            d = 90
        return d

    def damage(self, amount):
        """Damage the mob."""
        self.health = self.health - amount
        if self.health < 0:
            self.health = 0


class Boss():
    """A BOSS, aka an overpowered exp farm."""

    def __init__(self, stage):
        """Make this bigger mob."""
        self.name = 'Just a Boss'

        self.lv = stage

        self.str = 5+self.lv+(1-rng_bless(2))

        self.vit = 5+self.lv+(1-rng_bless(2))
        self.agi = 5+self.lv+(1-rng_bless(2))
        self.lck = 5+self.lv+(1-rng_bless(2))
        self.health = self.max_hp

    @property
    def max_hp(self):
        """Get max HP."""
        return self.vit*6

    @property
    def base_atk(self):
        """Get base attack."""
        return self.str*4

    @property
    def dodge_rate(self):
        """Get dodge rate."""
        d = self.agi*2
        if d > 90:
            d = 90
        return d

    def damage(self, amount):
        """Give the boss what for."""
        self.health = self.health - amount
        if self.health < 0:
            self.health = 0


class Event():
    """The place where anything happens."""

    def __init__(self, bot):
        """Make the event."""
        self.stages = 0
        self.bot = bot

    def say(self, message):
        """Talk to the player."""
        self.bot.say(message)

    def choice(self, message, options, callbacks):
        """Pass choices onto bot."""
        self.bot.choice(message, options, callbacks)

    def enter(self, player):
        """Do something."""
        raise NotImplementedError


class Battle(Event):
    """Fight that exp farm."""

    def enter(self, player, opponent):
        """Start the event."""
        b_options = ["Fight", "Give_Up", "See_Stat"]
        self.say(f"You have encounter {opponent.name}")
        for idx, b_option in enumerate(b_options):
            self.say(f"{idx+1} : {b_option} ")
        self.choice("What will you do?", b_options, self.bot.post_battle)


class Inn(Event):
    """Time to rest."""

    def enter(self, player):
        """Start the event."""
        i_options = [
            "Add_Strength",
            "Add_Agility",
            "Add_Vitality",
            "Add_Luck"
            ]
        self.say("You found an inn and decided to stay for a night")
        self.say("You can choose to increase your stats  once by"
                 + " spending twice the amount of current stats")
        self.say("If you don't have enough ducat, the choice is"
                 + " invalid and nothing happen")
        for idx, i_option in enumerate(i_options):
            self.say(f"{idx+1} : {i_option} ")
        self.choice("What will you improve?", i_options, self.bot.post_inn)


class Nothing(Event):
    """Noda."""

    def enter(self, player):
        """Start the event."""
        self.say("Nothing happen, you have a good lonely camping.")
        player.stage += 1
        return "End Stage"


class Add_status(Event):
    """Get some stats."""

    def enter(self, player, option):
        """Start the event."""
        if option == "Add_Strength":
            player.add_str()
        elif option == "Add_Agility":
            player.add_agi()
        elif option == "Add_Vitality":
            player.add_vit()
        elif option == "Add_Luck":
            player.add_lck()
        else:
            self.bot.say("this is a bug")
        player.healed(float("inf"))
        player.stage += 1
        return "End Stage"


class Fight(Event):
    """More exp farm logic."""

    def enter(self, player, opponent):
        """Start the event."""
        money_earn = int(opponent.lv * (1+rng_bless(player.lck)/100))
        exp_earn = int(money_earn/2)
        while True:
            self.say("You choose to attack the monster")
            roll = rng_bless(99)
            multiplier_p = 1
            multiplier_o = 1
            if player.dodge_rate >= roll:
                multiplier_p = 0

            if opponent.dodge_rate >= roll:
                multiplier_o = 0
            damage_by_player = int(player.base_atk
                                   * (1 + rng_bless(10)/10) * multiplier_p)
            damage_by_mons = int(opponent.base_atk
                                 * (1 * rng_bless(10)/10) * multiplier_o)

            self.say(f"You attack the monster by {damage_by_player},"
                     + f"but get counter by {damage_by_mons}")
            opponent.damage(damage_by_player)

            player.damage(damage_by_mons)
            if player.health == 0 or opponent.health == 0:
                player.stage += 1

                if player.health > 0:
                    player.exp_gain(exp_earn)
                    player.money_gained(money_earn)
                return "End Stage"


class Give_Up(Event):
    """This is just too much."""

    def enter(self, player):
        """Start the event."""
        self.say("When you decided to give up, even God cannot save you")
        self.say("Your opponent decided to not to kill you")
        self.say("Alas you still died from your own cowardice.")
        player.health = 0
        return "End Stage"


class See_Stat(Event):
    """Show me those stats."""

    def enter(self, player):
        """Start the event."""
        the_stat = {
            "Name": player.name,
            "Lv.": player.lv,
            "Health": f"{player.health}/{player.max_hp}",
            "str": player.str,
            "vit": player.vit,
            "agi": player.agi,
            "lck": player.lck,
            "ducat": player.ducat,
            "exp": player.exp
        }
        self.bot.say(yaml.dump(the_stat))


class Start(Event):
    """The intro."""

    def enter(self, player):
        """Start the event."""
        player.stage += 1
        self.say("Just another trashy RPG game")
        self.say("Don't expect much, mkay?")
        return "End Stage"


class Died(Event):
    """The inevitable result."""

    def enter(self, player):
        """Start the event."""
        self.say("What a shame, you are dead")
        self.say(f"You have reach {player.stage} stage, congrat?!!")
        return "GAME OVER"


class Rng(Game):
    """The actual game loop."""

    @classmethod
    def game_name(self):
        """Get unique game name used for selection no spaces."""
        return "rng"

    @classmethod
    def description(self):
        """Get the game description."""
        return "A self proclaimed trashy rng."

    def welcome(self):
        """Get a welcome message."""
        return "RNG\nYou must love pointlessly trawling through games."

    def __init__(self, bot, chat_id):
        """Init the game."""
        super().__init__(bot, chat_id)

        self.battle_choices = [
            Fight(self),
            Give_Up(self),
        ]
        self.stage_setting = [
            Inn(self),
            Battle(self),
            Nothing(self)

        ]

        self.start = Start(self)
        self.died = Died(self)

        data = {
            "name": 'gimme a name',
            "lv": 1,
            "health": 25,
            "str": 5,
            "vit": 5,
            "agi": 5,
            "lck": 5,
            "ducat": 0,
            "exp": 0
        }
        list_of_stat = ("name", "lv", "str", "vit", "agi", "lck", "ducat",
                        "exp")
        self.player = Player(self)
        for i in list_of_stat:
            setattr(self.player, i, data[i])  # set the player stat

    def play(self):
        """Time to play."""
        start = self.start
        player = self.player
        event_result = start.enter(player)
        self.event_result = event_result
        player.healed(float("inf"))
        if player.name == 'gimme a name':
            self.open_answer("Please enter a new name", self.stage2)
        else:
            self.event_loop()

    def stage2(self, new_name):
        """Stage 2 we set the name."""
        self.player.set_name(new_name)
        self.event_loop()

    def event_loop(self):
        """Start the loop."""
        player = self.player
        if self.event_result == "End Stage":
            path = rng_bless(9)
            stage_number = player.stage
            if path == 9:
                Inn(self).enter(player)  # inn
            elif path >= 1:
                self.opponent = Monster(stage_number)
                Battle(self).enter(player, self.opponent)  # mons=stage
            elif path == 0:
                if player.stage % 5 == 0:
                    self.opponent = Boss(stage_number)
                    # boss_fight
                    Battle(self).enter(player, self.opponent)
                else:
                    Nothing(self).enter(player)
                    self.battle_choice = "nothing"
                    self.post_events()

    def post_inn(self, inn_choice):
        """Post inn event."""
        self.battle_choice = "nothing"
        Add_status(self).enter(self.player, inn_choice)
        self.post_events()

    def post_battle(self, battle_choice):
        """Start the actual battle."""
        if battle_choice == 'Fight':
            Fight(self).enter(self.player, self.opponent)
        elif battle_choice == 'Give_Up':
            Give_Up(self).enter(self.player)
        elif battle_choice == "See_Stat":
            See_Stat(self).enter(self.player)
            Battle(self).enter(self.player, self.opponent)
            return
        self.post_events()

    def post_events(self):
        """Post event happening."""
        event_result = self.event_result
        if self.player.health <= 0:
            event_result = Died(self).enter(self.player)
        else:
            self.say(f"Your pointless endless journey continue")
            self.say(f"The current stage is {self.player.stage}")

        if event_result == "GAME OVER":
            self.say("Your progress will be kept for next play"
                     + " through... Just use /play again (Stats lost if you"
                     + " pick another game from the main menu.)")
            self.say("Have a better luck next time")
            self.say("Hail Great RNG God!!!")
        self.event_result = event_result
        self.event_loop()
