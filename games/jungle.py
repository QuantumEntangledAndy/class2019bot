"""
The Jungle Survial Game.

Authours:  Thitaporn Petchpadoong
"""

start = True


def gameOver():
    print("Game Over. Start Again.")
    print("=" * 95)

def stage1():
    print("=" * 95)
    print("Welcome to the Jungle!!!")
    print("There are many dangerous creatures such as monkeys, hippos, tigers, and cannibals.")
    print("In order to survive in this jungle, you need to build a house to protect yourself from them.")
    score = 0
    print("Level 1: Build a house that will keep you away from the dangerous monkeys.")
    print("1. wood")
    print("2. hay")
    print("3. clay")
    answer = input("your material: ")
    answer = answer.lower()
    if answer == "wood":
        score += 3
    elif answer == "hay":
        score += 1
    elif answer == "clay":
        score += 2
    else:
        score += 0

    if score == 3:
        stage2()
    else:
        gameOver()

def stage2():
    score = 0
    print("Level 2: Build a house that will keep you away from the aggressive hippos.")
    print("1. brick")
    print("2. wood")
    print("3. rock")
    answer = input("your material: ")
    answer = answer.lower()
    if answer == "brick":
        score += 3
    elif answer == "wood":
        score += 1
    elif answer == "rock":
        score += 2
    else:
        score += 0

    if score == 3:
        stage3()
    else:
        gameOver()
def stage3():
    score = 0
    print("Level 3.1 Build a house that will keep you away from the hungry tigers.")
    print("1. stainless steel")
    print("2. brick")
    print("3. concrete")
    print("4. gold")
    answer = input("your material:")
    answer = answer.lower()
    if answer == "stainless steel":
        score += 4
    elif answer == "brick":
        score += 1
    elif answer == "concrete":
        score += 2
    elif answer == "gold":
        score += 3
    else:
        score += 0
    print("Level 3.2 In order to survive from these hungry tigers, you need to choose your weapon.")
    print("1. saucepan")
    print("2. spears")
    print("3. bacon")
    answer = input("your weapon:")
    answer = answer.lower()
    if answer == "spears":
        score += 3
    elif answer == "saucepan":
        score += 1
    elif answer == "bacon":
        score += 10
    else:
        score += 0

    if score >= 7:
        stage4()
    else:
        gameOver()

def stage4():
    global start
    score = 0
    print("Level 4.1 Build a house that will keep you away from the savage cannibals")
    print("1. concrete")
    print("2. glass")
    print("3. stainless steel")
    print("4. gold")
    answer = input("your material:")
    answer = answer.lower()
    if answer == "concrete":
        score += 2
    elif answer == "glass":
        score += 1
    elif answer == "gold":
        score += 3
    elif answer == "stainless steel":
        score += 4
    else:
        score += 0

    print("Level 4.2 In order to survive from these save cannibals, you need to choose your weapon.")
    print("1. carrots")
    print("2. shotguns")
    print("3. tennis bat")
    answer = input("your weapon:")
    answer = answer.lower()
    if answer == "carrots":
        score += 1
    elif answer == "shotguns":
        score += 10
    elif answer == "tennis bat":
        score += 2
    else:
        score += 0
    if score >= 6:
        print("Congrats! You win")
        start = False
    else:
        gameOver()




while start:
    stage1()
