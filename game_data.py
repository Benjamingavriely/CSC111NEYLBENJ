"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
from typing import Optional, TextIO

import pygame.mixer
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

pygame.mixer.music.load("background.mp3")
pygame.mixer_music.play(-1, 0.0, 0)


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - map_position:
            The number of the position of this location on the map
        - brief_description:
            A brief description of the location. This will be displayed every time this location is
            visited after the first time
        - long_description:
            A long description of the location. This will be displayed the first time a location is visited
        - points_for_visit :
            The number of points obtained when visiting this location for the first time.
        - visted_before :
            Wheither this location has been visited before.

    Representation Invariants:
        - (-1 <= self.map_position <= 25) and (self.map_position != 0)
        - len(self.brief_description) < len(self.long_description)
        - self.brief_description != ""
        - points_for_visit >= 0

    """
    map_position: int
    brief_description: str
    long_description: str
    points_for_visit: int
    visited_before: bool

    def __init__(self, position: int, brief: str, long: str, points: int) -> None:
        """Initialize a new location.
        """
        self.map_position = position
        self.brief_description = brief
        self.long_description = long
        self.points_for_visit = points
        self.visited_before = False
        # NOTES:
        # Data that could be associated with each Location object:
        # a position in the world map,
        # a brief description,
        # a long description,
        # a list of available commands/directions to move,
        # items that are available in the location,
        # and whether the location has been visited before.
        # Store these as you see fit, using appropriate data types.
        #
        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.


class pn_tower(Location):
    """
    A class that inherits from Location made to distinguish between the PN tower and the other locations.
    """
    map_position: int
    brief_description: str
    long_description: str
    points_for_visit: int
    visited_before: bool

    def __init__(self, position: int, brief: str, long: str, points: int) -> None:
        """Initialize a new location.
        """
        super().__init__(position, brief, long, points)

    def drake_music(self) -> None:
        """
        A method that changes the music if the player is in the pn_tower
        """
        pygame.mixer.music.load("drake.mp3")
        pygame.mixer_music.play(-1, 0.0, 0)


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name:
            The name of the item
        - start_position:
            The location of the item when the map is first loaded in. This is stored as the location
            number.
        - target_position:
            The location number where the item has to be dropped to progress in the game. This is stored as the
            location number.
        - target_points:
            The points earned when dropping the item in a target_position location.
        - current_position:
            The current location number of the item, 0 if the item is in the inventory of the player.

    Representation Invariants:
        - self.name != ""
        - self.start_position > 0
        - self.current_position >= 0
        - self.target_position > 0
        - self.target_points >= 0

    """
    name: str
    start_position: int
    target_position: int
    target_points: int
    current_position: int

    def __init__(self, name: str, start: int, target: int, target_points: int) -> None:
        """Initialize a new item.
        """

        # NOTES:
        # This is just a suggested starter class for Item.
        # You may change these parameters and the data available for each Item object as you see fit.
        # (The current parameters correspond to the example in the handout).
        # Consider every method in this Item class as a "suggested method".
        #
        # The only thing you must NOT change is the name of this class: Item.
        # All item objects in your game MUST be represented as an instance of this class.

        self.name = name
        self.start_position = start
        self.target_position = target
        self.target_points = target_points
        self.current_position = start


