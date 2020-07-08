from player import Player
from room import Room
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mount beckons"),

    'foyer':    Room("Foyer",
                     """Dim light filters in from the south.
Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you,
falling into the darkness. Ahead to the
north, a light flickers in the distance,
but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage",
"""The narrow passage bends here from west
to north. The smell of gold permeates the
air."""),

    'treasure': Room("Treasure Chamber",
"""You've found the long-lost treasure
chamber! Sadly, it has already been
completely emptied by earlier adventurers.
The only exit is to the south."""),
}
 
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Make a new player object that is currently in the 'outside' room.
sex = input("Art thou man or woman? ")
name = input("How shall I address thee, adventurer? ")

while True:
    
    class_ = input("What is they profession? ")
    
    class_desc = f"""The world of Aecceghar is populated by
adventurers of three main stripes,

Knights:

Knights are distinguished from the common skirmisher by their
devotion to the ideals of chivalry and by the surpassing
excellence of their armor.

Rouges:

Rogues are agile and stealthy thieves, with knowledge of locks,
traps, and poisons. Their advantage lies in surprise, which they
employ to great advantage.

Wizards:

Wizards start out with a knowledge of magic, a selection of
magical items, and a particular affinity for dweomercraft.
Although seemingly weak and easy to overcome at first sight, an
experienced Wizard is a deadly foe.
"""
    if  class_ == "knight" or class_ == "rogue" or class_ == "wizard":
        player = Player(name=name, sex=sex, class_=class_, current_room=room["outside"])
        player.define_class()
        
        print("\n")
        print(f"{name}, welcome to the magical world of Aecceghar!")
        print("\n")
        print(player.current_room.name)
        print(player.current_room.description)
        break
        
    elif class_ == "h" or class_ == "help":
        print("\n")
        print(class_desc)
            
    else:
        print("Class not defined, see class descriptions below.")
        print("\n")
        print(class_desc)

# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.

while True:

    input_ = input()

    print("\n")

    # Navigation

    if input_ == "n":
        if "n_to" in player.current_room.__dir__():
            player.current_room = player.current_room.n_to
            print(player.current_room.name)
            print(player.current_room.description)

            if len(player.current_room.items) > 0:
                print("\n")
                print("You see these items: ")
                for item in items:
                    print(item)

        elif "n_to" not in player.current_room.__dir__():
            print("There is no path in that direction, adventurer.")
        

    if input_ == "s":
        if "s_to" in player.current_room.__dir__():
            player.current_room = player.current_room.s_to
            print(player.current_room.name)
            print(player.current_room.description)

            if len(player.current_room.items) > 0:
                print("\n")
                print("You see these items: ")
                for item in player.current_room.items:
                    print(item)

        elif "s_to" not in player.current_room.__dir__():
            print("There is no path in that direction, adventurer.")
        

    if input_ == "e":
        if "e_to" in player.current_room.__dir__():
            player.current_room = player.current_room.e_to
            print(player.current_room.name)
            print(player.current_room.description)

            if len(player.current_room.items) > 0:
                print("\n")
                print("You see these items: ")
                for item in player.current_room.items:
                    print(item)

        elif "e_to" not in player.current_room.__dir__():
            print("There is no path in that direction, adventurer.")


    if input_ == "w":
        if "w_to" in player.current_room.__dir__():
            player.current_room = player.current_room.w_to
            print(player.current_room.name)
            print(player.current_room.description)

            if len(player.current_room.items) > 0:
                print("\n")
                print("You see these items: ")
                for item in items:
                    print(item)

        elif "w_to" not in player.current_room.__dir__():
            print("There is no path in that direction, adventurer.")

    # Getting and dropping items.

    if "get " in input_:
        item = input_ - "get "
        if item in player.current_room.items:
            player.get_item(item)
            item.on_take()
        else:
            print("There is no {item}")

    if "take " in input_:
        item = input_ - "take "
        if item in player.current_room.items:
            player.get_item(item)
            item.on_take()
        else:
            print("There is no {item}")

    if "drop " in input_:
        item = input_ - "drop "
        if item in player.inventory:
            player.drop_item(item)
            item.on_drop()
        else:
            print("{item} was not found in your inventory, adventurer.")

    if input_ == "i" or input_ == "inventory":
        player.access_inventory()

    # Quitting the program

    if input_ == "q":
        break