"""
The Trashy RPG Game.

Authours:  Pimsucha Kanjchanapoomi
"""

import yaml
import random
import time

def rng_bless(num):
        rng = random.randint(0,num)
        return rng
class Player():
    def __init__(self):
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
        self.name = namey
    @property
    def max_hp(self):
        return self.vit*5
    @property
    def base_atk(self):
        return self.str*3
    @property
    def dodge_rate(self):
        d= self.agi
        if d > 90:
            d= 90
        return d
    @property
    def max_exp(self):
        return self.lv*5
    def damage(self, amount):
        print(f"From your Hp {self.health} you lost {amount}...\nYou have {max([self.health-amount,0])} Hp left")
        self.health = self.health - amount
        if self.health <0:
            self.health = 0
    def healed(self, amount):
        self.health += amount
        if self.health > self.max_hp:
            self.health = int(self.max_hp)
    def exp_gain(self,amount):
        self.exp += amount
        if self.exp > self.max_exp:
            self.exp = self.exp - self.max_exp
            self.lv += 1
            self.str +=1
            self.vit +=1
            self.agi +=1
    def add_str(self):
        if self.ducat >= self.str:
            self.ducat -= self.str
            self.str+=1
            print("successfully add strength")
    def add_agi(self):
        if self.ducat >= self.agi:
            self.ducat -= self.agi
            self.agi+=1
            print("successfully add agility")
    def add_vit(self):
        if self.ducat >= self.vit:
            self.ducat -= self.vit
            self.vit+=1
            print("successfully add vitality")
    def add_lck(self):
        if self.ducat >= 2*self.lck:
            self.ducat -= self.lck
            self.lck+=1
            print("successfully add luck")
    def money_gained(self, amount):
        self.ducat += amount

class Monster():
    def __init__(self, stage):
        self.name = 'random mob A on the way'
        self.lv = stage + (1 - rng_bless(2))

        self.str = 3+stage+(1-rng_bless(2))
        self.vit = 3+stage+(1-rng_bless(2))
        self.agi = 3+stage+(1-rng_bless(2))
        self.health = self.max_hp
        self.lck = 3+stage+(1-rng_bless(2))
    @property
    def max_hp(self):
        return self.vit*4
    @property
    def base_atk(self):
        return self.str*2
    @property
    def dodge_rate(self):
        d= int(self.agi/2)
        if d > 90:
            d= 90
        return d
    def damage(self, amount):
        self.health = self.health - amount
        if self.health <0:
            self.health = 0
class Boss():
    def __init__(self, stage):
        self.name = 'Just a Boss'

        self.lv = stage

        self.str = 5+self.lv+(1-rng_bless(2))


        self.vit = 5+self.lv+(1-rng_bless(2))
        self.agi = 5+self.lv+(1-rng_bless(2))
        self.lck = 5+self.lv+(1-rng_bless(2))
        self.health = self.max_hp
    @property
    def max_hp(self):
        return self.vit*6
    @property
    def base_atk(self):
        return self.str*4
    @property
    def dodge_rate(self):
        d= self.agi*2
        if d > 90:
            d= 90
        return d
    def damage(self, amount):
        self.health = self.health - amount
        if self.health <0:
            self.health = 0
class Event():
    def __init__(self):
        self.stages = 0

    def dialog(self, message):
        time.sleep(0)
        print(message)



    def enter(self, player):
            raise NotImplemented


class Battle(Event):

    def enter(self, player, opponent):
        n = "name"
        b_options = ["Fight","Give Up", "See Stat"]
        while True:
            self.dialog(f"You have encounter {opponent.name}, what will you do?")
            for idx, b_option in enumerate(b_options):
                self.dialog(f"{idx+1} : {b_option} ")
            choice = input()
            for idx, b_option in enumerate(b_options):
                if choice == str(idx+1) or choice.lower() == b_option.lower():
                    if b_option == 'See Stat':
                        See_Stat().enter(player)
                    else:
                        return b_option

class Inn(Event):
    def enter(self, player):
        i_options = [
            "Add Strength",
            "Add Agility",
            "Add Vitality",
            "Add Luck"
            ]
        while True:
            self.dialog("You found an inn and decided to stay for a night")
            self.dialog("You can choose to increase your stats  once by spending twice the amount of current stats")
            self.dialog("If you don't have enough ducat, the choice is invalid and nothing happen")
            for idx, i_option in enumerate(i_options):
                self.dialog(f"{idx+1} : {i_option} ")
            choice = input()
            for idx, i_option in enumerate(i_options):
                if choice == str(idx+1) or choice.lower() == i_option.lower():
                    return i_option

class Nothing(Event):

    def enter(self, player):
        self.dialog("Nothing happen, you have a good lonely camping.")
        player.stage += 1
        return "End Stage"


class Add_status(Event):
    def enter(self, player, option):
        if option == "Add Strength":
            player.add_str()
        elif option == "Add Agility":
            player.add_agi()
        elif option == "Add Vitality":
            player.add_vit()
        elif option == "Add Luck":
            player.add_lck()
        else:
            print("this is a bug")
        player.healed(float("inf"))
        player.stage += 1
        return "End Stage"