class Player:
    """
    A Player in the text adventure game.

    Instance Attributes:
        - x:
            The player's x position
        - y:
            The player's y position
        - inventory:
            The player's items stored in a list
        - victory:
            Boolean storing whether the player has won.
        - score:
            The player's score
        - num_moves:
            The number of moves the player completed since the beginning

    Representation Invariants:
        - x >= 0
        - y >= 0
        - score >= 0
        - 0 <= num_moves <= 31
    """
    x: int
    y: int
    inventory: list[Item]
    victory: bool
    score: int
    num_moves: int

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.

        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False
        self.score = 0
        self.num_moves = 0


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - locations:
            List of locations in the map
        - items:
            List of all items in the map


    Representation Invariants:
        - len(self.map) != 0
        - len(self.map) == len(self.map[0])
        - self.items != []
        - self.locations != []
    """
    map: list[list[int]]
    locations: list[Location]
    items: list[Item]

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """

        # NOTES:

        # map_data should refer to an open text file containing map data in a grid format, with integers separated by a
        # space, representing each location, as described in the project handout. Each integer represents a different
        # location, and -1 represents an invalid, inaccessible space.

        # You may ADD parameters/attributes/methods to this class as you see fit.
        # BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES IN THIS CLASS

        # The map MUST be stored in a nested list as described in the load_map() function's docstring below
        self.map = self.load_map(map_data)
        self.locations = self.load_locations(location_data)
        self.items = self.load_items(items_data)
        # NOTE: You may choose how to store location and item data; create your own World methods to handle these
        # accordingly. The only requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def load_map(self, map_data: TextIO) -> list[list[int]]:
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:

        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].

        Return this list representation of the map.
        """
        # Tries to open the file
        # try:
        #    file = open("map.txt")
        # except FileNotFoundError:
        #    print("The map file does not exist or is not in the right directory")
        #    raise FileNotFoundError

        # create a map that will hold the data
        map_list = []
        # iterate through the file
        line = map_data.readline()
        while line:
            # save each line to a list
            map_list.append([int(x) for x in line.split()])
            line = map_data.readline()
        # close the file
        map_data.close()

        # save the data to the instance attribute
        # self.map = map_list

        return map_list

    def load_items(self, item_data: TextIO) -> list[Item]:
        """
        This loads the items from the item file as an item object. It then saves them in the
        items instance attribute and returns the list of items objects.
        """
        # Tries to open the file
        # try:
        #     file = open("items.txt")
        # except FileNotFoundError:
        #     print("The item file does not exist or is not in the right directory")
        #     raise FileNotFoundError

        # stores item objects
        items = []

        # iterate through the file
        line = item_data.readline().strip()
        while line:
            # save each line to an item
            item_line = line.split()

            # create an item object
            curr_item = Item(item_line[0], int(item_line[1]), int(item_line[2]), int(item_line[3]))

            # add the item to the item list
            items.append(curr_item)
            line = item_data.readline().strip()
        # close the file
        item_data.close()

        return items

    def load_locations(self, location_data: TextIO) -> list[Location]:
        """
        Save the location data for the world in the location_data attribute of this object as a list of Locations
        """

        # stores item objects
        locations = []

        # iterate through the file
        line = location_data.readline().strip()
        while line != "END OF FILE":
            # save the location number
            loc_num = int(line.split()[1])
            line = location_data.readline().strip()
            num_points = int(line)
            line = location_data.readline().strip()
            short_desc = line
            line = location_data.readline().strip()
            long_desc = ""
            while line != "END":
                long_desc += line + "\n"
                line = location_data.readline().strip()
            if loc_num == 21:
                locations.append(pn_tower(loc_num, short_desc, long_desc, num_points))
            else:
                locations.append(Location(loc_num, short_desc, long_desc, num_points))
            line = location_data.readline()
            line = location_data.readline().strip()

        # close the file
        location_data.close()

        return locations

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        Precondition :
         - 0 <= x <= len(self.map[0])
         - 0 <= y <= len(self.map)
         - any(self.map[y][x] == location.map_position for location in self.locations)
        """
        location_num = self.map[y][x]
        if location_num == (-1):
            return None
        for location in self.locations:
            if location.map_position == location_num:
                if isinstance(location, pn_tower):
                    location.drake_music()
                return location

    def available_actions(self, x: int, y: int) -> list[str]:
        """
        This method will return a list of all available actions in a location
        Preconditions:
        - 0 <= x <= len(self.map[O])
        - 0 <= y <= len(self.map)
        """
        actions = []
        # check cardinal directions CHANGE EVERYTHING CAUSE BENJ MESSED UP
        if (y != 0) and (self.map[y - 1][x] != (-1)):
            actions.append("Go North")
        if (y != (len(self.map) - 1)) and (self.map[y + 1][x] != (-1)):
            actions.append("Go South")
        if (x != (len(self.map[0]) - 1)) and (self.map[y][x + 1] != (-1)):
            actions.append("Go East")
        if (x != 0) and (self.map[y][x - 1] != (-1)):
            actions.append("Go West")
        # check if there are items here and if so, adding to actions taking the items
        for item in self.items:
            if item.current_position == self.map[y][x]:
                actions.append("Take " + item.name)
        return actions
