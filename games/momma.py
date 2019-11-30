"""
Momma.

Time machines are nothing but trouble.
"""


__author__ = "Ranvir Koknutphongchai"
__copyright__ = "Copyright 2019, Chulalongkorn University"
__credits__ = ["Ranvir Koknutphongchai"]
__license__ = "AGPL"
__version__ = "1.0.0"
__maintainer__ = "Dr Andrew King"
__email__ = "sheepchaan@gmail.com"
__status__ = "Production"

import random
import time


class Girl():
    """All the girls are represented by this."""

    def __init__(self, name):
        """Do this initial setup of the girl."""
        self.hobbies = ['exercise', 'meditation', 'read books', 'painting',
                        'gardening', 'watching television', 'shopping']
        self.field_of_studies = ['science', 'art', 'social science',
                                 'bussiness', 'medical']
        self.careers = ['doctor', 'teacher', 'salesperson', 'researcher',
                        'artist']
        self.music_genres = ['pop', 'rock', 'jazz', 'R&B', 'classic']
        self.crusines = ['Thai', 'Japan crusine', 'Italian', 'Indian',
                         'Korean']
        self.q_check = [False, False, False, False]
        self.name = name
        self.asked_Q = 0

        self.get_random_info()

    def get_random_info(self):
        """Randomly assign traits."""
        self.hobby = random.choice(self.hobbies)
        self.field_of_study = random.choice(self.field_of_studies)
        self.music_genre = random.choice(self.music_genres)
        self.crusine = random.choice(self.crusines)


class Event():
    """Base event class."""

    def __init__(self):
        """Init the events."""
        self.hard_mode = False

    def say(self, message):
        """Tell the player something, long wait."""
        time.sleep(1.5)
        print(message)

    def say2(self, message):
        """Tell the player something, short wait."""
        time.sleep(0.5)
        print(message)

    def choose(self, options):
        """Choose an option."""
        while True:
            self.say("Choose an option:")
            for idx, option in enumerate(options):
                self.say2(f"{idx+1}: {option}")
            choice = input()
            for idx, option in enumerate(options):
                if choice == str(idx+1) or choice.lower() == option.lower():
                    return option

    def create_girls(self):
        """Create all the girls."""
        self.sarah = Girl('Sarah')
        self.grace = Girl('Grace')
        self.daisy = Girl('Daisy')
        self.nina = Girl('Nina')
        self.all_girls = [self.sarah, self.grace, self.daisy, self.nina]

    def common_value(self):
        """Make the game harder by making girls have something in common."""
        girls = self.all_girls
        random.shuffle(girls)
        girls[0].hobby = girls[1].hobby
        girls[1].field_of_study = girls[2].field_of_study
        girls[2].music_genre = girls[3].music_genre
        girls[3].crusine = girls[0].crusine

    def assign_mother(self):
        """Assign momma."""
        self.mom = random.choice(self.all_girls)
        if self.mom.field_of_study == 'science':
            self.mom.career = 'researcher'
        elif self.mom.field_of_study == 'art':
            self.mom.career = 'artist'
        elif self.mom.field_of_study == 'social science':
            self.mom.career = 'teacher'
        elif self.mom.field_of_study == 'bussiness':
            self.mom.career = 'salesperson'
        elif self.mom.field_of_study == 'medical':
            self.mom.career = 'doctor'

    def difficulty(self):
        """Set the difficulty."""
        self.say("------------------------------")
        self.say("Please choose a difficulty. [Easy] or [Hard]")
        self.say("Note that your investigation will be harder in hard mode.")
        while True:
            choice = input()
            if 'easy' in choice.lower():
                self.hard_mode = False
                self.say2("You choose: Easy Mode")
                return None
            elif 'hard' in choice.lower():
                self.hard_mode = True
                self.say2("You choose: Hard Mode")
                return None

    def what_girl(self):
        """Pick a girl to question."""
        self.say("\nWhich girl would you like to ask?")
        choices = self.choose(["Sarah", "Grace", "Daisy", "Nina"])
        return choices

    def object_name(self, name_str):
        """Get girl by name."""
        if name_str == "Sarah":
            return self.sarah
        elif name_str == "Grace":
            return self.grace
        elif name_str == "Daisy":
            return self.daisy
        elif name_str == "Nina":
            return self.nina

    def check_q(self, name):
        """Check if you can ask another question."""
        if name.asked_Q >= 2:
            self.say("\nYou can't ask any more questions")
            return False
        else:
            return True

    def ask_q(self, name):
        """Ask the girl a question."""
        self.say("\nWhat do you want to ask about her?")
        choices = self.choose(["Hobby", "Field of Study", "Favourite Crusine",
                               "Favourite Song Genre"])
        if self.hard_mode:
            answer_reveal = random.randint(0, 1)
            if answer_reveal == 0:
                name.asked_Q += 1
                self.say(f"\n[The Boy] What is your {choices.lower()}?")
                self.say(f"[{name.name}] Why are you asking that? I don’t"
                         + " want to answer that question, sorry.")
                self.say("[The Boy] I... I'm sorry.\n")
                return 'Not answer'
        if choices == "Hobby" and not name.q_check[0]:
            name.asked_Q += 1
            self.say(f"\n[The Boy] What is your {choices.lower()}?")
            self.say(f"[{name.name}] Oh, my hobby is {name.hobby}.")
            self.say("[The Boy] Thanks for the answer.\n")
            name.q_check[0] = True
            return name.hobby
        elif choices == "Field of Study" and not name.q_check[1]:
            name.asked_Q += 1
            self.say(f"\n[The Boy] What is your {choices.lower()}?")
            self.say(f"[{name.name}] I'm studying {name.field_of_study}.")
            self.say("[The Boy] Thanks for the answer.\n")
            name.q_check[1] = True
            return name.field_of_study
        elif choices == "Favourite Crusine" and not name.q_check[2]:
            name.asked_Q += 1
            self.say(f"\n[The Boy] What is your {choices.lower()}?")
            self.say(f"[{name.name}] I love {name.crusine} crusine!"
                     + " That's my favourite.")
            self.say("[The Boy] Thanks for the answer.\n")
            name.q_check[2] = True
            return name.crusine
        elif choices == "Favourite Song Genre" and not name.q_check[3]:
            name.asked_Q += 1
            self.say(f"\n[The Boy] What is your {choices.lower()}?")
            self.say(f"[{name.name}] I like to listen to {name.music_genre}"
                     + " songs.")
            self.say("[The Boy] Thanks for the answer.\n")
            name.q_check[3] = True
            return name.music_genre
        else:
            self.say("\nYou have already asked that question.")
            self.say("Try another question.")
            return 'Not answer'

    def cont(self, name, list_q):
        """Ask what to do next."""
        while True:
            self.say("\nHow would you like to continue?")
            resume = self.choose(list_q)
            if resume == 'Ask more question about her':
                return 'ask_q'
            if resume == 'Ask someone else':
                return 'what_girl'
            if resume == 'End the investigation':
                self.say("\nAre you sure that you have all information"
                         + "that you needed?")
                confirm = self.choose(["Yes", "No"])
                if confirm == "Yes":
                    return 'END'

    def select_girl(self):
        """Select a girl as your momma."""
        trial = 0
        while True:
            self.say("\nWho do you think is your real future mother?")
            choices = self.choose(["Sarah", "Grace", "Daisy", "Nina"])
            if choices == self.mom.name:
                return 'WIN'
            else:
                if not self.hard_mode or trial >= 1:
                    return 'LOSE'
                elif self.hard_mode:
                    self.say("You choose the wrong answer.")
                    self.say("You will have another chance to choose.")
                    trial += 1


