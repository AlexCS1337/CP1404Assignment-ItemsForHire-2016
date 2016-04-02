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

#Creates an empty list
items = []

def main():
    print("Items for Hire - by Alex Silva")
    print("items loaded from", filename)

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("Test123")

main()