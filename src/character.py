# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
from item import Item
import pandas as pd

class Player:
    def __init__(self, name, sex, class_, current_room):
        self.name = name
        self.class_ = class_
        self.current_room = current_room
        self.inventory = []

    def get_item(item):
        # self.inventory.append(item)
        self.current_room.items = self.current_room.items.drop(self.current_room.items[self.current_room.items == item].index[:1])

    def drop_item(self, item):
        self.inventory = self.inventory.drop(self.inventory[self.inventory["name"] == item].index[:1])

        # Due to a pesky TypeError, I wound up opting for this
        # print statement in lieu of adding an on_drop() method
        # to the Item class.       
        print(f"You have dropped the {item}.")

    def access_inventory(self):
        print("Inventory: ")
        print("---------")
        for item in self.inventory["item"]:
            print(f"{item.name}, {item.description}")

    def search(self):
        print("You see: ")
        print("---------")
        for item in self.current_room.items["item"]:
            print(f"{item.name}, {item.description}")

    def define_class(self):
        """
        Sets starting attribute for one of three classes,
        Knight, Rogue, or Wizard, base on the player's
        choice up front.

        Note: since I was lazy, these classes, their stats and their
        starting items are quite literally copy pasted from
        Diablo --albeit their descriptions are taken from NetHack.
        """
        if self.class_ == "knight":

            # starting attributes
            self.Strength = 30
            self.Magic = 10
            self.Dexterity = 20
            self.Vitality = 25
            self.Life = 70
            self.Mana = 10

            # starting items
            # short_sword = Weapon(
            #     name="Short Sword",
            #     description="TODO",
            #     slot="weapon",
            #     damage=(2, 6)
            #     )

            # buckler = Armor(
            #     name="Buckler",
            #     description="TODO",
            #     slot="shield",
            #     AC=(1, 5),
            #     durability=16
            # )

            health_potion = Item(
                name="Health Potion",
                description=f"Restores 20 - 50% of player's full Life points"
            )

            inventory = [health_potion, health_potion]
            name = [str(item.name) for item in inventory]
            self.inventory = pd.DataFrame({"item" : inventory, "name" : name})


        if self.class_ == "rogue":

            # starting attributes
            self.Strength = 30
            self.Magic = 10
            self.Dexterity = 20
            self.Vitality = 25
            self.Life = 70
            self.Mana = 10 

            # starting equipment
            # short_bow = Weapon(
            #     name="Short Bow",
            #     description="TODO",
            #     slot="weapon",
            #     damage=(1, 4),
            #     durability=12
            # )

            health_potion = Item(
                name="Health Potion",
                description=f"Restores 20 - 50% of player's full Life points"
            )

            inventory = [health_potion, health_potion]
            name = [str(item.name) for item in inventory]
            self.inventory = pd.DataFrame({"item" : inventory, "name" : name})

        if self.class_ == "wizard":

            # starting attributes
            self.Strength = 30
            self.Magic = 10
            self.Dexterity = 20
            self.Vitality = 25
            self.Life = 70
            self.Mana = 10 

            # starting equipment
            # short_staff = Weapon(
            #     name="Short Staff",
            #     description="TODO",
            #     slot="weapon",
            #     damage=(2, 4),
            #     durability=25
            # )

            mana_potion = Item(
                name="Mana Potion",
                description=f"Restores 20 - 50% of player's full Mana"
            )

            inventory = [mana_potion, mana_potion]
            name = [str(item.name) for item in inventory]
            self.inventory = pd.DataFrame({"item" : inventory, "name" : name})


if __name__ == "__main__":

    health_potion = Item(
                name="Health Potion",
                description=f"Restores 20 - 50% of player's full Life points"
            )

    print(type(health_potion.__str__()))

    inventory = [health_potion, health_potion]
    name = [str(item.name) for item in inventory]
    inventory = pd.DataFrame({"item" : inventory, "name" : name})

    print(inventory)
    print(type(inventory.name[0]))
    print(len(inventory.name[0]))
    print(inventory.name[0])

    hp =  inventory['name']=="Health Potio"
    inv_hp = inventory[hp]
    print(inv_hp)

    print(len(inv_hp.index))

    def drop_item(item, inventory=inventory):
        inventory = inventory.drop(inventory[inventory["name"] == item].index)
        # self.current_room.items.append(item)

    input_ = input()

    if "drop " in input_:
        item = input_.replace("drop", " ")
        item = item.replace("  ", "")
        print(type(item))
        print(item)
        print(inventory["name"])

        boolean = inventory["name"] == item
        has_item = inventory[boolean]
        print(has_item[0])
