# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to, s_to, e_to, w_to):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = []

    def player_takes_item(item):
        if item is in self.items:
            self.items.remove(item)
            print(f"{item} added to inventory.")
        elif item is not in self.items:
            print(f"There is no {item} to be found.")
