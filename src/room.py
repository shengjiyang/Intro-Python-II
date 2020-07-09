# Implement a class to hold room information. This should have name and
# description attributes.

import pandas as pd

class Room:
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        
        self.item = []
        self.name_ = []

        self.items = pd.DataFrame({"item" : self.item, "name" : self.name_})

    def __str__(self):
        return f"name : {self.name}, description : {self.description}"

