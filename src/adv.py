from player import Player
from room import Room

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
name = input("How shall I address thee, squire? ")
player = Player(name=name, current_room=room["outside"])

print("\n")

# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.

print(f"{name}, welcome to the magical world of Aecceghar!")
print("\n")
print(player.current_room.name)
print(player.current_room.description)

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
            print("There is no path in that direction, squire.")
        

    if input_ == "s":
        if "s_to" in player.current_room.__dir__():
            player.current_room = player.current_room.s_to
            print(player.current_room.name)
            print(player.current_room.description)

            if len(player.current_room.items) > 0:
                print("\n")
                print("You see these items: ")
                for item in items:
                    print(item)

        elif "s_to" not in player.current_room.__dir__():
            print("There is no path in that direction, squire.")
        

    if input_ == "e":
        if "e_to" in player.current_room.__dir__():
            player.current_room = player.current_room.e_to
            print(player.current_room.name)
            print(player.current_room.description)

            if len(player.current_room.items) > 0:
                print("\n")
                print("You see these items: ")
                for item in items:
                    print(item)

        elif "e_to" not in player.current_room.__dir__():
            print("There is no path in that direction, squire.")


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
            print("There is no path in that direction, squire.")

    # Getting and dropping items.

    if "get " in input_:
        item = input_ - "get "
        if item in player.current_room.items:
            player.get_item(item)
            print("You take the {item}")
        else:
            print("There is no {item}")

    if "take " in input_:
        item = input_ - "take "
        if item in player.current_room.items:
            player.get_item(item)
            print("You take the {item}")
        else:
            print("There is no {item}")
            
    # Quitting the program

    if input_ == "q":
        break