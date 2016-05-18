""" CP1404 Assignment 1 - 2016
    ItemsForHire
    Alex Silva
    02/04/2016
    https://github.com/AlexCSilva/CP1404Assignment1-ItemsForHire

Pseudocode:

Constants:
MENU
FILENAME


function main()
    items = load_items()
    save = 0
    display welcome message
    display amount of items loaded from csv
    display menu
    get choice
    while choice is not 'Q'
        if choice is 'L'
            display message "all items on file:"
            call function list_items(items, "a")
        else if choice is 'H'
            call function hire_items(items)
        else if choice is 'R'
            call function return_items(items)
        else if choice is 'A'
            call function add_items(items, SAVE)
        else
            display invalid choice message
        display menu
        get choice
    print farewell message


"""
# imports the required Item and ItemList classes
from item import Item
from itemlist import ItemList

# Determines a menu as a constant
MENU = "\nMenu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit"

# Determines the filename
FILENAME = "items.csv"


# Main function; contains welcome and farewell messages and choices
def main():
    items = load_items()

    # Counts how many items being saved to filename
    save = 0
    # Welcome message
    print(items)
    print("Items for Hire - by Alex Silva")
    print("items loaded from", FILENAME)

    # This prints the menu which loops back until input is Q/q (quit)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("All items on file (* indicates item is currently out):")
            list_items(items, "a")
        elif choice == "H":
            items = hire_items(items)
        elif choice == "R":
            items = return_items(items)
        elif choice == "A":
            items = add_items(items, save)
            save += 1
        else:
            print("Invalid menu choice.")
        print(MENU)
        choice = input(">>> ").upper()

    # displays farewell message
    print(save, "items saved to items.csv")
    print("Have a nice day. :)")


"""
function load_items()
    items = ""
    open FILENAME
        sort lines in in_file
        append parts to items
    close FILENAME
    return items
"""


def load_items():
    # Creates an empty list for variable 'items'
    items = []

    # Opens and loads filename
    in_file = open(FILENAME)
    for line in in_file:
        parts = line.strip().split(',')
        items.append(parts)
    in_file.close()
    return items


"""
function hire_item(items)
    call list_items(items, "i")
    rows = length of items
    valid_index = []
    counter = 0
    for i in range
        counter += 1
        if items = in
            counter appends into valid_index
            items[i] appends into valid_index
    valid_input = Fasle
    while not valid_input
        try
            get item_to_hire
            if item_to_hire in valid_index
                valid_input = True
            else
                display invalid input error message
        except ValueError
            display invalid value message
        except index error
            display index error message

    item_to_hire = "out"
    dsiplay item hired for price
    return items

"""


def hire_items(items):
    # Lists all items that are currently in
    list_items(items, "i")
    rows = len(items)

    # ACQUIRE VALID ITEMS
    valid_index = []
    counter = 0
    for i in range(0, rows):
        if items[i][3] == "in":
            valid_index.append(counter)
            valid_index.append(items[i])
            counter += 1

    # SELECT VALID ITEM
    valid_input = False
    while not valid_input:
        try:
            item_to_hire = int(input("Enter the number of an item to hire\n>>>"))
            if item_to_hire in valid_index:
                valid_input = True
            else:
                print("That item is not on hire")
        except ValueError:
            print("Invalid input; enter a number\n>>>")
        except IndexError:
            print("Invalid item number")

    # Changes hired item status to 'out'
    items[item_to_hire][3] = "out"

    print(items[item_to_hire][0], "hired for $", items[item_to_hire][2])
    return items


"""
function list_items(items. data_filter)
    rows = len(items)
    data_table = ""

    if data_filter = all
        data_tale += list of items.format
        if items = out
            data_table += '*'
        data_table += space
    if data_filter = in
        data_talbe += list of in stock items.format
        data_table += space
    if data_filter = out
        data_talbe += list of out of stock items.format
        data_table += space
    else
        display error message

    display data_table

"""


