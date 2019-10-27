"""
    in this file we just initialize the text files for the project
"""

def prepare_files() :

    open("data/ape.txt",'w').write(""" you met the guardian ape of the island """)

    open("data/bear.txt",'w').write("""
        So you have chosen to explore the island of the apes but as the rules tell, you gotta do the objectives first !
        now you face the bear ! Dum dah dum
        """)

    open("data/gorilla.txt",'w').write(""" Good job!
    you have escaped the prison but now you have to face the mighty gorilla
    the strongest yet cuttiest creature on the island.
    it has the key to happiness.""")

    open("data/lion.txt",'w').write(""" you are facing the lion right now, what you are going to do ? """)

    open("data/UI_Intro.txt",'w').write("""
    You have arrived at an island in the middle of nowhere in the atalntic sea.
    it has a panel on its gate saying :
    welcome to the island of APES, this island lords are apes but it has also many more dangerous creatures so be carful
    and don't put yourself in danger.
    So first things first, if you want to enter the island you must firstly move the bear from the gate.

    so you want to enter or go home ?
    """)
prepare_files()
