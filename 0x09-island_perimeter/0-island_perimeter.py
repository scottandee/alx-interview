#!/usr/bin/python3
"""This module contains a function that
solves the island perimeter interview
question
"""


def island_perimeter(grid):
    """This function returns the perimeter
    of the island found in the 2D array grid
    passed as parameter
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    # Iterate through all elements of the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Assume each grid has a perimeter of 4
                perimeter += 4
                # Check if adjacent sides are land

                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2
    return perimeter
