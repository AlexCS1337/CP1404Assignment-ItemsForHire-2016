__author__ = 'Alex Silva'


"""
Application created by Alex Silva
08/05/16
CP1404 Assignment 1 - 2016
    ItemsForHire - itemlist.py
    Alex Silva
    https://github.com/AlexCSilva/CP1404Assignment1-ItemsForHire

pseudocode:
import app
import builder

class EquipmentHire(App)
    function build(self)

"""

# Imports necessary modules for a kivy app
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

from itemlist import ItemList
from item import Item

#Global variables
#To be implemented

class EquipmentHire(App):
    """ Information here """


    def build(self):
        """ Build kivy app from the kv file """
        self.title = "Equipment Hire"
        self.root = Builder.load_file('gui.kv')
        return self.root

    def press_add(self):
        """
        Handler for pressing the add button
        :return: None
        """
        self.status_text = "Enter details for new Item"
        # this opens the popup
        self.root.ids.popup.open()


EquipmentHire().run()