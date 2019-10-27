import sys
from modules import animals, events, places, utils

"""
this contains all the utility files that project needs
"""

def intro() :

        """
        loads the game intro
        """

        print( open("data/UI_Intro.txt",'r').read())
        ans = input("> ")
        return ans

def start () :

    """
    starts the game
    """

    ans = utils.intro()

    while (True) :

        if ans == "explore island" :
            events.explore()

        elif ans == "Oh that's a dangerous place, better go back to home" :
            events.go_home()

        else :
            print("apes don't understand that dude ! ")
            ans = input("> ")
