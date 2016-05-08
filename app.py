__author__ = 'Alex Silva'


"""
Application created by Alex Silva
08/05/16

pseudocode:
import app
import builder

class EquipmentHire(App)
    function build(self)

"""

# Imports necessary modules for a kivy app
from kivy.app import App
from kivy.lang import Builder

#Global variables
#To be implemented

class EquipmentHire(App):
    """ Information here """


    def build(self):
        """ Build kivy app from the kv file """
        self.title = "Equipment Hire"
        self.root = Builder.load_file('gui.kv')
        return self.root


EquipmentHire().run()