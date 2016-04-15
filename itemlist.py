""" CP1404 Assignment 1 - 2016
    ItemsForHire - itemlist.py
    Alex Silva
    15/04/2016
    https://github.com/AlexCSilva/CP1404Assignment1-ItemsForHire

Class ItemList Pseudocode
"""


class ItemList:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items
