"""
Quiz.

A simple quiz game with bonuses too.
"""

__author__ = "Tania Saisod"
__copyright__ = "Copyright 2019, Chulalongkorn University"
__credits__ = ["Tania Saisod"]
__license__ = "AGPL"
__version__ = "1.0.0"
__maintainer__ = "Dr Andrew King"
__email__ = "sheepchaan@gmail.com"
__status__ = "Production"


def question(level, prob):
    """Print the question."""
    print("Level " + str(level) + ": " + prob + " = ?")


def bonus():
    """Do the bonus question."""
    global hp
    q = ["What is the capital city of Thailand?",
         "What clothing is always sad?",
         "What two words contain thousands of letters?"]
    c = [["a: Bangkok ", "b: Phuket", "c: Krabi", "d:Pattaya"],
         ["a:pajamas", "b:blue jean", "c:skirt", "d:socks"],
         ["a: let ter", "b: thou sand", "c:post office", "d:good luck"]]
    ans = ['a', 'b', 'c']
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
    """Check if player is still here."""
    if (hp == 0):
        return False
    return True


def choice(a, b, c, d):
    """Show the choices."""
    global hp, wrong
    print("A: " + str(a))
    print("B: " + str(b))
    print("C: " + str(c))
    print("D: " + str(d))


def check(ch, ans):
    """Check the correct answer."""
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
    print("(Instructions)")
    print("1.You have 5 chances")
    print("2.If your live is 3, you will have chance to answer bonus question")
    print("3.If your live is 0 = GAME OVER")
    begin = input("Type [start] to begin a game: ")

print("------START------")
while (not finished):
    hp = 5
    wrong = 0
    question(1, "Which country produce most copper?")
    choice('China', 'Thailand', 'Brazil', 'USA')
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
    print('Congratulations! Game Completed!')
    finished = True
