# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def get_item(item):
        self.inventory.append(item)
        player.current_room.items.remove(item)

    def drop_item(item):
        self.insventory.remove(item)
        player.current_room.items.append(item)