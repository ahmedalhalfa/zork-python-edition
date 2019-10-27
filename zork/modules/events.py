import sys
from modules import animals, events, places, utils
import data

def dead(s):
    print(s)
    exit(0)

def explore():

    print("""
        So you have chosen to explore the island of the apes but as the rules tell, you gotta do the objectives first !
        """)
    print(" now you face the bear ! Dum dah dum")

    animals.bear()

def go_home():
    print("Oh little boy, you don't have the balls to enter, do you? ")
    exit(0)

def try_open (ans):
        if ans == "open the door" :
            return True

def enter() :
      pass
