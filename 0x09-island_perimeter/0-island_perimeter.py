def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): The grid representation of the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Add 4 for each land cell
                perimeter += 4

                # Check for neighboring land cells and subtract for shared borders
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2  # Subtract 2 for the shared border with the cell above
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2  # Subtract 2 for the shared border with the cell to the left

    return perimeter
