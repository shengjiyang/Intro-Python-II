# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__(self, name, sex, class_, current_room):
        self.name = name
        self.class_ = class_
        self.current_room = current_room
        self.inventory = []

    def get_item(item):
        self.inventory.append(item)
        player.current_room.items.remove(item)

    def drop_item(item):
        self.insventory.remove(item)
        player.current_room.items.append(item)

    def access_inventory(self):
        print("Inventory: ")
        print("---------")
        for item in self.inventory:
            print(item)

    def define_class(self):
        """
        Sets starting attribute for one of three classes,
        Knight, Rogue, or Wizard, base on the player's
        choice up front.

        Note: since I was lazy, these classes and their stats
        are quite literally copy pasted from NetHack.
        """
        if self.class_ == "knight":
            self.Str = 15
            self.Int = 8
            self.Wis = 15
            self.Dex = 8
            self.Con = 11
            self.Char = 17

        if self.class_ == "rogue":
            self.Str = 15
            self.Int = 14
            self.Wis = 14
            self.Dex = 18
            self.Con = 14
            self.Char = 8

        if self.class_ == "wizard":
            self.Str = 10
            self.Int = 18
            self.Wis = 10
            self.Dex = 13
            self.Con = 13
            self.Char = 10

        