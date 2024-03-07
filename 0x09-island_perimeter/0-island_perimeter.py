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
                perimeter += 4

                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

            # # check the contents of the top
            # if r - 1 < 0 and :
            #     p += 1
            #     continue
            # if grid[r - 1][c] == 0:
            #     p += 1

            # # check the contents of the bottom
            # if r + 1 > rows - 1:
            #     p += 1
            #     continue
            # if grid[r + 1][c] == 0:
            #     p += 1

            # # check the contents of the left side
            # if c - 1 < 0:
            #     p += 1
            #     continue
            # if grid[r][c - 1] == 0:
            #     p += 1

            # # check the contents of the right side
            # if c + 1 > cols - 1:
            #     p += 1
            #     continue
            # if grid[r][c + 1] == 0:
            #     p += 1
    return perimeter