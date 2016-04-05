""" CP1404 Assignment 1 - 2016
    ItemsForHire
    Alex Silva
    02/04/2016
    https://github.com/AlexCSilva/CP1404Assignment1-ItemsForHire

Pseudocode:

determine filename
items = empty list

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
filename = "items.csv"

#Creates an empty list for variable 'items'
items = []

#Opens and loads filename
in_file = open(filename)
for line in in_file:
    in_file.split(", ")
    items.append(in_file)
in_file.close()

#Main function; contains welcome and farewell messages and choices
def main():
    print("Items for Hire - by Alex Silva")
    print("items loaded from", filename)

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("Test123")
        elif choice == "H":
            print("Test234")
        elif choice == "R":
            print("Test456")
        elif choice == "A":
            print("Test789")
        else:
            print("Invalid menu choice.")
        print(MENU)
        choice == input(">>> ").upper()

    print("items saved to items.csv")
    print("Have a nice day. :)")

"""
function load_items()
    read csv file
    close csv file
    append to items list
"""

def load_items():
    print("test")

"""
function hire_item()
    pass
"""

main()