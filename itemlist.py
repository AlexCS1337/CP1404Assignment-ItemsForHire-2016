""" CP1404 Assignment 1 - 2016
    ItemsForHire - itemlist.py
    Alex Silva
    15/04/2016
    https://github.com/AlexCSilva/CP1404Assignment1-ItemsForHire

Class ItemList Pseudocode
"""
from item import Item

class ItemList:
    def __init__(self, items=None):
        self.items = []
        for item in items:
            self.items.append(Item(item[0], item[1], float(item[2]), item[3]))

    def add_items(self):
        pass

    def get_item(self, name):
        pass