class Fight(Event):

    def enter(self, player, opponent):
        money_earn = int(opponent.lv * (1+rng_bless(player.lck)/100))
        exp_earn = int(money_earn/2)
        while True:
            self.dialog("You choose to attack the monster")
            roll = rng_bless(99)
            multiplier_p = 1
            multiplier_o = 1
            if player.dodge_rate >= roll:
                multiplier_p = 0

            if opponent.dodge_rate >= roll:
                multiplier_o = 0
            damage_by_player = int(player.base_atk*(1+rng_bless(10)/10)*multiplier_p)
            damage_by_mons = int(opponent.base_atk * (1*rng_bless(10)/10)*multiplier_o)

            self.dialog(f"You attack the monster by {damage_by_player}, but get counter by {damage_by_mons}")
            opponent.damage(damage_by_player)

            player.damage(damage_by_mons)
            if player.health == 0 or opponent.health == 0:
                player.stage += 1

                if player.health > 0:
                    player.exp_gain(exp_earn)
                    player.money_gained(money_earn)
                return "End Stage"

class Give_Up(Event):

    def enter(self, player):
        self.dialog("When you decided to give up, even God cannot save you")
        self.dialog("Your opponent decided to not to kill you")
        self.dialog("Alas you still died from your own cowardice.")
        player.health = 0
        return "End Stage"

class See_Stat(Event):

    def enter(self, player):
        the_stat ={
            "Name" : player.name,
            "Lv." : player.lv,
            "Health" : f"{player.health}/{player.max_hp}",
            "str" : player.str,
            "vit" : player.vit,
            "agi" : player.agi,
            "lck" : player.lck,
            "ducat" : player.ducat,
            "exp" : player.exp


        }
        print(yaml.dump(the_stat))

class Start(Event):

    def enter(self, player):
        player.stage += 1
        self.dialog("Just another trashy RPG game")
        self.dialog("Don't expect much, mkay?")
        return "End Stage"

class Died(Event):

    def enter(self, player):
        self.dialog("What a shame, you are dead")
        self.dialog(f"You have reach {player.stage} stage, congrat?!!")
        return "GAME OVER"
class Game(Event):

    def __init__(self):
        self.battle_choices = [
            Fight(),
            Give_Up(),
        ]
        self.stage_setting = [
            Inn(),
            Battle(),
            Nothing()

        ]


        self.start = Start()
        self.died = Died()

    def play(self):
        import yaml
        from pathlib import Path
        load_from = Path("savedata.yml")
        int_data = {
            "name" : 'gimme a name',
            "lv" : 1,
            "health" : 25,
            "str" : 5,
            "vit" : 5,
            "agi" : 5,
            "lck" : 5,
            "ducat" : 0,
            "exp" : 0
        }
        if load_from.exists():
            player_data = load_from.read_text()
            data=yaml.safe_load(player_data)
        else:
            data = int_data
        player = Player()
        list_of_stat = ("name","lv","str","vit","agi","lck","ducat","exp")
        for i in list_of_stat:
            setattr(player,i,data[i]) #set the player stat
        battle_choices = self.battle_choices
        start = self.start
        died = self.died
        event_result = start.enter(player)
        stage = player.stage
        player.healed(float("inf"))
        if player.name == 'gimme a name':
            new_name = input("Please enter a new name")
            player.set_name(new_name)
        while event_result == "End Stage":
            path = rng_bless(9)
            stage_number = player.stage
            if path == 9:
                inn_choice = Inn().enter(player) #inn
                battle_choice = "nothing"
                Add_status().enter(player, inn_choice)
            elif path >= 1:
                opponent = Monster(stage_number)
                battle_choice = Battle().enter(player, opponent)#mons=stage
            elif path == 0:
                if player.stage % 5 ==0:
                    opponent = Boss(stage_number)
                    battle_choice = Battle().enter(player, opponent)#boss_fight
                else:
                    Nothing().enter(player)
                    battle_choice = "nothing"
            if battle_choice == 'Fight':
                Fight().enter(player, opponent)
            elif battle_choice == 'Give Up':
                Give_Up().enter(player)
            if player.health <= 0:
                event_result = Died().enter(player)
            else:
                self.dialog(f"Your pointless endless journey continue")
                print(f"The current stage is {player.stage}")

            if event_result == "GAME OVER":
                self.dialog("Saving in progress...")
                self.dialog("Have a better luck next time")
                self.dialog("Hail Great RNG God!!!")
                """
                Add saving mechanism here
                """
                save_data = {
                    "name" : player.name,
                    "lv" : player.lv,
                    "str" : player.str,
                    "vit" : player.vit,
                    "agi" : player.agi,
                    "lck" : player.lck,
                    "ducat" : player.ducat,
                    "exp" : player.exp
                    }
                import yaml
                text_data = yaml.dump(save_data)
                from pathlib import Path
                save_to = Path("savedata.yml")
                save_to.write_text(text_data)


game = Game()
