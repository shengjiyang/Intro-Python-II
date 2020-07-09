# src/item.py

from room import Room

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"name: {self.name}, description: {self.description}"

    # def on_take(self):
    #     print(f"You have picked up the {self.name}")

    # def on_drop(self):
    #    print(f"You have dropped the {self.name}")


# class Weapon(Item):
#     def __init__(self, name, description, damage, durability, slot="weapon"):
#         super().__init__(name, description)
#         self.damage = damage
#         self.durability = durability 


# class Armor(Item):
#     def __init__(self, name, description, slot, AC, durability):
#         super().__init__(name, description)
#         self.slot = slot
#         self.AC = AC
#         self.durability = durability


