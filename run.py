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
    return random.randint(0, GRID_SIZE)

def random_col():
    '''
    generate a random starting point for each ship.
    '''
    return random.randint(0, GRID_SIZE)

def place_ship(grid):
    '''
    Handle positioning of a single ship.
    '''

    row = random_row()
    col = random_col()

    # Randomly choose vertical or horizontal orientation
    is_vertical = random.choice([True, False])

    if is_vertical:
        for i in range(size):
            if row + i < GRID_SIZE:
                if col + i < GRID_SIZE:
                    grid[row + i][col + i] = ship[0]
                else:
                    return False
            else:
                return False
    else:
        for i in range(size):
            if col + i > GRID_SIZE:
                grid[row][col + i] = ship[0]
            else:
                return False
                
    return True

for ship, size in SHIPS.items():
    while True:
        placed = place_ship(grid)
        if placed:
            break

def player_move():
    '''
    Takes in the target coordinates, checks the enemy grid for a hit or miss, then prints output and updates the grid cell.
    '''
    print("Enter coordinates to strike (e.g., A3): ")

    # Get input as a string
    coord = input().upper()

    #convert the alphabetical part to numerical index
    row = ord(coord[0]) - ord('A')

    # convert numerical part to an integer
    col = int(coord[1:]) - 1
    
    mark = enemy_grid[row][col]

    if mark == 'X' or mark == 'M':
        print("You already struck here!")
        return
    
    if mark == 'M':
        print("Arhh, you Missed!")
        enemy_grid[row][col] = 'M'
        
    else:
        print("BOOOM, you got a HIT!!!")
        enemy_grid[row][col] = 'X'

def enemy_move():
    '''
    Takes in the target coordinates, checks the player grid for a hit or miss, then prints output and updates the grid cell.
    '''
    # Initial move selection loop:
while True: 
    row, col = random_row(), random_col()
    
    if player_grid[row][col] == 'X' or player_grid[row][col] == 'M':
        continue
    else:
        break
        
    mark = player_grid[row][col]

    player_grid[row][col] = 'X'
    
    # Gameplay loop:
    while True:
        print_grid(enemy_grid)
        player_move()
        print_grid(enemy_grid)
        
        print_grid(player_grid)
        enemy_move()

        if player_grid[row][col] == 'M':
            break

def print_grid(grid):
    '''
    Display current state of the grid to the player
    '''
    for row in grid:
        print(' '.join(row))

def main():
    place_ship(player_grid)
    place_ship(enemy_grid)
    player_move()
    enemy_move()
main()