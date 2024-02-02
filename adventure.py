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
from game_data import World, Item, Location, Player, pn_tower

# Note: You may add helper functions, classes, etc. here as needed
# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    w = World(open("map.txt"), open("locations.txt"), open("items.txt"))
    p = Player(0, 0)

    menu = ["look", "inventory", "score", "quit", "back"]

    while not p.victory:
        location = w.get_location(p.x, p.y)

        # print the long or short description
        if location.visited_before:
            print(location.brief_description)
        else:
            print(location.long_description)
            p.score += location.points_for_visit
            location.visited_before = True

        # win conditions
        # if you reach the final destination with all of the items
        if location == 23 and len(p.inventory) != len(w.items):
            print("You do not have all of the items, so you cannot write the exam!")
        elif location == 23:
            print("Congratulations! You have collected all of the items and are ready to write the final exam!")
            print("You forgot to study and barely passed the course. Your career prospects dwindle and"
                  "you become an unsuccessful rapper. At least you passed")
            print("\nCongratulations! You have won! \n Score " + str(p.score))
            p.victory = True

        if isinstance(location, pn_tower):
            while choice != "Take a selfie":
                print("\nactions:")
                choice = input("Take a selfie\n")
            print("CLICK!")
            while choice != "Tell Drake about my exam":
                print("\nactions:")
                choice = input("\nTell Drake about my exam\n")

            print("Drake: ""Man, I feel you on that. Life's full of exams"
                  "\nwe ain't ready for, but you gotta trust the process. "
                  "\nTake a deep breath, focus up, and give it your all."
                  "\nIt's all about the journey, not just the destination. You got this,"
                  "\nkeep pushing through, and remember, 'started from the bottom, now we here.' 🙌💯")
            while choice != "Thank him for his kind words":
                print("\nactions:")
                choice = input("Thank him for his kind words.\n")
            print("Drake personally helicopters you out to the exam center")
            choice = input("Press enter to continue from now on.\n")
            print("\n*Landing on top of the Health Science building* \n")
            choice = input()
            print("Drake: What a ride, huh? It really makes you appreciate our city.\n")
            choice = input()
            print("Drake: Listen,After an adventure like what you just had,\n "
                  "my gut tells me that you're not meant for this CS thing.\n")
            choice = input()
            print("Drake: I think you're destined for something greater. Something more noble. \n"
                  "So, I want to personally tell Sadia that you will not be writing this exam,\n"
                  "And STARTING TODAY, I want to sign you as the CEO of OVO.\n")
            choice = input()
            print("*LOUD GRUMBLE*")
            choice = input()
            print(" \n*Drake blushes*\n")
            choice = input()
            print("Drake: Yo, my people, it's been real, but your boy Drake's gotta bounce for a minute."
                  "\nThe hunger's hitting hard, and I'm on a mission – gotta satisfy that craving, you know?")
            choice = input()
            print("\nDrake: It's poutine time, and I can't keep the fries waiting."
                  "\nSo, I'm signing off for now, but catch me on the flip side."
                  "\nIf you see me at the poutine spot, slide through – we')ll vibe over some fries,"
                  "\ncheese curds, and gravy."
                  "\nUntil then, stay blessed, stay hungry, and we'll rendezvous on the other side. OVO, out. ✌️🍟")
            choice = input("Press enter to continue\n")
            print("\nCongratulations! You have won! \n Score: " + str(p.score))
            p.victory = True

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

        if p.victory:
            break
        print("What to do? \n")
        print("[menu]")
        for action in w.available_actions(p.x, p.y):
            print(action)
        choice = input("\nEnter action: ")
        if choice in w.available_actions(p.x, p.y) or choice == "[menu]":
            # This ensures that the player enters a valid action
            if choice == "[menu]":
                while choice != "back":
                    print("Menu Options: \n")

                    for option in menu:
                        if not p.inventory and option == "inventory":
                            continue
                        print(option)
                    choice = input("\nChoose action: ")
                    if choice in menu:
                        if choice == "look":
                            print(location.long_description)

                        if choice == "inventory" and p.inventory:
                            for item in p.inventory:
                                print(item.name)
                            print("'Drop' + item to drop an item")
                            choice = input()
                            # allow the user to drop items
                            for item in p.inventory:
                                if choice == "Drop " + item.name:
                                    p.inventory.remove(item)
                                    item.current_position = location.map_position

                        if choice == "score":
                            print(p.score)

                        if choice == "quit":
                            exit()

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
                if choice == "Take " + item.name:
                    print("You picked up the " + item.name)
                    p.inventory.append(item)
                    item.current_position = 0
                continue
        else:
            print("That is not a valid action!")
