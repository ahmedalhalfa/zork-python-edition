import sys
from modules import animals, events, places, utils
import data

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
        dead("the bear doesn't understand that, you are eaten anyway, RIP!")
        
    if open_door and moved_bear :
        events.enter()
    else :
        events.dead("the bear catches you and eats you in one shot yet again!, RIP")

def ape () :
    pass

def gorilla () :
    pass

def lion () :
    pass
