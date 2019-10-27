import sys
from modules import animals, events, places, utils

"""
this module contains the functions of the events that could happen in the game
"""

def dead(s):
    print(s)
    input("Game Over")
    exit(0)

def explore():

    print(open("data/bear.txt",'r').read())

    animals.bear()

def go_home():
    print("Oh little boy, you don't have the balls to do it, do you? ")
    input("Game finished and now you can go home ! \n")
    exit(0)

def try_open (ans):
        if ans == "open the door" :
            return True
        else :
            return False
def enter() :

    print("you are at the gate")
    ans = input("> ")

    if ans == "go 50m left" :
        animals.ape()

    elif ans == "go 50m right" :
        animals.lion(False)
    else :
        print("no you can't !")
        events.enter()

def shoot():

    print("you have to shoot her in the right spot")
    ans = input("> ")

    if ans == "headshot" :
        print("Good job, the gorilla is dead, the keys are yours")
        print("Now it's time to fight the lion, the guardian of the happiness")
        animals.lion(True)
    else :
        print("wrong shot, you better run and come later")
        events.enter()
