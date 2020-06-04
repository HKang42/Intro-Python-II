# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player():
    def __init__(self, name = "Player 1", room = Room("Outside Cave Entrance", "North of you, the cave mount beckons"), items = []):
        self.name = name
        self.room = room
        self.items = items

    def get_item(self, item):
        self.item = item
        self.items.append(self.item)
        print(item, "has been added to your inventory.")