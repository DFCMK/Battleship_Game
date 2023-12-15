import random

grid = [["."] * 10 for row in range(10)]

GRID_SIZE = 10
SHIPS = {"Destroyer": 2, "Submarine": 3, "Battleship": 4}

player_grid = [["."] * GRID_SIZE for _ in range(GRID_SIZE)]

enemy_grid = [["."] * GRID_SIZE for _ in range(GRID_SIZE)]


def random_row():
    '''
    generate a random starting point for each ship.
    '''
    return random.randint(0, GRID_SIZE - 1)

def random_col():
    '''
    generate a random starting point for each ship.
    '''
    return random.randint(0, GRID_SIZE - 1)

def place_ship(grid, ship, size):
    '''
    Handle positioning of a single ship.
    '''
    row = random_row()
    col = random_col()

    # Randomly choose vertical or horizontal orientation
    is_vertical = random.choice([True, False])

    if is_vertical:
        for i in range(size):
            if 0 <= row + i < GRID_SIZE and 0 <= col < GRID_SIZE and grid[row + i][col] != 'X':
                grid[row + i][col] = ship[0]
            else:
                return False
    else:
        for i in range(size):
            if 0 <= row < GRID_SIZE and 0 <= col + i < GRID_SIZE and grid[row][col + i] != 'X':
                grid[row][col + i] = ship[0]
            else:
                return False
                
    return True

for ship, size in SHIPS.items():
    while True:
        placed = place_ship(grid, ship, size)
        if placed:
            break


def player_move():
    '''
    Takes in the target coordinates, checks the enemy grid for a hit or miss, then prints output and updates the grid cell.
    '''
    print("Enter coordinates to strike (e.g., A3): ")

    # Get input as a string
    coord = input().upper()

    # Convert the alphabetical part to a numerical index
    row = ord(coord[0]) - ord('A')

    # Convert the numerical part to an integer
    col = int(coord[1:]) - 1
   
    mark = enemy_grid[row][col]

    if mark == 'X' or mark == 'M':
        print("You already struck here!")
        return
   
    if mark != 'B':
        print("Arhh, you Missed!")
        enemy_grid[row][col] = 'M'
    
    else:
        print("BOOOM, you got a HIT!!!")
        enemy_grid[row][col] = 'X'

    print("This is your Gameboard, with your own Ships!:\n")
    print_player_grid(player_grid)

    print("This is your enemies Gameboard which show you where you shoot already!:\n")
    print_grid(enemy_grid)
    

def enemy_move():
    '''
    Takes in the target coordinates, checks the player grid for a hit or miss, then prints output and updates the grid cell.
    '''
    
    ships_remaining = sum(SHIPS.values())

    # Initial move selection loop:
    while True: 
        row, col = random_row(), random_col()
        
        if player_grid[row][col] == 'X' or player_grid[row][col] == 'M':
            continue
        else:
            break

    mark = player_grid[row][col]

    if mark == 'B':
        print("Computers move...\n")
        print("Hit!\n")
        player_grid[row][col] = 'X'
        ships_remaining -= 1
    else:
        print("Computers move...\n")
        print("Missed!\n")
        player_grid[row][col] = 'M'

def print_grid(grid):
    '''
    Display current state of the grid to the player and hide positioning of Ships from enemy and player Grid
    '''
    for row in grid:
        print(' '.join('.' if cell == '.' or cell == 'X' or cell == 'B' else 'X' for cell in row))

def print_player_grid(grid):
    '''
    Display current state of the player's grid to the player with also showing positioning of player ships
    '''
    for row in grid:
        print(' '.join(row))

def main():
    place_ship(player_grid, ship, size)
    place_ship(enemy_grid, ship, size)
    while sum(SHIPS.values()) > 0:
        player_move()
        enemy_move()
main()