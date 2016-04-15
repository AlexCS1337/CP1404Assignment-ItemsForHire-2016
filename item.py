""" CP1404 Assignment 1 - 2016
    ItemsForHire - item.py
    Alex Silva
    15/04/2016
    https://github.com/AlexCSilva/CP1404Assignment1-ItemsForHire

Class Item Pseudocode
"""


class Item:
    def __init__(self, name="", description="", cost=0.0, status=""):
        """ initialise an Item instance
        name: name of item, description: brief description of item
        cost: float, status: in or out """
        self.name = name
        self.description = description
        self.cost = cost
        self.status = status