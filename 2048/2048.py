"""
Clone of 2048 game.
"""

import poc_2048_gui
#import user40_12jlSFeyWj_15 as testsuite
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    
    line is a input list you want to merge
    return a new list that represent a merged input list
    """
    creat = []
    
    line_length = len(line)
    
    #make the length of "creat" the same as "line",with setting all elements to 0
    for dummy_num in range(line_length):
        creat.append(0)
    
    #initialize "create" copying all non-zero elements of "line" from leftmost   
    index_line = 0
    for val in line:
        if val != 0:
            creat[index_line] = val
            index_line += 1
    
    #merge "create" with two adjacent elements 
    for index_creat in range(line_length - 1):
        if creat[index_creat] == creat[index_creat + 1]:
            plus = creat[index_creat] + creat[index_creat + 1]
            creat[index_creat] = plus
            creat.pop(index_creat + 1)
            creat.append(0)
    
    return creat

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self._cells = []
        #call method "reset"
        self.reset()
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._cells = [[0 for dummy_col in range(self._width)]
                       for dummy_row in range(self._height)]
        #call method "new_tile"
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        mgs = ""
        for row in range(self._height):
            mgs += str(self._cells[row])
        return mgs

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        initial_tiles_dict = {UP: [[0, col]for col in range(self._width)],
                             DOWN: [[self._height - 1, col]for col in range(self._width)],
                             LEFT: [[row, 0]for row in range(self._height)],
                             RIGHT: [[row, self._width - 1]for row in range(self._height)]}
        #print initial_tiles_dict
        
        num_steps_dict = {UP: self._height - 1, DOWN: self._height - 1,
                         LEFT: self._width - 1, RIGHT: self._width - 1}
        
        add_new_tile = False
        
        for indice in initial_tiles_dict:
            if indice == direction:
                for index in initial_tiles_dict[indice]:
                    temp = []
                    temp.append(self._cells[index[0]][index[1]])
                    for dummy_step in range(num_steps_dict[indice]):
                        index[0] += OFFSETS[indice][0]
                        index[1] += OFFSETS[indice][1]
                        temp.append(self._cells[index[0]][index[1]])
#                    print temp
#                    print
                    
                    new_line = merge(temp)
                    if new_line != temp:
                        add_new_tile = True
                    end_line = len(new_line) - 1
#                    print new_line, index[0], index[1]
                    
                    self._cells[index[0]][index[1]] = new_line[end_line]
                    index_new_line = end_line
                    for dummy_step in range(num_steps_dict[indice]):
                        index[0] -= OFFSETS[indice][0]
                        index[1] -= OFFSETS[indice][1]
                        index_new_line -= 1
                        self._cells[index[0]][index[1]] = new_line[index_new_line]
#                    print self._cells
#                    print
                if add_new_tile == True:
                    self.new_tile()
          
                

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        #find out all indexes of cells which values are zero
        index_list = []
        for row in range(self._height):
            for col in range(self._width):
                if self._cells[row][col] == 0:
                    index_list.append((row, col))
        print index_list
        
        if index_list != []:
            random_index = random.choice(index_list)
            random_row = random_index[0]
            random_col = random_index[1]
            random_val = random.choice([4, 2, 2, 2, 2, 2, 2, 2, 2, 2])
            self._cells[random_row][random_col] = random_val
        
       
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._cells[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
#testsuite.run_test(TwentyFortyEight)