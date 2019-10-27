import sys
from modules import animals, events, places, utils
import data

def dead(s):
    print(s)
    input("Game Over")
    exit(0)

def explore():

    print("""
        So you have chosen to explore the island of the apes but as the rules tell, you gotta do the objectives first !
        """)
    print(" now you face the bear ! Dum dah dum")

    animals.bear()

def go_home():
    print("Oh little boy, you don't have the balls to do it, do you? ")
    input("Game finished")
    exit(0)

def try_open (ans):
        if ans == "open the door" :
            return True

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
