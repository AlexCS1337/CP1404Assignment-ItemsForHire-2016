""" CP1404 Assignment 1 - 2016
    ItemsForHire
    Alex Silva
    02/04/2016
    https://github.com/AlexCSilva/CP1404Assignment1-ItemsForHire

Class Item Pseudocode
"""


class Item:
    def __init__(self, name="", description="", cost=0.0, status=""):
        self.name = name
        self.description = description
        self.cost = cost
        self.status = status
