"""
A game of snake.

This is a simple branching path story.

"""

__author__ = "Pakhin Pawornwitoon"
__copyright__ = "Copyright 2019, Chulalongkorn University"
__credits__ = ["Pakhin Pawornwitoon"]
__license__ = "AGPL"
__version__ = "1.0.0"
__maintainer__ = "Dr Andrew King"
__email__ = "sheepchaan@gmail.com"
__status__ = "Production"

import time
class Event():
    def __item__(self):
        self.time_event_occured = 0
    def say(self, massage):
        time.sleep(0.5)
        print(massage)
    def choose(self, options):
        while True:
            self.say("What will you do?")
            for idx, value in enumerate(options):
                print(f"{idx+1}: {value}")
            choice = input()
            for idx, value in enumerate(options):
                if choice.lower() == value.lower():
                    return value
                if str(idx+1) == choice:
                    return value
    def enter(self):
        pass


class Start(Event):
    def enter(self):
        self.say("Jason wakes up in the forest with vague memory")
        self.say("He stands up and looks around himself")
        self.say("He looks to the left and find an axe and to the right a compass")
        answer = self.choose(["axe", "compass"])
        if answer == "axe":
            print("iI got an axe")
            return "axe"
        elif answer == "compass":
            print("It is gonna br useful, isn't it?")
            return "compass"

class Anaconda(Event):
    def enter(self):
        self.say("After walking for a while, he hears the flow of water")
        self.say("He feels very thirsty, so he walks steadily toward the sound")
        self.say("Suddenly, Anaconda jumps out of the river!!!")
        answer = self.choose(["runaway", "fight"])
        if answer == "runaway":
            self.say("Oh no!, it is faster than I expected")
            return "GAME OVER"
        elif answer == "fight":
            self.say("I can endure its agrassive attack, helppppp")
            return 'GAME OVER'

class Tiger(Event):
    def enter(self):
        self.say("After walking for along time, Jason feels extremly exhuasted")
        self.say("The sky is getting darker and derker")
        self.say("Heyyy, there is a cave ahead!!, I'm gonna take a nap there")
        self.say("In the cave, there are red eyes appearing in the dark")
        self.say("Then, the creature rush out of the dark, RRRRRRR")
        self.say("That's a huge tiger!!!")
        self.say("Jason see a big tall tree not far away")
        answer = self.choose(["fight", "climb the tree"])
        if answer == "fight":
            self.say("OUCHHH!!!, Mommmmmmm, I wanna go homeeee")
            return "GAME OVER"
        elif answer == "cilmb the tree":
            self.say("He could get away from the tiger")
            self.say("He fell asleep, until tiger got bored and went away")
            self.say("He gets down from the tree and uses the compass to guid him out of the forest")
            return "Yayyy, VICTORY"

class Death(Event):
    def enter(self):
        self.say("GAME OVER")

class Victory(Event):
    def enter(self):
        self.say("congratulation!! You are able to to get out")

def play():
    event = Start()
    result = event.enter()
    if result == 'axe':
        event = Anaconda()
        result = event.enter()
        print("YOU DIED")
        return
    elif result == 'compass':
        event = Tiger()
        result = event.enter()
        if result == 'GAME OVER':
            print("YOU DIED")
            return
        else:
            print("YOU WON")

            return
    else:
        raise ValueError(f"RESULT NOT HANDELLED {result}")

play()
