from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# add some times
room['foyer'].items = [Item("Rock", "It's a rock...")]
room['overlook'].items = []
room['narrow'].items = []
room['treasure'].items = []

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player1= Player()

move_error = "\nInvalid Direciton. Please enter a different one."

loc = room['outside']

while True:
    print("\n________________________________________________________________________")
    print("\nCurrent Location:", loc.name)
    print("Room Description:", loc.desc)

    ### MOVEMENT
    move = input("\nType a direction (n, s, e, w) or q to exit: ")
    
    while move not in ['n', 's', 'e', 'w', 'q']:
        print("Please enter a valid command.")
        move = input("\nType a direction (n, s, e, w) or q to exit: ")

    if move == 'q':
        break

    move = move + "_to"

    if getattr(loc, move) == None:
        print(move_error)
        continue
        
    else:
        loc = getattr(loc, move)
        print("\nYou enter the", loc.name)
    

    ### ITEM CHECK
    check_item = input("Would you like to search for items? (y/n) ")

    while check_item != 'n' and check_item != 'y':
        print("Please enter a valid command.")
        check_item = input("\nWould you like to search for items? (y/n) ")

    if check_item == "n":
        pass
    
    elif check_item == "y":
        room_items = loc.items

        if len(room_items) == 0:
            print("\nThere are no items in this room.")

        else:
            print("\nYou found:\n")
            for item in room_items:
                print("Name: {:<10} Description: {}".format(item.name, item.desc))

            get_item = input("\nWould you like to take an item? (y/n) ")
            while check_item != 'n' and check_item != 'y':
                print("Please enter a valid command.")
                check_item = input("\nWould you like to take an item? (y/n) ")
            
            if get_item == "y":
                item_name = int(input("\nEnter the item name. "))

                while number not in [i for i in range(0, len(room_items))]:
                    print("Please enter a valid number.")
                    number = int(input("\nEnter the item number. "))
                
                player1.get_item(room_items.pop(number-1))
                
                get_more = len(room_items)
                



"""
# Old movement command code that has been replaced
elif move == "n":
    if loc.n_to == None:
        print(move_error)
        continue
    else:
        loc = loc.n_to

elif move == "s":
    if loc.s_to == None:
        print(move_error)
        continue
    else:
        loc = loc.s_to

elif move == "e":
    if loc.e_to == None:
        print(move_error)
        continue
    else:
        loc = loc.e_to

elif move == "w":
    if loc.w_to == None:
        print(move_error)
        continue
    else:
        loc = loc.w_to

else:
    print("\nPlease enter a valid command.")
"""