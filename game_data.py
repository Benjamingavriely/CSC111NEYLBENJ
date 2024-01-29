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
        - available_actions:
            A list of available actions in this location
        - points_for_visit

    Representation Invariants:
        - # TODO
    """
    map_position: int
    brief_description: str
    long_description: str
    available_actions: list[str]
    points_for_visit: int
    visited_before: bool

    def __init__(self, position: int, brief: str, long: str, available_actions: list,
                 points: int) -> None:
        """Initialize a new location.

        # TODO Add more details here about the initialization if needed
        """
        self.map_position = position
        self.brief_description = brief
        self.long_description = long
        self.available_actions = available_actions
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


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name:
            The name of the item
        - start_position:
            The location of the item when the map is first loaded in. This is stored as the location
            number.
        - target_position:

    Representation Invariants:
        - name != ''
        -
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
        -  y:
            The player's y position
        -  inventory:
            The player's items stored in a list
        - victory:
            Boolean storing whether the player has won.

    Representation Invariants:
        - x >= 0
        - y >= 0
    """

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


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - locations:
            List of locations in the map
        - items:
            List of all items


    Representation Invariants:
        - # TODO
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
        line = item_data.readline()
        while line:
            # save each line to an item
            item_data = line.split()

            # create an item object
            curr_item = Item(item_data[0], int(item_data[1]), int(item_data[2]), int(item_data[3]))

            # add the item to the item list
            items.append(curr_item)

        # close the file
        item_data.close()

        return items

    # TODO: Add methods for loading location data and item data (see note above).
    def load_locations(self, location_data: TextIO) -> list[Location]:
        """
        Save the location data for the world in the location_data attribute of this object as a
        """

        # Tries to open the file
        # try:
        #     file = open("locations.txt")
        # except FileNotFoundError:
        #     print("The location file does not exist or is not in the right directory")
        #     raise FileNotFoundError

        # stores item objects
        locations = []

        # iterate through the file
        line = location_data.readline()
        while line != "END OF FILE":
            # save the location number
            loc_num = int(line.split()[1])
            num_points = int(location_data.readline())
            short_desc = location_data.readline()
            long_desc = ""
            while line != "END":
                long_desc += line
                location_data.readline()
            locations.append(Location(loc_num, short_desc, long_desc, actions, num_points))

        # close the file
        location_data.close()

        return locations

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        Precondition :
         TODOOOOOOOO
        """
        location_num = self.map[y][x]
        if location_num == (-1):
            return None
        for location in self.locations:
            if location.map_position == location_num:
                return location

    def available_actions(self, x:int, y:int) -> list[str]:
        """
        This method will return a list of all available actions in a location
        """
        actions = []
        # check cardinal directions

        if len(self.map[0]) > x and self.map[x+1][y] != -1:
            actions.append("Go East")
        if x > 0 and self.map[x-1][y] != -1:
            actions.append("Go West")
        if len(self.map) > y and self.map[x][y + 1] != -1:
            actions.append("Go South")
        if y > 0 and self.map[x][y-1] != -1:
            actions.append("Go North")

        return actions