class Story(Event):
    """The story event."""

    def intro(self):
        """Start the intro."""
        self.say("Once upon a time, in the land of sophisticated innovation,"
                 + " the boy accidentally walked into a time machine.")
        self.say("[The Boy] Oh! Awwww! My head is aching!! I’m about to throw"
                 + " up now! BBLLAARGGHH!!")
        self.say("[The Boy] Oh the machine stop spinning. Where am I now! Oh"
                 + " god damn its 1960!")
        self.say("He saw his dad and be able to recognize him. By the way. He"
                 + " was shocked that he can’t remember any of his mother’s"
                 + " appearance.")
        self.say("After wandering around his parent’s college, the boy saw his"
                 + " dad talking with a bunch of girls!")
        self.say("[The Boy] Oh my goodness! If he marries another woman,"
                 + " beside my mom. What should I do now!! I will not be"
                 + " born!!!")
        self.say("The boy cries as loud as rainstorm in the middle of the"
                 + " ocean, unknowing of his future that he will still stay"
                 + " alive in the time where he came from.")
        self.say("Players! We would like you to help us find his real mother,"
                 + " in order to let he be survived by investigating four of"
                 + " his father’s college girl.")
        self.say("Select one of the four that you think that is his real"
                 + " mother")
        self.say("GOOD LUCK. LET’S THE INVESTIGATION BEGINS!!\n")

    def mother_info(self, mom):
        """Intro your momma."""
        self.say2("------------------------------")
        self.say("\n[The Boy] (thinking…) Now...what do I remember about"
                 + " my mother?")
        self.say("Wow... the time machine seems to have erased some of"
                 + " my memory... ")
        self.say("[The Boy] I can't even remember her name...")
        self.say("[The Boy] Let me jot down what I remember...\n")
        self.say2("------------")
        self.say(f"'My Mother'\n   Favorite Cuisine: {mom.crusine.title()}\n"
                 + "  Career: {mom.career.title()}\n   Favourite Music Genre:"
                 + " {mom.music_genre.title()}\n   Hobby: {mom.hobby.title()}")
        self.say2("------------")

    def direction(self):
        """Talk to your dadda."""
        self.say("\nThen, you have a serious talk with your dad...")
        self.say("...")
        self.say("[The Boy] ... and that is all I can remember... *sigh*")
        self.say("[Dad] Oh, so you are... 'my son'...?")

        self.say("[The Boy] *nods*")
        self.say("[Dad] My son… in order to solve the mystery of who is"
                 + " your real mother you will have to investigate four of"
                 + " my girlfriends.")
        self.say("[Dad] Their names are Sarah, Grace, Daisy and Nina.")
        self.say("[Dad] Good Luck!")
        self.say2(".\n.")
        self.say("--- Note: You are only allowed to ask two questions per"
                 + " girl. ---")
        self.say("--- Note: Different girls may possess similar"
                 + " characteristics. ---")
        self.say2(".\n.")

    def girl_talk(self, name):
        """Talk to a girl."""
        self.say(f"\n[The Boy] Excuse me...are you {name.name}?")
        self.say(f"[{name.name}] Yes...that is me.")
        self.say("[The Boy] I’m sorry to disturb you. Can I ask you"
                 + " a few questions?")
        self.say("[The Boy] It is very important... please don’t mind...")

    def end_invest(self):
        """Stop the investigation."""
        self.say("\nIt seems like you are ready to find the truth...")
        self.say("The boy go back and have another talk with his dad...")
        self.say("...")
        self.say("[DAD] So?? Now that you have spoken to all the girls..."
                 + " who do you think is your real mother?\n")

    def good_end(self):
        """Play the good end."""
        self.say("\nCongrats! Your select your right mother!")
        self.say("[The Boy] YA HOO! I will be born in my time!")
        self.say("[The Boy] Now I’m so tired. I will rest now!")
        self.say("[The Boy] zzZZZ zzZZZ")
        self.say("Years ahead in the future...we find ourselves in a"
                 + " delivery room of a hospital.")
        self.say("After hours of labour...the anxious parents found peace"
                 + " in the sound of a baby wailing...")
        self.say("[BABY] Waah! Waaah!")
        self.say("[PARENTS] Oh my ...what a wonderful baby...he has done"
                 + " so much for us already.")
        self.say(" ")
        self.say("""
                ================
                Congratulations
                you have won!
                We hope you enjoyed
                our lovely game!
                ================
                Creators: Krittin T. , Porsuk P. , Ranvir K. , Theerasit S.
                """)

    def bad_end(self):
        """Do the thing that happens when your screw up."""
        self.say("\nUnfortunately, that girl you chosen is not your"
                 + " real mother!")
        self.say("You realised that you have fail your most"
                 + " important decision.")
        self.say("And that is your last decision...")
        self.say("Your body is fading away... you don't know why...")
        self.say("You chose poorly, and you shall pay the price with your"
                 + " existence.")
        self.say("And then the boy disappeared.")
        self.say(" ")
        self.say("""
                =================
                You LOOSE the game.
                Please try again...
                =================
                Creators: Krittin T. , Porsuk P. , Ranvir K. , Theerasit S.
                """)


class Game(Event):
    """The actual Momma game."""

    def play(self):
        """Play the game."""
        event = Event()
        story = Story()

        event.create_girls()
        event.common_value()
        event.assign_mother()

        # Intro Part
        story.intro()
        event.difficulty()
        story.mother_info(event.mom)

        # Investigation Loop Part
        loop = "what_girl"
        while loop == "what_girl":
            girl_name_str = event.what_girl()
            girl_name = event.object_name(girl_name_str)
            story.girl_talk(girl_name)

            loop = "ask_q"
            while loop == "ask_q":

                if event.check_q(girl_name):
                    event.ask_q(girl_name)
                    loop = event.cont(girl_name, ["Ask more question"
                                                  + " about her",
                                                  "Ask someone else",
                                                  "End the investigation"])

                else:
                    self.say("Sorry, you have already asked her 2 questions!")
                    self.say("You can't ask each girl more than 2 questions.")
                    loop = event.cont(girl_name, ["Ask someone else",
                                                  "End the investigation"])

        # Final Selection Part
        story.end_invest()
        result = event.select_girl()

        if result == "WIN":
            story.good_end()
        elif result == "LOSE":
            story.bad_end()


game = Game()


# Play the game here

game.play()