def list_items(items, data_filter):
    # determins rows as the length of items and data_table an empty varible
    rows = len(items)
    data_table = ""

    # Lists all items
    if data_filter == "a":
        for i in range(0, rows):
            data_table += "{:5}".format(str(i))
            data_table += "{:15}".format(items[i][0])
            data_table += "{:30}".format(items[i][1])
            data_table += "= $ {}".format(items[i][2])
            if items[i][3] == "out":
                data_table += "*"
            data_table += "\n"

    # Lists all items in stock
    elif data_filter == "i":
        for i in range(0, rows):
            if items[i][3] == "in":
                data_table += "{:5}".format(str(i))
                data_table += "{:15}".format(items[i][0])
                data_table += "{:30}".format(items[i][1])
                data_table += "= $ {}".format(items[i][2])
                data_table += "\n"

    # Lists all items out of stock
    elif data_filter == "o":
        for i in range(0, rows):
            if items[i][3] == "out":
                data_table += "{:5}".format(str(i))
                data_table += "{:15}".format(items[i][0])
                data_table += "{:30}".format(items[i][1])
                data_table += "= $ {}".format(items[i][2])
                data_table += "\n"

    else:
        print("An internal error occurred.")

    print(data_table)


"""
function return_items(items)
    call list_items(items, "o"
    rows = len(items)

    valid_index = []
    for i in range(0, rows)
        if item == "out"
            append to valid_index

    valid_input = False
    while not valid_input
        try
            get item_to_return
                valid_input = True
            else
                display "That item is not on hire"
        except ValueError
            display Value error message
        :except
            display error message
"""


def return_items(items):
    # Lists all items that are currently out
    list_items(items, "o")
    rows = len(items)
    # ACQUIRE VALID ITEMS
    valid_index = []
    counter = 0
    for i in range(0, rows):
        if items[i][3] == "out":
            valid_index.append(counter)
            valid_index.append(items[i])
            counter += 1

    # SELECT VALID ITEM
    valid_input = False
    while not valid_input:
        try:
            item_to_return = int(input("Enter the number of an item to return\n>>>"))
            if item_to_return in valid_index:
                valid_input = True
            else:
                print("That item is not on hire")
        except ValueError:
            print("Invalid input; enter a number\n>>>")
        except IndexError:
            print("Invalid item number")

    # Changes item_to_return status to 'in'
    items[item_to_return][3] = "in"

    print(items[item_to_return][0], "returned")
    return items


"""
function add_items(items, save)
    new_item = ["", "", 0.0, "in"]

    get item_name
    while item_name = ""
        display error message
        get item_name
    get description
    while description = ""
        display error message
        get description
    valid_input = False
    while not valid_input
        try
            get prince_per_day
            valid_input = True
        :except ValueError
            display value error message

    new_item[0] = item_name
    new_item[1] = item_description
    new_item[2] = price_per_day

    append new_item to items
    save += 1
    return items

"""


def add_items(items, save):
    # Creates a list called new_item
    new_item = ["", "", 0.0, "in"]

    # Gets item information and stores them while error checking
    item_name = input("Item name: ")
    while item_name == "":
        print("Input cannot be blank")
        item_name = input("Item name: ")
    item_description = input("Description: ")
    while item_description == "":
        print("Input cannot be blank")
        item_description = input("Description: ")
    valid_input = False
    while not valid_input:
        try:
            price_per_day = float(input("Price per day: $"))
            valid_input = True
        except ValueError:
            print("Invalid input; enter a number\n>>>")

    # This adds item_name, item_description and price_per_day into the list new_item
    new_item[0] = item_name
    new_item[1] = item_description
    new_item[2] = price_per_day

    # This appends new_item into items
    items.append(new_item)
    # displays message
    print(new_item[0], new_item[1] + ", $", new_item[2], "now available for hire")
    return items


main()
