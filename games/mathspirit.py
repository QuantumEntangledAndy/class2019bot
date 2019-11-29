"""
Math spirit.

Why ghosts should not like math.
"""


__author__ = "Atiwit Intarasorn"
__copyright__ = "Copyright 2019, Chulalongkorn University"
__credits__ = ["Atiwit Intarasorn"]
__license__ = "AGPL"
__version__ = "1.0.0"
__maintainer__ = "Dr Andrew King"
__email__ = "sheepchaan@gmail.com"
__status__ = "Production"


def question(level, prob):
    """Display a question to the user."""
    print("Level " + str(level) + ": " + prob + " = ?")


def bonus():
    """Do the bonus question."""
    global hp
    q = ["(120/6)+78", "(91-25)/11", "(34+47)/9"]
    c = [["A: 95", "B: 96", "C: 97", "D: 98"],
         ["A: 5", "B: 6", "C: 7", "D: 8"],
         ["A: 9", "B: 10", "C: 11", "D: 12"]]
    ans = ['d', 'b', 'a']
    global wrong
    print("Bonus", str(wrong) + ": ", q[wrong - 1], "  = ?")
    for i in range(4):
        print(c[wrong - 1][i])
    ch = input("Answer: ")
    if str(ch) == ans[wrong - 1]:
        hp += 1
        print("Congrats, you won a bonus question. HP : ", hp)
    else:
        hp -= 1
        wrong += 1


def alive():
    """Check if player is alive."""
    if (hp == 0):
        return False
    return True


def choice(a, b, c, d):
    """Display the choices."""
    global hp, wrong
    print("A: " + str(a))
    print("B: " + str(b))
    print("C: " + str(c))
    print("D: " + str(d))


def check(ch, ans):
    """Check for correct answer."""
    global hp, wrong
    if str(ch) == ans:
        print("Congrats HP : ", hp)
    else:
        hp -= 1
        print("Wrong! You have ", hp, "HP left")
    if hp == 1 and wrong < 3:
        wrong += 1
        bonus()


begin = ''
finished = False
while(begin != 'start'):
    print("In the middle of the town they was a very old school with a"
          + " magical look. One day in late night one boy he forgets his bag"
          + " in the class so he have to go back to the school .When the boy"
          + " arrived to the school he went up to his class but there was"
          + " something wrong with the school’s atmosphere. The air was cold,"
          + " the lights was blinking,the place was very quite so he can "
          + " here his heartbeat he keep walking through the hallway till"
          + " he see his class and he went in. The boy was in the class"
          + " with a weird feeling. He thinks that school in daytime and"
          + " in nighttime was completely different suddenly the door was"
          + " close with a very loud noise. At that time they are the mist"
          + " around the blackboard after the mist disappear they have"
          + " something written on the board. “If you want to be out of"
          + " this class you have to answer 10 questions.” The boy read it"
          + " in his mind and when he glanced back up to the board the"
          + " letter was changed. “You have 5 chance. After you answer"
          + " it wrong your chance will be deduct.” After reading the"
          + " boy thinks that what if his chance runs out what will be"
          + " happen. The letter on the board change again. “If your"
          + " chance goes to 1 we will have an extra help for you so"
          + " let’s start.” After that letter on the board disappears"
          + " all the locks from door and windows start to lock by itself."
          + " The boy was shocked. “The first question is ...”")
    print("You have 5 lives if you anwer wrong your live will be deduct.")
    print("The game is not that hard, you will have a chance to answer"
          + " bonus question if your lives = 1")
    print("Good Luck")
    begin = input("Type [start] to begin a game: ")

print("------START------")
while (not finished):
    hp = 5
    wrong = 0
    question(1, "59+87+48")
    choice(174, 184, 194, 204)
    ch = input("Answer: ")
    check(ch, 'd')
    if (not alive()):
        print('You died!')
        op = input('Do you want to restart(y/n) ? ')
        if op == 'y':
            continue
        else:
            break
    question(2, "62-19+37")
    choice(70, 80, 90, 100)
    ch = input("Answer: ")
    check(ch, 'b')
    if (not alive()):
        print('You died!')
        op = input('Do you want to restart(y/n) ? ')
        if op == 'y':
            continue
        else:
            break
    question(3, "85+48-56")
    choice(76, 77, 87, 97)
    ch = input("Answer: ")
    check(ch, 'b')
    if (not alive()):
        print('You died!')
        op = input('Do you want to restart(y/n) ? ')
        if op == 'y':
            continue
        else:
            break
    question(4, "83-45+37")
    choice(75, 76, 85, 86)
    ch = input("Answer: ")
    check(ch, 'a')
    if (not alive()):
        print('You died!')
        op = input('Do you want to restart(y/n) ? ')
        if op == 'y':
            continue
        else:
            break
    question(5, "91-47-18")
    choice(25, 26, 35, 36)
    ch = input("Answer: ")
    check(ch, 'b')
    if (not alive()):
        print('You died!')
        op = input('Do you want to restart(y/n) ? ')
        if op == 'y':
            continue
        else:
            break
    question(6, "82-15+78")
    choice(125, 135, 145, 155)
    ch = input("Answer: ")
    check(ch, 'c')
    if (not alive()):
        print('You died!')
        op = input('Do you want to restart(y/n) ? ')
        if op == 'y':
            continue
        else:
            break
    question(7, "36+78-58")
    choice(46, 56, 66, 76)
    ch = input("Answer: ")
    check(ch, 'b')
    if (not alive()):
        print('You died!')
        op = input('Do you want to restart(y/n) ? ')
        if op == 'y':
            continue
        else:
            break
    question(8, "61-36+48")
    choice(71, 73, 75, 77)
    ch = input("Answer: ")
    check(ch, 'b')
    if (not alive()):
        print('You died!')
        op = input('Do you want to restart(y/n) ? ')
        if op == 'y':
            continue
        else:
            break
    question(9, "45+68+37")
    choice(150, 160, 170, 180)
    ch = input("Answer: ")
    check(ch, 'a')
    if (not alive()):
        print('You died!')
        op = input('Do you want to restart(y/n) ? ')
        if op == 'y':
            continue
        else:
            break
    question(10, "91-23+15")
    choice(80, 81, 82, 83)
    ch = input("Answer: ")
    check(ch, 'd')
    if (not alive()):
        print('You died!')
        op = input('Do you want to restart(y/n) ? ')
        if op == 'y':
            continue
        else:
            break
    print('Congratulations! You made it out of the room!')
    finished = True
