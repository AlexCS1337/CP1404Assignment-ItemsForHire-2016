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
            print(items)
        elif choice == "H":
            print(items)
        elif choice == "R":
            print(items)
        elif choice == "A":
            hire_items()
        else:
            print("Invalid menu choice.")
        print(MENU)
        choice == input(">>> ").upper()

    print("items saved to items.csv")
    print("Have a nice day. :)")

"""
function load_items()
    items = []
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
function hire_item()
    test
"""

def hire_items():
    print("test")

main()