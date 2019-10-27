import sys
from modules import animals, events, places, utils
import data

def intro() :

        print(
            """
            You have arrived at an island in the middle of nowhere in the atalntic sea.
            it has a panel on its gate saying :
            welcome to the island of APES, this island lords are apes but it has also many more dangerous creatures so be carful
            and don't put yourself in danger.
            So first things first, if you want to enter the island you must firstly move the bear from the gate, secondly you need
            to answer some questions without lying or you will be put in the prison.
            """)

        print("""
            so you want to enter or go home ?
            """)
        ans = input("> ")
        return ans

def start () :

    ans = utils.intro()

    while (True) :

        if ans == "explore island" :
            events.explore()

        elif ans == "Oh that's a dangerous place, better go back to home" :
            events.go_home()

        else :
            print("apes don't understand that dude ! ")
            ans = input("> ")
