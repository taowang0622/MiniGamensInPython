"""
Student facing code for Tantrix Solitaire
http://www.jaapsch.net/puzzles/tantrix.htm

Game is played on a grid of hexagonal tiles.
All ten tiles for Tantrix Solitaire and place in a corner of the grid.
Click on a tile to rotate it.  Cick and drag to move a tile.

Goal is to position the 10 provided tiles to form
a yellow, red or  blue loop of length 10
"""

# Core modeling idea - a triangular grid of hexagonal tiles are
# model by integer tuples of the form (i, j, k)
# where i + j + k == size and i, j, k >= 0.

# Each hexagon has a neighbor in one of six directions
# These directions are modeled by the differences between the
# tuples of these adjacent tiles

# Numbered directions for hexagonal grid, ordered clockwise at 60 degree intervals
DIRECTIONS = {0: (-1, 0, 1), 1: (-1, 1, 0), 2: (0, 1, -1),
              3: (1, 0, -1), 4: (1, -1, 0), 5: (0, -1, 1)}


def reverse_direction(direction):
    """
    Helper function that returns opposite direction on hexagonal grid
    """
    num_directions = len(DIRECTIONS)
    return (direction + num_directions / 2) % num_directions


# Color codes for ten tiles in Tantrix Solitaire
# "B" denotes "Blue", "R" denotes "Red", "Y" denotes "Yellow"
SOLITAIRE_CODES = ["BBRRYY", "BBRYYR", "BBYRRY", "BRYBYR", "RBYRYB",
                   "YBRYRB", "BBRYRY", "BBYRYR", "YYBRBR", "YYRBRB"]

# Minimal size of grid to allow placement of 10 tiles
MINIMAL_GRID_SIZE = 4


class Tantrix:
    """
    Basic Tantrix game class
    """

    def grid_invariant(self):
        for key in self._tile_value.keys():
            if self._size != key[0] + key[1] + key[2]:
                return False
        return True

    def __init__(self, size):
        """
        Create a triangular grid of hexagons with size + 1 tiles on each side.
        """
        assert size >= MINIMAL_GRID_SIZE
        # Initialize dictionary tile_value to contain codes for ten
        # tiles in Solitaire Tantrix in one 4x4 corner of grid
        self._size = size
        self._tile_value = {}  # declare one field and self is equivalent to this
        counter = 0
        for x_index in range(size + 1):
            for y_index in range(size + 1):
                z_index = size - (x_index + y_index)
                if z_index < 0:
                    break
                else:
                    assert size == x_index + y_index + z_index
                    if z_index <= size and z_index >= size - 3:
                        self._tile_value[(x_index, y_index, z_index)] = SOLITAIRE_CODES[counter]
                        counter += 1
                    else:
                        self._tile_value[(x_index, y_index, z_index)] = ""
        assert counter == 10
        assert self.grid_invariant()    # invariant


    def __str__(self):
        """
        Return string of dictionary of tile positions and values
        """
        return str(self._tile_value)

    def get_tiling_size(self):
        """
        Return size of board for GUI
        """
        return self._size

    def tile_exists(self, index):
        """
        Return whether a tile with given index exists
        """
        return self._tile_value[index] != ""

    def place_tile(self, index, code):
        """
        Play a tile with code at cell with given index
        """
        self._tile_value[index] = code

    def remove_tile(self, index):
        """
        Remove a tile at cell with given index
        and return the code value for that tile        """
        code = self._tile_value[index]
        self._tile_value[index] = ""
        return code

    def rotate_tile(self, index):
        """
        Rotate a tile clockwise at cell with given index
        """
        code = self._tile_value[index]
        self._tile_value[index] = code[-1:] + code[:-1]

    def get_code(self, index):
        """
        Return the code of the tile at cell with given index
        """
        return self._tile_value[index]

    def get_neighbor(self, index, direction):
        """
        Return the index of the tile neighboring the tile with given index in given direction
        """
        return (index[0] + DIRECTIONS[direction][0], index[1] + DIRECTIONS[direction][1], index[2] + DIRECTIONS[direction][2])

    def is_legal(self):
        """
        Check whether a tile configuration obeys color matching rules for adjacent tiles
        """
        for tileIndex in self._tile_value:
            tileCode = self._tile_value[tileIndex]
            for direct in DIRECTIONS:
                # examine every direction of the current tile
                nbrIndex = self.get_neighbor(tileIndex, direct)
                if self._tile_value.has_key(nbrIndex):
                    nbrCode = self._tile_value[nbrIndex]
                    if tileCode[direct] != nbrCode[reverse_direction(direct)]:
                        return False
        return True

    def has_loop(self, color):
        """
        :param color is one of "R", "B" and "Y"
        Check whether a tile configuration has a loop of size 10 of given color
        """
        """
                Check whether a tile configuration has a loop of size 10 of given color
                """
        if not self.is_legal():
            return False

        # choose arbitrary starting point
        tile_indices = self._tile_value.keys()
        start_index = tile_indices[0]
        start_code = self._tile_value[start_index]
        next_direction = start_code.find(color)
        next_index = self.get_neighbor(start_index, next_direction)
        current_length = 1

        # loop through neighboring tiles that match given color
        while start_index != next_index:
            current_index = next_index
            if not self.tile_exists(current_index):
                return False
            current_code = self._tile_value[current_index]
            if current_code.find(color) == reverse_direction(next_direction):
                next_direction = current_code.rfind(color)
            else:
                next_direction = current_code.find(color)
            next_index = self.get_neighbor(current_index, next_direction)
            current_length += 1

        return current_length == len(SOLITAIRE_CODES)


# print Tantrix(6)

# run GUI for Tantrix
import poc_tantrix_gui

poc_tantrix_gui.TantrixGUI(Tantrix(6))