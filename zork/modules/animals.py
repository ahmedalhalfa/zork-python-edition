import sys
from modules import animals, events, places, utils

"""
this module contains the functions of the reactions of the animals in the game
"""

def bear () :

    open_door = False
    moved_bear = False
    ans = input("> ")

    if ans == "fight the bear" :
        events.dead("the bear eats you in one shot, Good job!")

    elif ans == "draw its attention" :

        moved_bear = True
        ans = input("> ")
        open_door = events.try_open(ans)
    else :
        events.dead("the bear doesn't understand that, you are eaten anyway, RIP!")

    if open_door and moved_bear :
        events.enter()
    else :
        events.dead("the bear catches you and eats you in one shot yet again!, RIP")

def ape () :

    print(open("data/ape.txt",'r').read())
    ans = input("> ")

    if ans == "ignore him" :
        places.prison()

    elif ans == "banana" :
        places.gold_room_gate()

    else:
        print("What's that ?")
        animals.ape()

def gorilla () :

    print(open("data/gorilla.txt",'r').read())
    ans = input("> ")

    if ans == "run" :
        events.go_home()

    elif ans == "fight" :
        events.dead("""Oh boy, although she's cute, but your strength will never come nowhere near hers.
        so you are ripped off , RIP!""")
    elif ans == "shoot her" :
        events.shoot()
    else :
        print("you can't do that")
        animals.gorilla()
def lion (keys) :

    print(open("data/lion.txt",'r').read())
    ans = input("> ")

    if ans == "run" :
        events.enter()

    elif ans == "eat my arm" and keys :
        places.diamond_room()

    elif ans == "eat my arm" and not keys :
        events.enter()

    elif ans == "fight it" :
        events.dead("you must be kidding me, fight a lion?, RIP!")

    else:
        events.dead("Lions don't understand bullshit, RIP!")
