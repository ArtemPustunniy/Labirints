import random

from src.entities.maze import Maze, PossibleChoiceOfTypeOfMaze
from src.entities.point import common_elem, symbols, weights
from src.services.generators.generator import Generator


class KruskalGenerator(Generator):
    """
    A class that implements a Kruskal's algorithm-based maze generation.
    This generator uses the randomized Kruskal's algorithm to generate a maze.
    """

    def generate(
        self,
        width: int,
        height: int,
        cords: tuple,
        density,
        user_choice_of_type_of_maze,
    ) -> Maze:
        """
        Generates a maze using the Kruskal's algorithm.

        Args:
            width (int): The width of the maze.
            height (int): The height of the maze.
            cords (tuple): A tuple containing the start and end coordinates of the maze.
            density (float): The density of walls or obstacles in the maze.
            user_choice_of_type_of_maze (str): Indicates whether the maze should contain different terrains.

        Returns:
            Maze: The generated maze object.
        """
        maze = Maze(width, height, cords, density, user_choice_of_type_of_maze)

        # Initialize sets for each cell and edges between cells.
        sets = {}
        edges = []

        # Assign each cell its own set and add potential edges to the list.
        for y in range(1, height, 2):
            for x in range(1, width, 2):
                sets[(x, y)] = (x, y)
                if x < width - 2:
                    edges.append(((x, y), (x + 2, y)))
                if y < height - 2:
                    edges.append(((x, y), (x, y + 2)))

        # Shuffle edges to randomize the order of processing.
        random.shuffle(edges)

        def find(cell):
            """
            Find the root of the given cell in the disjoint set.

            Args:
                cell (tuple): The cell for which the root is to be found.

            Returns:
                tuple: The root of the given cell.
            """
            while sets[cell] != cell:
                sets[cell] = sets[sets[cell]]
                cell = sets[cell]
            return cell

        def union(cell1, cell2):
            """
            Union the sets of the two given cells.

            Args:
                cell1 (tuple): The first cell to union.
                cell2 (tuple): The second cell to union.
            """
            root1 = find(cell1)
            root2 = find(cell2)
            if root1 != root2:
                sets[root2] = root1

        # Process each edge in the shuffled list.
        for (x1, y1), (x2, y2) in edges:
            if find((x1, y1)) != find((x2, y2)):
                union((x1, y1), (x2, y2))

                # Update the symbols and weights for the chosen cells and the wall between them.
                if user_choice_of_type_of_maze == PossibleChoiceOfTypeOfMaze.YES.value:
                    choice = random.randint(0, 3)
                    if (y1 + y2) // 2 < height - 2 and (x1 + x2) // 2 < width - 2:
                        maze.grid[(y1 + y2) // 2][(x1 + x2) // 2].symbol = symbols[
                            choice
                        ]
                        maze.grid[(y1 + y2) // 2][(x1 + x2) // 2].weight = weights[
                            choice
                        ]
                        maze.grid[y1][x1].symbol = symbols[choice]
                        maze.grid[y2][x2].symbol = symbols[choice]
                        maze.grid[y1][x1].weight = weights[choice]
                        maze.grid[y2][x2].weight = weights[choice]
                else:
                    if (y1 + y2) // 2 < height - 2 and (x1 + x2) // 2 < width - 2:
                        maze.grid[(y1 + y2) // 2][
                            (x1 + x2) // 2
                        ].symbol = common_elem.symbol
                        maze.grid[y1][x1].symbol = common_elem.symbol
                        maze.grid[y2][x2].symbol = common_elem.symbol
                        maze.grid[(y1 + y2) // 2][
                            (x1 + x2) // 2
                        ].weight = common_elem.weight
                        maze.grid[y1][x1].weight = common_elem.weight
                        maze.grid[y2][x2].weight = common_elem.weight

                # Add additional open cells based on the density setting.
                if random.random() >= maze.density:
                    rand_y = random.randint(1, maze.height - 2)
                    rand_x = random.randint(1, maze.width - 2)
                    maze.grid[rand_y][rand_x].symbol = common_elem.symbol
                    maze.grid[rand_y][rand_x].weight = common_elem.weight

        return maze
