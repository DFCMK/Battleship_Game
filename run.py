import random

grid = [["."] * 10 for row in range(10)]

#GRID_SIZE = 10
SHIPS = {"Destroyer": 2, "Submarine": 3, "Battleship": 4}

def random_row(grid_size):
    '''
    generate a random starting point for each ship.
    '''
    return random.randint(0, grid_size - 1)

def random_col(grid_size):
    '''
    generate a random starting point for each ship.
    '''
    return random.randint(0, grid_size - 1)

def place_ship(grid, ship, size, grid_size):
   '''
   Handle positioning of a single ship.
   '''
   row = random_row(grid_size)
   col = random_col(grid_size)

   # Randomly choose vertical or horizontal orientation
   is_vertical = random.choice([True, False])

   if is_vertical:
       if row + size > grid_size:
           return False

       for i in range(size):
           if ( 
            0 <= row + i < grid_size
            and 0 <= col < grid_size
            and (grid[row + i][col] != '.' or grid[row + i][col] == ship[0])):
               return False

       for i in range(size):
           grid[row + i][col] = ship[0]
   else:
       if col + size > grid_size:
           return False

       for i in range(size):
           if (
            0 <= row < grid_size
            and 0 <= col + i < grid_size
            and (grid[row][col + i] != '.' or grid[row][col + i] != ship[0])):
               return False

       for i in range(size):
           grid[row][col + i] = ship[0]
   
   return True




def player_move(player_grid, enemy_grid, PLAYER_GRID_SIZE, ENEMY_GRID_SIZE):
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
   
    if mark[0] in ['S', 'D', 'B']:
        print("BOOOM, you got a Hit!!!\n")
        enemy_grid[row][col] = '@'
    
    else:
        print("Arhh, you Missed!\n")
        enemy_grid[row][col] = 'X'

    print("This is your Gameboard, with your own Ships!:\n")
    print_player_grid(player_grid, PLAYER_GRID_SIZE)

    print("This is your enemies Gameboard which show you where you shoot already!:\n")
    print_grid(enemy_grid, ENEMY_GRID_SIZE)
    

def enemy_move(player_grid, ENEMY_GRID_SIZE):
    '''
    Takes in the target coordinates, checks the player grid for a hit or miss, then prints output and updates the grid cell.
    '''
    
    ships_remaining = sum(SHIPS.values())

    # Initial move selection loop:
    while True: 
        row, col = random_row(ENEMY_GRID_SIZE), random_col(ENEMY_GRID_SIZE)
        
        if player_grid[row][col] not in ['X', 'M']:
            break

    mark = player_grid[row][col]

    if mark[0] in ['S', 'D', 'B']:
        print("Computers move...\n")
        print("Hit!\n")
        player_grid[row][col] = '@'
        ships_remaining -= 1
    else:
        print("Computers move...\n")
        print("Missed!\n")
        player_grid[row][col] = 'M'

    print_grid(player_grid, ENEMY_GRID_SIZE)

def print_grid(grid, grid_size):
    '''
    Display current state of the grid to the player and hide positioning of Ships from enemy and player Grid
    '''
    print('  ' + ' '.join(str(i + 1) for i in range(grid_size)))

    for i, row in enumerate(grid):
        print(' ' + '-' * (2 * grid_size + 1))
        print(chr(i + ord('A')) + '|' + '|'.join('.' if cell in ['S', 'D', 'B'] else cell for cell in row) + '|')
    print(' ' + '-' * (2 * grid_size + 1))

def print_player_grid(grid, grid_size):
    '''
    Display current state of the player's grid to the player with also showing positioning of player ships
    '''
    print('  ' + ' '.join(str(i + 1) for i in range(grid_size)))

    for i, row in enumerate(grid):
        print(' ' + '-' * (2 * grid_size + 1))
        print(chr(i + ord('A')) + '|' + '|'.join(row) + '|')
    print(' ' + '-' * (2 * grid_size + 1))


def main():
    
    # Let the user adjust the grid size
    while True:
        PLAYER_GRID_SIZE = int(input("Enter the size of the player's grid (e.g., 10):\n"))
        if 4 <= PLAYER_GRID_SIZE <= 26:
            break
        else:
            print("Invalid size. Please enter a size between 4 and 26!")

    while True:
        ENEMY_GRID_SIZE = int(input("Enter the size of the enemy's grid (e.g., 10):\n"))
        if 4 <= ENEMY_GRID_SIZE <= 26:
            break
        else:
            print("Invalid size. Please enter a size between 4 and 26!")

    player_grid = [['.' for _ in range(PLAYER_GRID_SIZE)] for _ in range(PLAYER_GRID_SIZE)]
    enemy_grid = [['.' for _ in range(ENEMY_GRID_SIZE)] for _ in range(ENEMY_GRID_SIZE)]

    # Get the number of ships for each type from the user for both player and enemy
    num_ships_player = {}
    num_ships_enemy = {}

    for ship, _ in SHIPS.items():
        num_player = int(input(f"Enter the number of {ship}s for the player:\n"))
        num_enemy = int(input(f"Enter the number of {ship}s for the enemy:\n"))
        
        num_ships_player[ship] = num_player
        num_ships_enemy[ship] = num_enemy

        # Place ships on player's grid
        for _ in range(num_player):
            while True:
                placed = place_ship(player_grid, ship, SHIPS[ship], PLAYER_GRID_SIZE)
                if placed:
                    break

    while sum(SHIPS.values()) > 0:
        player_move(player_grid, enemy_grid, PLAYER_GRID_SIZE, ENEMY_GRID_SIZE)
        enemy_move(player_grid, ENEMY_GRID_SIZE)


main()