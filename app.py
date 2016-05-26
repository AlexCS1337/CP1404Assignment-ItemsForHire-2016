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

# Import necessary modules for the app's functionality
from itemlist import ItemList
from AlexSilvaA1 import load_items

#Defines constants
LIST_MODE = 0
HIRE_MODE = 1
RETURN_MODE = 3


class EquipmentHire(App):
    """
    Main program - Kivy app for Equiptment Hire(Assignment)
     """
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super(EquipmentHire, self).__init__(**kwargs)
        # This loads the item list from the csv
        self.itemlist = ItemList()
        self.itemlist.add_items(load_items())
        self.mode = LIST_MODE
        self.selected_items = []
        self.status_text = 'Choose action from the left menu, then select items on the right'

    def build(self):
        """ Build kivy app from the kv file """
        self.title = "Equipment Hire"
        self.root = Builder.load_file('gui.kv')
        self.create_entry_buttons()
        return self.root

    def on_stop(self):
        # get items from self.itemlist
        # call save functioon from AlexSilva1
        pass

    def press_add(self):
        """
        Handler for pressing the add button
        :return: None
        """
        self.status_text = "Enter details for new Item"
        # this opens the popup
        self.root.ids.popup.open()

    def create_entry_buttons(self):
        """
        Create the entry buttons and add them to the GUI
        :return: None
        """
        for item in self.itemlist.items:
            # create a button for each phonebook entry
            temp_button = Button(text=item.name)
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_button)

    def press_entry(self, instance):
        """
        Handler for pressing entry buttons
        :param instance: the Kivy button instance
        :return: None
        """
        # update status text
        name = instance.text
        clicked_item = self.itemlist.get_item(name)

        if self.mode == LIST_MODE:
            self.status_text = "{}'s price is ${}".format(name, clicked_item.cost)
        elif self.mode == HIRE_MODE:
            if clicked_item.name not in self.selected_items and clicked_item.status == 'in':
                self.selected_items.append(clicked_item)
                #set instance state
                instance.state = 'down'
                self.status_text = "Hiring: {} for ${}".format(name, clicked_item.cost)
        elif self.mode == RETURN_MODE:
            if clicked_item.name not in self.selected_items and clicked_item.status == 'out':
                self.selected_items.append(clicked_item)
                #set instance state
                instance.state = 'down'
                self.status_text = "Returning: {}".format(name)


    def press_hire(self):
        self.mode = HIRE_MODE
        #changes state of each button
        self.root.ids.hireItems.state = 'down'
        self.root.ids.listItems.state = 'normal'
        self.root.ids.returnItems.state = 'normal'


    def press_return(self):
        self.mode = RETURN_MODE
        #changes state of each button
        self.root.ids.hireItems.state = 'normal'
        self.root.ids.listItems.state = 'normal'
        self.root.ids.returnItems.state = 'down'



    def press_clear(self):
        """
        Clear any buttons that have been selected (visually) and reset status text
        :return: None
        """
        # use the .children attribute to access all widgets that are "in" another widget
        for instance in self.root.ids.entriesBox.children:
            instance.state = 'normal'
        self.status_text = ""

    def press_save(self, added_name, added_number):
        """
        Handler for pressing the save button in the add entry popup - save a new entry to memory
        :param added_name: name text input (from popup GUI)
        :param added_number: phone number text input (string)
        :return: None
        """
        self.itemlist[added_name] = added_number
        # change the number of columns based on the number of entries (no more than 5 rows of entries)
        self.root.ids.entriesBox.cols = len(self.itemlist) // 5 + 1
        # add button for new entry (same as in create_entry_buttons())
        temp_button = Button(text=added_name)
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.entriesBox.add_widget(temp_button)
        # close popup
        self.root.ids.popup.dismiss()
        self.clear_fields()

    def clear_fields(self):
        """
        Clear the text input fields from the add entry popup
        If we don't do this, the popup will still have text in it when opened again
        :return: None
        """
        self.root.ids.addedName.text = ""
        self.root.ids.addedNumber.text = ""

    def press_cancel(self):
        """
        Handler for pressing cancel in the add entry popup
        :return: None
        """
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.status_text = ""



EquipmentHire().run()