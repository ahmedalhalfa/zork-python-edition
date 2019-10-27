import sys
from modules import animals, events, places, utils
import data

def gold_room_gate():

    print("""
        you are the locked gold room gate !
        """)
    ans = int(input("> "))

    if ans == 123456 :
        places.gold_room()
    else :
        print("try again")
        places.gold_room_gate()

def gold_room() :

    print("""
        you have entered the gold room!
        how much gold would you take?
        """)
    ans = int(input("> "))

    if ans >= 0 and ans <= 50 :
        print("""good thing, you are not greedy
                 but bad thing is that's not enough actually to proceed """)
        events.enter()

    elif ans > 50 :
        print("""well you are a greedy dick sucker bitch
                congrats on proceeding !""")
        animals.lion(False)

    else :
        print(" you kidding ?")
        places.gold_room()

def diamond_room():

    print("""And eventually, you have arrived at the diamond room
            How much would you take ?""")
    ans = int(input("> "))

    if ans >=0 and ans <= 100 :
        print("after being greedy last time, you have improved and became a better person, Good job!")
        exit(0)
    elif ans >=101 :
        print("Still the same greedy AF perso, Good job!")
        exit(0)
    else :
        print("we are not joking reight here !")
        places.diamond_room()

def prison():

    print(""" The ape has put you in the prison
    could you escape master intelligent ?""")
    ans = input("> ")
    escape = events.try_open(ans)

    if escape :
        animals.gorilla()
    else :
        events.dead("Oh man you could have given the ape a banana, however you will strive here until you die, RIP!")
