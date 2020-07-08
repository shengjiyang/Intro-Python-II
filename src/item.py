# src/item.py

from player import Player
from room import Room

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description

    def __str__(self):
        return f"name: {self.name}, description: {self.description}"

    def on_take(self):
        print("You have picked up the {self.name}")

    def on_drop(self):
        print("You have dropped the {self.name} in the {player.current_room.name}")