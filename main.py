import os
import math
from random import *
from os.path import exists


def EasyNumber():
    return randint(1,10)
def MediumNumber():
    return randint(1,50)
def HardNumber():
    return randint(1,100)
def SaveScore(s):
    V = open("HighScore.txt", "r")
    fx = V.read()
    V.close()
    newscore = int(fx[:]) + int(s)
    f = open("HighScore.txt", "w")
    f.write(str(newscore))
    f.close()
    return s
def userscore():
    if exists("HighScore.txt") == False:
        f = open("HighScore.txt", "w")
        f.write("0")
        f.close()
        return "0"
    else:
        f = open("HighScore.txt", "r")
        fx = f.read()
        return fx
def game(randomInt,a,b):
    points = 50

    Hintcount = 0
    isLoser = False
    correct = ["well played","perhaps you cheated","Correcto mundo"]
    lechange = randint(0,2)
    print("Let us begin 😁")

    while isLoser != True:
        userinput = input(f"guess the number between {a} & {b} :p \n")
        if userinput == str(randomInt):
            isLoser = True
            SaveScore(str(points))
            print(f"\n {correct[lechange]} you scored:{points} points")# make a list that randomly tells you different ways of say correct
        elif userinput.isdigit() == False:
            print("wrong input D: please use numbers :ps just for that -10 points >:|")
            points -= 10
        elif int(userinput) > randomInt:
            print("Nope to High")
            points -= 2
            Hintcount += 1
            print(Hintcount)
            if Hintcount == 2:
                if randomInt % 2 == 0:
                    print("Hint: the number can be divided into  2")
                    points -= 4
                else:
                    print("Hint: the number cannot be divided into  2")
                    points -= 4
            elif Hintcount == 3:
                    randhint = randint(1,8)
                    print(f"Second hint: if i add together {randhint} and the hidden value i get {randhint+randomInt}")
                    points -= 8
            elif Hintcount == 4:
                    print(f"Last chance buddy the sqr root of the number is {math.sqrt(randomInt)}")
                    points -= 8
            elif Hintcount == 5:
                    print(f"pfft what a loser you could not guess {randomInt}")
                    isLoser = True


        elif int(userinput) < randomInt:
            print("Nope to low")
            points -= 2
            Hintcount += 1
            print(Hintcount)
            if Hintcount == 2:
                if (randomInt % 2 == 0):
                    print("Hint: the number can be divided into  2")
                    points -= 4
                else:
                    print("Hint: the number cannot be divided into  2")
                    points -= 4
            elif Hintcount == 3:
                    randhint = randint(1,5)
                    print(f"Second hint: if i add together {randhint} and the hidden value i get {randhint+randomInt}")
                    points -= 8
            elif Hintcount == 4:
                    print(f"Last chance buddy the sqr root of the number is {math.sqrt(randomInt)}")
                    points -= 8

            elif Hintcount == 5:
                    print(f"pfft what a loser you could not guess {randomInt}")
                    isLoser = True

        else:

            print(randomInt)

userinput = int()

while userinput != "9":
    print(f"Your current score: {userscore()}")
    print("welcome to the Number Guessing game \n Please select a Difficulty level")
    userinput = input(" 1.Easy (1 to 10) \n 2.medium (1 to 50) \n 3.Hard(1, to 100) \n\n\n9 to Exit game \n")

    if userinput == "1":
        game(EasyNumber(), 1, 10)
    elif userinput == "2":
        game(MediumNumber(), 1, 50)
    elif userinput == "3":
        game(HardNumber(), 1, 100)
    elif userinput == "9":
         print("bye user ^^")
    else:
        print("invalid input my good user be sure to  follow instructions ^-^\"")
