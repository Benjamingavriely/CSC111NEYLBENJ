"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

# Note: You may add in other import statements here as needed
from game_data import World, Item, Location, Player

# Note: You may add helper functions, classes, etc. here as needed
#test
# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    w = World(open("map.txt"), open("locations.txt"), open("items.txt"))
    p = Player(0, 0)

    menu = ["look", "inventory", "score", "quit", "back"]

    while not p.victory:
        location = w.get_location(p.x, p.y)

        # checks if the player has any moves left
        if p.num_moves == 45:
            print("You only have 5 moves left!")
        elif p.num_moves == 46:
            print("You only have 4 moves left!")
        elif p.num_moves == 47:
            print("You only have 3 moves left!")
        elif p.num_moves == 48:
            print("You only have 2 moves left!")
        elif p.num_moves == 49:
            print("You only have 1 move left!")
        elif p.num_moves == 50:
            print("You have no moves left :(")
            print("Game over.")
            break

        # print the long or short description
        if location.visited_before:
            print(location.brief_description)
        else:
            print(location.long_description)
            p.score += location.points_for_visit
            location.visited_before = True

        print("What to do? \n")
        print("[menu]")
        for action in w.available_actions(p.x, p.y):
            print(action)
        choice = input("\nEnter action: ")

        if choice == "[menu]":
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")

        if choice == "look":
            print(location.long_description)

        if choice == "inventory":
            for item in p.inventory:
                print(item)
            print("'Drop' + item to drop an item")
            print("Back to return to actions")
            choice = input()
            if choice == "Back":
                continue

            # allow the user to drop items
            for item in p.inventory:
                if choice == "Drop" + item.name:
                    p.inventory.remove(item)
                    item.current_position = location.map_position

        if choice == "score":
            print(p.score)

        if choice == "quit":
            break

        if choice == "back":
            continue

        if choice == "Go East":
            # change the player's x coordinate
            p.x += 1
            p.num_moves += 1
            continue

        if choice == "Go West":
            # change the player's x coordinate
            p.x -= 1
            p.num_moves += 1
            continue

        if choice == "Go North":
            # change the player's y coordinates
            p.y -= 1
            p.num_moves += 1
            continue

        if choice == "Go South":
            # change the player's y coordinates
            p.y += 1
            p.num_moves += 1
            continue

        for item in w.items:
            if choice == "Take" + item.name:
                print("You picked up the " + item.name)
                p.inventory.append(item)
                item.current_location = 0
                continue

        # win conditions
        # if you reach the final destination with all of the items
        if location == "int" and len(p.inventory) != len(w.items): #TODO put the number of the final location
            print("You do not have all of the items, so you cannot write the exam!")
        elif location == "int": #TODO put the number of the final location
            print("Congratulations! You have collected all of the items and are ready to write the final exam!")
            print("You forgot to study and barely passed the course. Your career prospects dwindle and"
                  "you become an unsuccessful rapper. At least you passed")
            p.victory = True


