""" CP1404 Assignment 1 - 2016
    ItemsForHire
    Alex Silva
    02/04/2016
    https://github.com/AlexCSilva/CP1404Assignment1-ItemsForHire

Pseudocode:

Constants:
MENU
determine filename

function main()
    display welcome message
    display amount of items loaded from csv
    display menu
    get choice
    while choice is not 'Q'
        if choice is 'L'
            display all items from list
        else if choice is 'H'
            display avaliable items from list
        else if choice is 'R'
            display hired items
        else if choice is 'A'
            get new item name
            add item to list
        else
            display invalid choice message
        display menu
        get choice
    print farewell message


"""

#Determines Constants
MENU = "\nMenu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item\n(Q)uit"

#Determines the filename
FILENAME = "items.csv"

#Main function; contains welcome and farewell messages and choices
def main():

    items = load_items()
    print(items)
    print("Items for Hire - by Alex Silva")
    print("items loaded from", FILENAME)

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("All items on file (* indicates item is currently out):")
            list_items(items, "all")
        elif choice == "H":
            items = hire_items(items)
        elif choice == "R":
            items = return_items(items)
        elif choice == "A":
            items = add_items(items)
        else:
            print("Invalid menu choice.")
        print(MENU)
        choice == input(">>> ").upper()

    print("items saved to items.csv")
    print("Have a nice day. :)")

"""
function load_items()
    determine items as empty list
    open FILENAME
    sort lines in in_file
    append parts to items
    close FILENAME
    return items
"""
def load_items():
    #Creates an empty list for variable 'items'
    items = []

    #Opens and loads filename
    in_file = open(FILENAME)
    for line in in_file:
        parts = line.strip().split(',')
        items.append(parts)
    in_file.close()
    return items



"""
function hire_item(items)
    to be implemented

"""

def hire_items(items):

    list_items(items, "in")

    valid_input = False
    while not valid_input:
        try:
            item_to_hire = int(input("Enter the number of an item to hire\n>>>"))
            valid_input = True
        except ValueError:
            print("Invalid input; enter a number\n>>>")

    items[item_to_hire][3] = "out"

    print('item',"hired for", items[item_to_hire][2])
    return items


def list_items(items, data_filter):
    rows = len(items)
    data_table = ""

    if data_filter == "all":
        for i in range(0, len(items)):
            data_table += items[i][0]
            data_table += items[i][1]
            data_table += items[i][2]
            data_table += items[i][3]

    if data_filter == "in":
         for i in range(0, len(items)):
            if items[i][3] == "in":
                data_table += items[i][0]
                data_table += items[i][1]
                data_table += items[i][2]
                data_table += items[i][3]

    if data_filter == "out":
        for i in range(0, len(items)):
            if items[i][3] == "out":
                data_table += items[i][0]
                data_table += items[i][1]
                data_table += items[i][2]
                data_table += items[i][3]


def return_items(items):

    list_items(items, "out")

    valid_input = False
    while not valid_input:
        try:
            item_to_hire = int(input("Enter the number of an item to hire\n>>>"))
            valid_input = True
        except ValueError:
            print("Invalid input; enter a number\n>>>")

    items[item_to_hire][3] = "in"

    print('item',"hired for", items[item_to_hire][2])
    return items

def add_items(items):
    item_name = input("Item name: ")
    item_description = input("Description: ")
    price_per_day = float(input("Price per day: "))

main()