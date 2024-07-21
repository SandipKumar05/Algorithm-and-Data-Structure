# Implement Minesweeper
# Minesweeper is a game where the objective is correctly identify the location of all mines in a given grid. You are given a uniform grid of gray squares in the beginning of the game. Each square contains either a mine (indicated by a value of 9), or an empty square. Empty squares have a number indicating the count of mines in the adjacent squares. Empty squares can have counts from zero (no adjacent mines) up to 8 (all adjacent squares are mines).

# If you were to take a complete grid, for example, you can see which squares have mines and which squares are empty:
    
# 0  0  0  0  0
# 0  0  0  0  0
# 1  1  1  0  0
# 1  9  1  0  0
# 1  2  2  1  0
# 0  1  9  1  0
# 0  1  1  1  0
# The squares with "2" indicate that there 2 mines adjacent to that particular square.

# Gameplay starts with a user un-hiding a square at random. If the square contains a mine, the game ends. If it is a blank, the number of adjacent mines is revealed.

# Exposing a zero means that there are no adjacent mines, so exposing all adjacent squares is guaranteed safe. As a convenience to the player, the game continues to expose adjacent squares until a non-zero square is reached.

# For example, if you click on the top right corner you get this ('-' means hidden):
# 0  0  0  0  0
# 0  0  0  0  0
# 1  1  1  0  0
# -  -  1  0  0
# -  -  2  1  0
# -  -  -  1  0
# -  -  -  1  0

# Please write functions to construct the playing field given the size and number of mines.

# Note: You can suppose that you have a Matrix class that looks like this:
# Generate random minesweeper grid.

import random

def create_empty_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def place_mines(grid, num_mines):
    rows, cols = len(grid), len(grid[0])
    mines_placed = 0
    
    while mines_placed < num_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        
        if grid[row][col] != 9:  # 9 represents a mine
            grid[row][col] = 9
            mines_placed += 1

def calculate_adjacent_mines(grid):
    rows, cols = len(grid), len(grid[0])
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 9:  # Skip mines
                continue
            
            # Check all adjacent cells
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 9:
                        grid[row][col] += 1

def generate_minesweeper_grid(rows, cols, num_mines):
    grid = create_empty_grid(rows, cols)
    place_mines(grid, num_mines)
    calculate_adjacent_mines(grid)
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))

# Example usage
rows, cols = 8, 8
num_mines = 10

minesweeper_grid = generate_minesweeper_grid(rows, cols, num_mines)
print_grid(minesweeper_grid)