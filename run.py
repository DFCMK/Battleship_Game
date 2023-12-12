import random
import time

grid = ["." * 10] * 10

GRID_SIZE = 10
SHIPS = {"Destroyer": 2, "Submarine": 3, "Battleship": 4}

player_grid = [["."] * GRID_SIZE for _ in range(GRID_SIZE)]

def random_row():
    '''
    generate a random starting point for each ship.
    '''
    return random.randint(0, GRID_SIZE, -1)

def random_col():
    '''
    generate a random starting point for each ship.
    '''
    return random.randint(0, GRID_SIZE, -1)

def place_ship():
    '''
    Handle positioning of a single ship.
    '''

    row = random_row()
    col = random_col()

    # Randomly choose vertical or horizontal orientation
    is_vertical = random.choice([True, False])

    if is_vertical:
        if row + size > GRID_SIZE:
            return False

        for i in range(size):
            grid[row + i][col] = ship[0]
    else:
        if col + size > GRID_SIZE:
            return False

        for i in range(size):
            grid[row][col + i] = ship[0]

    return True

    for ship, size in ship.items():
        while True:
            placed = place_ship(ship, size, grid)
        if placed:
            break
