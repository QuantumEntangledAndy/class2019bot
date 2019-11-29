"""
Abyss Game.

Adapted to play on telegram by Andrew W King
"""

__author__ = "Kevin Yuen,  Yosita Phailomwong,  Kornkanok  Paramesirikuntorn"
__copyright__ = "Copyright 2019, Chulalongkorn University"
__credits__ = ["Kevin Yuen",  "Yosita Phailomwong",
               "Kornkanok  Paramesirikuntorn"]
__license__ = "AGPL"
__version__ = "1.0.0"
__maintainer__ = "Dr Andrew King"
__email__ = "sheepchaan@gmail.com"
__status__ = "Production"

from game import Game


class Player():
    """Player class."""

    def __init__(self):
        """Init the player."""
        self.inventory = {}

    def has_item(self, item):
        """Get if item is present."""
        item_count = self.inventory.get(item, 0)
        if item_count > 0:
            return True
        else:
            return False

    def add_item(self, item):
        """Add an item."""
        item_count = self.inventory.get(item, 0)
        self.inventory[item] = item_count + 1

    def remove_item(self, item):
        """Remove an item."""
        if self.has_item(item):
            item_count = self.inventory.get(item, 0)
            self.inventory[item] = item_count - 1


class Abyss(Game):
    """The quester game."""

    @classmethod
    def game_name(self):
        """Get unique game name used for selection."""
        return "abyss"

    @classmethod
    def description(self):
        """Get the game description."""
        return "Rescue the fair pricess from the king of darkness."

    def welcome(self):
        """Get a welcome message."""
        return ("Abyss\nBe your ladies white knight\n"
                + "Created by " + __author__)

    def play(self):
        """Start playing."""
        self.player = Player()

        # Legends
        self.yes_no = ["yes", "no"]
        self.directions = ["left", "right", "forward", "backward"]

        # Introduction to the game
        self.open_answer("Name yourself, challenger?", self.stage2)

    def stage2(self, name):
        """Stage 2."""
        self.name = name
        self.say("Greetings, " + self.name + ". Lucifer knows you are here and"
                 + "he is ready for you. If you can beat him, you can take "
                 + " back your beloved princess. Show me what you got!"
                 + " Goodluck challenger, you will need it. ")
        self.say("The gates of the castle creaks open and clouds of smoke "
                 + "rose up before your eyes.")
        self.say("""
                                  {} {}
                            !  !  II II  !  !
                         !  I__I__II II__I__I  !
                         I_/|--|--|| ||--|--|\\_I
        .-'"'-.       ! /|_/|  |  || ||  |  |\\_|\\ !       .-'"'-.
       /===    \\      I//|  |  |  || ||  |  |  |\\I      /===    \\
       \\==     /   ! /|/ |  |  |  || ||  |  |  | \\|\\ !   \\==     /
        \\__  _/    I//|  |  |  |  || ||  |  |  |  |\\I    \\__  _/
         _} {_  ! /|/ |  |  |  |  || ||  |  |  |  | \\|\\ !  _} {_
        {_____} I//|  |  |  |  |  || ||  |  |  |  |  |\\I {_____}
   !  !  |=  |=/|/ |  |  |  |  |  || ||  |  |  |  |  | \\|\\=|-  |  !  !
  _I__I__|=  ||/|  |  |  |  |  |  || ||  |  |  |  |  |  |\\||   |__I__I_
  -|--|--|-  || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||=  |--|--|-
  _|__|__|   ||_|__|__|__|__|__|__|| ||__|__|__|__|__|__|_||-  |__|__|_
  -|--|--|   ||-|--|--|--|--|--|--|| ||--|--|--|--|--|--|-||   |--|--|-
   |  |  |=  || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||   |  |  |
   |  |  |   || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||=  |  |  |
   |  |  |-  || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||   |  |  |
   |  |  |   || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||=  |  |  |
   |  |  |=  || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||   |  |  |
   |  |  |   || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||   |  |  |
   |  |  |   || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||-  |  |  |
  _|__|__|   || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||=  |__|__|_
  -|--|--|=  || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||   |--|--|-
  _|__|__|   ||_|__|__|__|__|__|__|| ||__|__|__|__|__|__|_||-  |__|__|_
  -|--|--|=  ||-|--|--|--|--|--|--|| ||--|--|--|--|--|--|-||=  |--|--|-
  jgs |  |-  || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||-  |  |  |
 ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~
""")
        self.say("Before you know it, you find yourself on the edge"
                 + " of a dark forest and all you can hear is small"
                 + " sounds of rustling bushes and the howl of the wind.")
        self.say("Will you still continue on this journey, challenger?")
        # Start of the game
        self.choice("Would you like to step into the deep dark forest?",
                    ['yes', 'no'], self.stage3)

    def stage3(self, response):
        """Start stage 3."""
        if response == "yes":
            self.say("You start your jouney into the dark, eerey forest."
                     + " You can hear voices of the night whispering to"
                     + " each other.\n")
            self.say("""
                                          .
                                              .         ;
                 .              .              ;%     ;;
                   ,           ,                :;%  %;
                    :         ;                   :;%;'     .,
           ,.        %;     %;            ;        %;'    ,;
             ;       ;%;  %%;        ,     %;    ;%;    ,%'
              %;       %;%;      ,  ;       %;  ;%;   ,%;'
               ;%;      %;        ;%;        % ;%;  ,%;'
                `%;.     ;%;     %;'         `;%%;.%;'
                 `:;%.    ;%%. %@;        %; ;@%;%'
                    `:%;.  :;bd%;          %;@%;'
                      `@%:.  :;%.         ;@@%;'
                        `@%.  `;@%.      ;@@%;
                          `@%%. `@%%    ;@@%;
                            ;@%. :@%%  %@@%;
                              %@bd%%%bd%%:;
                                #@%%%%%:;;
                                %@@%%%::;
                                %@@@%(o);  . '
                                %@@@o%;:(.,'
                            `.. %@@@o%::;
                               `)@@@o%::;
                                %@@(o)::;
                               .%@@@@%::;
                               ;%@@@@%::;.
                              ;%@@@@%%:;;;.
                          ...;%@@@@@%%:;;;;,..
""")
        elif response == "no":
            self.say("You are not ready to save your beloved princess."
                     + " Goodbye, " + self.name + ".")
            self.say("GAMER OVER, YOU FAILED IN YOUR QUEST")
            self.say("""
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                     ░
""")
            return

        # first part of the game
        self.say("You decided to walk through the dark forest not with your"
                 + " eyes but with your heart and your ears")
        self.say("You keep walking and you see flickering lights in"
                 + " distance as you keep moving")
        self.say("As you move closer and closer; you find yourself"
                 + " at a crossroad.")
        self.say("To your left, a dark path leads you right to Lucifer"
                 + " and you will have a chance to contend with him right"
                 + " away.")
        self.say("To your right, you continue through the forest to gather"
                 + " more information and armory.")
        self.say("In front of you is massive stone wall that separates the"
                 + " forest from the unknown path.")
        self.say("Behind you is the exit of the Castle of Death.\n")
        self.choice("What direction do you move?", self.directions,
                    self.stage4)

    def stage4(self, response):
        """Play stage 4."""
        if response == "left":
            self.say("You walk right into Lucifer's cage and he releases"
                     + " his hounds of death and they shred you to pieces and"
                     + " your journey ends here. Farewell, " + self.name + ".")
            self.say("GAMER OVER, YOU FAILED IN YOUR QUEST")
            self.say("""
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                     ░
""")
            return
        elif response == "right":
            self.say("You head deeper into the forest and you find a"
                     + " cave that you can use as a refuge for tonight.\n")
        elif response == "forward":
            self.say("You cannot scale the wall because you don't have the"
                     + " tools yet; come back when you are ready.\n")
            self.choice("What direction do you move?", self.directions,
                        self.stage4)
            return
        elif response == "backward":
            self.say("You have surrendered and abandoned your beloved"
                     + " princess. Goodbye, " + self.name + ".")
            self.say("GAMER OVER, YOU FAILED IN YOUR QUEST")
            self.say("""
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                     ░
""")
            return

        # second part of the game
        self.say("Once entered the cave, you are greeted by a friendly"
                 + "gollum. But in the back of the cave you see a great sword")
        self.say("""
            .';:;'.
            /_' _' /\\   __
            ;a/ e= J/-'"  '.
            \\ ~_   (  -'  ( ;_ ,.
             L~"'_.    -.  \\ ./  )
             ,'-' '-._  _;  )'   (
           .' .'   _.'")  \\  \\(  |
          /  (  .-'   __\\{`', \\  |
         / .'  /  _.-'   "  ; /  |
        / /    '-._'-,     / / \\ (
     __/ (_    ,;' .-'    / /  /_'-._
    `"-'` ~`  ccc.'   __.','     \\j\\L\
                     .='/|\7
                        ' `
    """)
        self.say('The gollum speaks in a high-pitched, "Hello stranger, what"'
                 + ' are you doing here? the last time I had a visitor was 5'
                 + ' years ago. Sadly, he died in this caved with me."')
        self.say('"So what are you looking for in this cave?"')
        response = ""
        answer1 = ["I_want_the_sword_in_the_back_of_the_cave",
                   "I_was_looking_for_a_weapon"]
        self.choice("You answer...", answer1, self.stage5)

    def stage5(self, response):
        """Play stage 5."""
        if response == "I_want_the_sword_in_the_back_of_the_cave":
            self.say("Oh, that old thing. Well if you want it, you have to"
                     + "listen to my story.\n")
        elif response == "I_was_looking_for_a_weapon":
            self.say("Wow, what a coincidence. I happen to have a sword lying"
                     + " around here. But if you want it, you have to listen"
                     + " to my story.\n")
        else:
            self.say("You spoke gibberish, please try again.\n")

        # gollum's story
        response = ""
        answer2 = ["listen", "steal_the_sword"]
        self.choice("Would you like to...", answer2, self.stage6)

    def stage6(self, response):
        """Play stage 6."""
        if response == "listen":
            self.say('The gollum exclaimed "HAHAAHA, great choice.'
                     + " I was just testing your character."
                     + ' You can have the sword."')
            self.player.add_item("Great Sword")
            self.say("""
                   />_________________________________
[########[]_________________________________>
         \\>
""")
        elif response == "steal_the_sword":
            self.say("You try the steal the sword from the gollum but he was"
                     + " faster and stronger than you thought. He attacks"
                     + " you but you escaped empty handed.")

        # Monster camp
        self.say("You leave the cave but on the way back to the crossroad,"
                 + " you see a monster camp full of goblin, trolls, and ogres."
                 + " And in the middle of the camp, you see a ladder.")
        self.say("Hint: You can use the ladder to climb the wall.")
        answer3 = ["fight_the_monsters", "run_away"]
        self.choice("You choose to...", answer3, self.stage7)

    def stage7(self, response):
        """Play stage 7."""
        if response == "fight_the_monsters":
            if self.player.has_item("Great Sword"):
                self.say('It was a hard fought battle but in the end,'
                         + ' all the monsters were killed and you acquired'
                         + ' the ladder."\n')
                self.player.add_item("Ladder")
                self.say("""
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
""")
            else:
                self.say('"You try to fight with your bare'
                         + ' hands and got smashed."\n')
                self.say("GAMER OVER, YOU FAILED IN YOUR QUEST")
                self.say("""
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                     ░
""")
                return
        elif response == "run_away":
            self.say("As you run away, you stepped on a bear trap"
                     + " that the monsters set up to find food."
                     + " You bleed out and parished.")
            self.say("GAMER OVER, YOU FAILED IN YOUR QUEST")
            self.say("""
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                     ░
""")
            return

        # Crossroad
        self.say("As you arrive back at the crossroad, ready and armed,"
                 + "its time to save your beloved princess")
        response = ""
        directions2 = ["left", "forward", "backwards"]
        self.say("To your left, a dark path leads you right to Lucifer"
                 + " and you will have a chance to contend with him"
                 + " right away.")
        self.say("In front of you is massive stone wall that separates the"
                 + " forest from the unknown path.")
        self.say("Behind you is the exit of the Castle of Death.\n")
        self.choice("What direction do you move?", directions2, self.stage8)

    def stage8(self, response):
        """Play stage 8."""
        if response == "left":
            self.say("You walk right into Lucifer's cage and he releases his"
                     + " hounds of death and they shred you to pieces and your"
                     + " journey ends here. Farewell, " + self.name + ".")
            self.say("GAMER OVER, YOU FAILED IN YOUR QUEST")
            self.say("""
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                     ░
""")
            return
        elif response == "forward":
            self.say("You used the ladder to scale the wall and arrive"
                     + " at Lucifer's throne room. \n")
            self.say('Lucifer is sitting on this throne and he laughs'
                     + ' hysterically and says, "you are finally here,'
                     + ' I have been expecting you."')
            self.say("You see your beloved princess in a cage next to"
                     + " his throne, her fate and your fate is literally"
                     + " in your own hands; proceed wisely.")
        elif response == "backward":
            self.say("You have surrendered and abandoned your"
                     + " beloved princess. Goodbye, " + self.name + ".")
            self.say("GAMER OVER, YOU FAILED IN YOUR QUEST")
            self.say("""
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                     ░
""")
            return

        # the final fight
        response = ""
        answer4 = ["Charge_into_Lucifer", "Deceive_him"]
        self.say("You advance towards Lucifer's throne slowly; Lucifer gets"
                 + " up from his throne and uses his telekinetic ability"
                 + " and slams your against the wall")
        self.choice("You choose to...", answer4, self.stage9)

    def stage9(self, response):
        """Play stage 9."""
        if response == "Charge_into_Lucifer":
            self.say("Lucifer lifts you up by your neck and squeezes it"
                     + " hard, your eyes become blurry, and then everything"
                     + " turns to black as he snaps your neck.")
            self.say("GAMER OVER, YOU FAILED IN YOUR QUEST")
            self.say("""
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                     ░
""")
            return
        elif response == "Deceive_him":
            self.say("You make him think that you're dead and when he"
                     + " comes to check on you; you strike him when he"
                     + " leasts expects it.")
            self.say("You make sure Lucifer is looking the other way,"
                     + " you get up quickly, wield out the great sword,"
                     + " and stab it at Lucifer's heart.")
            self.say("The strike stunted him and he drops to the ground"
                     + " and blood gushes out from his chest.")
            self.say("Lucifer is laying down and begging for his life.")
            self.say("""
            .-/`)
         // / / )
      .=// / / / )
     //`/ / / / /
    // /     ` /
   ||         /
    \\       /
     ))    .'
    //    /
         /
""")

        # the great choice
        response = ""
        answer5 = ["Spare_his_life", "Finish_him_off"]
        self.say("Oh please spare me great challenger! if you let me live,"
                 + " I will bestow you all the things you desire.")
        self.choice("You choose to...", answer5, self.stage10)

    def stage10(self, response):
        """Play stage 10."""
        if response == "Spare_his_life":
            self.say("Thank you, great challenger!; you can have your"
                     + " beloved princess back")
            self.say("As you leave the Castle of Death with your"
                     + " beloved princess; Lucifer gets up and"
                     + " brings down a rain of fire on both of you."
                     + " Both you and your beloved princess die.")
            self.say("GAMER OVER, YOU FAILED IN YOUR QUEST")
            self.say("""
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                     ░
""")
            return
        elif response == "Finish_him_off":
            self.say("You have no mercy for a man like Lucifer."
                     + " You swung your sword as hard as you can at"
                     + " Lucifer's neck and it comes right off.")
            self.say("After cleaning yourself up, you rescued your"
                     + " beloved princess out of the cage and took her"
                     + " out of here for good.")
            self.say("""
          .....
          WWWWW
         ((. .))
        ))) - (((
      ((((`...')))
      ))))\\  /(((
      /    \\/    \\
     / /\\      /\\ \\
    / /  \\    /  \\ \\
   @@@@  / \\/ \\  @@@@
   (v   /      \\   v)
       @@@@@@@@@@
      /          \\
     /            \\
    @@@@@@@@@@@@@@@@
   /                \\
  /                  \\
 @@@@@@@@@@@@@@@@@@@@@@
 /                    \\
@@@@@@@@@@@@@@@@@@@@@@@@      A princess
         v  v
""")
            self.say("VICTORY, you get to live forever after"
                     + " with your beloved princess.")
            self.say("""
,.-.                        ,.-·.                  ,. - .,                  ,  . .,  °           , ·. ,.-·~·.,   ‘         ,. -  .,                  ,-·-.          ,'´¨;
/   ';\\ '                    /    ;'\\'           ,·'´ ,. - ,   ';\\        ;'´    ,   ., _';\\'        /  ·'´,.-·-.,   `,'‚       ,' ,. -  .,  `' ·,           ';   ';\\      ,'´  ,':\\'
';    ;:'\\      ,·'´';        ;    ;:::\\      ,·´  .'´\\:::::;'   ;:'\\ '     \\:´¨¯:;'   `;::'\\:'\\      /  .'´\\:::::::'\\   '\\ °     '; '·~;:::::'`,   ';\\         ;   ';:\\   .'   ,'´::'\\'
';   ;::;     ,'  ,''\\      ';    ;::::;'    /  ,'´::::'\\;:-/   ,' ::;  '     \\::::;   ,'::_'\\;'   ,·'  ,'::::\\:;:-·-:';  ';\\‚      ;   ,':\\::;:´  .·´::\\'       '\\   ';::;'´  ,'´::::;'
';   ';::;   ,'  ,':::'\\'     ;   ;::::;   ,'   ;':::::;'´ ';   /\\::;' '           ,'  ,'::;'  ‘    ;.   ';:::;´       ,'  ,':'\\‚     ;  ·'-·'´,.-·'´:::::::';        \\  '·:'  ,'´:::::;' '
';   ;:;  ,'  ,':::::;'    ';  ;'::::;    ;   ;:::::;   '\\*'´\\::\\'  °           ;  ;:::;  °     ';   ;::;       ,'´ .'´\\::';‚  ;´    ':,´:::::::::::·´'          '·,   ,'::::::;'´
;   ;:;'´ ,'::::::;'  '   ;  ';:::';     ';   ';::::';    '\\::'\\/.'              ;  ;::;'  ‘      ';   ':;:   ,.·´,.·´::::\\;'°   ';  ,    `·:;:-·'´                ,'  /::::::;'  '
';   '´ ,·':::::;'        ';  ;::::;'     \\    '·:;:'_ ,. -·'´.·´\\‘            ;  ;::;'‚         \\·,   `*´,.·'´::::::;·´      ; ,':\\'`:·.,  ` ·.,             ,´  ';\\::::;'  '
,'   ,.'\\::;·´           \\*´\\:::;‘      '\\:` ·  .,.  -·:´::::::\\'           ',.'\\::;'‚          \\\\:¯::\\:::::::;:·´         \\·-;::\\:::::'`:·-.,';           \\`*ª'´\\\\::/‘
\\`*´\\:::\\;     ‘         '\\::\\:;'         \\:::::::\\:::::::;:·'´'             \\::\\:;'‚           `\\:::::\\;::·'´  °           \\::\\:;'` ·:;:::::\\::\\'          '\\:::::\\';  '
 '\\:::\\;'                   `*´‘            `· :;::\\;::-·´                   \\;:'      ‘           ¯                       '·-·'       `' · -':::''           `*ª'´‘
   `*´‘                                                                       °                   ‘                                                         '
""") # noqa
