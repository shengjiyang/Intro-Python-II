# item.py

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description

    def __str__(self):
        return f"name: {self.name}, description: {self.description}"