"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list=None,
                 zombie_list=None, human_list=None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width) #Explicitly call the superclass's initializer
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def __str__(self):
        ans = ""
        ans += "Grid:" + "\n" + poc_grid.Grid.__str__(self) #Explicitly call the superclass's __str__
        ans += "Humans: " + str(self._human_list) + "\n"
        ans += "Zombies: " + str(self._zombie_list) + "\n"
        return ans

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        :param entity_type's value is HUMAN(6) or ZOMBIE(7)
        """
        grid_height = self.get_grid_height()
        grid_width = self.get_grid_width()
        # "visited" is a table for us to refer to the state of each cell in the grid
        # in this game, there're only two states, which are EMPTY and FULL, those are equivalent to UNDISCOVERED and VISITED respectively!!!
        visited = [[EMPTY for dummy_col in range(0, grid_width)] for dummy_row in range(0, grid_height)]
        max_distance = grid_width * grid_height
        distance_field = [[max_distance for dummy_col in range(0, grid_width)] for dummy_row in range(0, grid_height)]
        # in this case, vertices must be able to reach each other, so DISCOVERED is not necessary!!!
        queue = poc_queue.Queue()
        if entity_type == HUMAN:
            entities = self._human_list
        else:
            entities = self._zombie_list
        for entity in entities:
            visited[entity[0]][entity[1]] = FULL  # initialize the statuses of entities to FULL, that is VISITED!!!
            distance_field[entity[0]][entity[1]] = 0  # initialize the distances of entities to 0
            queue.enqueue(entity)  # queue is a copy of the list entity_type

        while (len(queue) != 0):
            cell = queue.dequeue()
            for neighbor in self.four_neighbors(cell[0], cell[1]):
                if visited[neighbor[0]][neighbor[1]] == EMPTY and self._cells[neighbor[0]][
                    neighbor[1]] == EMPTY:  # self._cells[][] keeps track of obstacles!!!!
                    visited[neighbor[0]][neighbor[1]] = FULL  # Ensure invariant and monotonicity!!!
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[cell[0]][
                                                                   cell[1]] + 1  # Ensure invariant and monotonicity!!!!
                    queue.enqueue(neighbor)

        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for human in self.humans():
            cells = self.eight_neighbors(human[0], human[1])
            cells.append(human)  # cell list including the current cell
            max_dist = -float('inf')  #negative infinity
            cells_with_max_dist = []
            for cell in cells:
                distance = zombie_distance_field[cell[0]][cell[1]]
                #distance != self.get_grid_height() * self.get_grid_width() for avoiding bumping into the obstacles
                #distance != 0 for avoiding move to the zombies
                if distance != self.get_grid_height() * self.get_grid_width() and distance != 0 and distance > max_dist:
                    cells_with_max_dist = [cell]
                    max_dist = distance
                elif distance == max_dist:
                    cells_with_max_dist.append(cell)
            if len(cells_with_max_dist) == 0:
                cells_with_max_dist.append(human)
            self._human_list[self._human_list.index(human)] = cells_with_max_dist[
                random.randrange(0, len(cells_with_max_dist))]

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for zombie in self.zombies():
            cells = self.four_neighbors(zombie[0], zombie[1])
            cells.append(zombie)  # cell list including the current cell
            min_dist = float('inf') #positive infinity!!!
            cells_with_min_dist = []
            for cell in cells:
                distance = human_distance_field[cell[0]][cell[1]]
                # distance != self.get_grid_height() * self.get_grid_width() for avoiding bumping into the obstacles
                if distance < min_dist and distance != self._grid_height * self.get_grid_width():
                    cells_with_min_dist = [cell]
                    min_dist = distance
                elif distance == min_dist and distance != self.get_grid_width() * self.get_grid_height():
                    cells_with_min_dist.append(cell)
            if len(cells_with_min_dist) == 0:
                cells_with_min_dist.append(zombie)
            self._zombie_list[self._zombie_list.index(zombie)] = cells_with_min_dist[
                random.randrange(0, len(cells_with_min_dist))]


# Start up gui for simulation
poc_zombie_gui.run_gui(Apocalypse(30, 40))
# obj = Apocalypse(3, 3, [(0, 0), (0, 1), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)], [(0, 2)], [(1, 1)])
# dist_field =  obj.compute_distance_field(ZOMBIE)
# print dist_field
# obj.move_humans(dist_field)