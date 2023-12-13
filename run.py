import random

grid = [["."] for in _ range(10)]

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

for ship, size in SHIPS.items():
    while True:
        placed = place_ship(ship, size, grid)
        if placed:
            break

def player_move():
    '''
    Takes in the target coordinates, checks the enemy grid for a hit or miss, then prints output and updates the grid cell.
    '''
    print("Enter row and column to strike: ")

    row, col = input().split()
    row, col = int(row), int(col)

    mark = enemy_grid[row][col]

    if mark == 'X' or mark == '-':
        print("You already struck here!")
        return
    
    if mark == '-':
        print("Arhh, you Missed!")
        enemy_grid[row][col] = '-'
        
    else:
        print("BOOOM, you got a HIT!!!")
        enemy_grid[row][col] = 'X'

def enemy_move():
    '''
    Takes in the target coordinates, checks the player grid for a hit or miss, then prints output and updates the grid cell.
    '''

    row, col = input().split()
    row, col = int(row), int(col)

    mark = player_grid[row][col]

    if mark == 'X' or mark == '-':
        return
    
    if mark == '-':
        print("Enemy Missed!")
        player_grid[row][col] = '-'
    else:
        print("Enemy Hit!")
        player_grid[row][col] = 'X'

while True:
    player_move()
    print_grid(enemy_grid)

    enemy_move()
    print_grid(player_grid)

def main():
    random_row()
    random_col()
    place_ship()
    player_move()
    enemy_move()