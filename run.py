import random


grid = [["."] * 10 for row in range(10)]

GRID_SIZE = 10
SHIPS = {"Carrier": 5, "Submarine": 3, "Battleship1": 4, "Battleship2": 4}

def random_row(GRID_SIZE):
    '''
    generate a random starting point for each ship.
    '''
    return random.randint(0, GRID_SIZE - 1)

def random_col(GRID_SIZE):
    '''
    generate a random starting point for each ship.
    '''
    return random.randint(0, GRID_SIZE - 1)

def place_ship(grid, ship, size, GRID_SIZE):
    '''
    Handle positioning of a single ship. while True loop keep trying until a valid position is found.
    It checks for both the boundary and overlapping conditions before placing the ship.
    '''
    while True:
        row = random_row(GRID_SIZE)
        col = random_col(GRID_SIZE)

        # Randomly choose vertical or horizontal orientation
        is_vertical = random.choice([True, False])

        if is_vertical:
            if row + size > GRID_SIZE:
                continue

            valid_position = all(
                grid[row + i][col] == '.' for i in range(size)
            )
            if not valid_position:
                continue

            for i in range(size):
                grid[row + i][col] = ship[0]
        else:
            if col + size > GRID_SIZE:
                continue

            valid_position = all(
                grid[row][col + i] == '.' for i in range(size)
            )
            if not valid_position:
                continue

            for i in range(size):
                grid[row][col + i] = ship[0]

        break

    return True


def player_move(player_grid, enemy_grid, GRID_SIZE, player_name):
    '''
    Takes in the target coordinates, checks the enemy grid for a hit or miss,
    then prints output and updates the grid cell.
    '''
    print("Enter coordinates to strike (e.g., A3): ")

    # Get input as a string
    coord = input().upper()

    # Convert the alphabetical part to a numerical index
    row = ord(coord[0]) - ord('A')

    # Convert the numerical part to an integer
    col = int(coord[1:]) - 1

    player_messages = []
    # Check if coordinates are within the valid range
    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
        mark = enemy_grid[row][col]

        if mark == 'X' or mark == 'M':
            player_messages.append("You already struck here!")
            return

        if mark[0] in ['S', 'D', 'B']:
            player_messages.append("BOOOM, you got a Hit!!!")
            enemy_grid[row][col] = '@'

        else:
            player_messages.append("Arhh, you Missed!")
            enemy_grid[row][col] = 'X'

        print("\n")
        print(f"This is {player_name}'s Gameboard, with your own Ships!:")
        print_player_grid(player_grid, GRID_SIZE)

        print_grid(enemy_grid, GRID_SIZE)
        print("The Gameboard above is your opponent's Gameboard and shows where you shot already!")
    
    else:
        player_messages.append("You shot out of the range, please try again")
    
    print_moves(player_messages)

    return player_messages

    
def enemy_move(player_grid, GRID_SIZE):
    '''
    Takes in the target coordinates, checks the player grid for a hit or miss, then prints output and updates the grid cell.
    '''
    
    ships_remaining = sum(SHIPS.values())

    # Initial move selection loop:
    while True: 
        row, col = random_row(GRID_SIZE), random_col(GRID_SIZE)
        
        if player_grid[row][col] not in ['X', 'M']:
            break

    enemy_messages = []
    mark = player_grid[row][col]

    if mark[0] in ['S', 'D', 'B']:
        #enemy_messages.append("Computers move...")
        enemy_messages.append("Hit!")
        player_grid[row][col] = '@'
        ships_remaining -= 1
    else:
        #enemy_messages.append("Computers move...")
        enemy_messages.append("Missed!")
        player_grid[row][col] = 'M'

    print_moves(enemy_messages)

    return enemy_messages


def print_grid(grid, GRID_SIZE):
    '''
    Display current state of the grid to the player and hide positioning of Ships from enemy and player Grid
    '''
    print('  ' + ' '.join(str(i + 1) for i in range(GRID_SIZE)))
    print(' ' + '-' * (2 * GRID_SIZE + 1))

    for i, row in enumerate(grid):
        #print(' ' + '-' * (2 * GRID_SIZE + 1))

        # Hide Ships
        #print(chr(i + ord('A')) + '|' + '|'.join('.' if cell in ['S', 'D', 'B'] else cell for cell in row) + '|')
        print(chr(i + ord('A')) + '|' + '|'.join(row) + '|') # delte this line after debugging
    print(' ' + '-' * (2 * GRID_SIZE + 1))

def print_player_grid(grid, grid_size):
    '''
    Display current state of the player's grid to the player with also showing positioning of player ships
    '''
    print(' ' + ' '.join(str(i + 1) for i in range(GRID_SIZE)))
    print(' ' + '-' * (2 * GRID_SIZE + 1))


    for i, row in enumerate(grid):
        #print(' ' + '-' * (2 * GRID_SIZE + 1))
        
        #display ships
        print(chr(i + ord('A')) + '|' + '|'.join(row))
    print('-' + '-' * (2 * GRID_SIZE + 1))

def print_moves(*args):
    if len(args) >= 2:
        player_name = args[0]
        player_messages = args[1]
        enemy_messages = args[2] if len(args) >= 3 else []

        separator = '-' * 25

        print(separator)
        print(f"{player_name}'s move:")
        for message in player_messages:
            print(message)

        print(separator)

        print("Enemy's Move:")
        for message in enemy_messages:
            print(message)

        print(separator)

def get_valid_player_name():
    '''
    Get and validate player name
    '''

    while True:
        player_name = input("Please Enter your name:\n")

        for char in player_name:
            if not ('A' <= char <= 'Z' or 'a' <= char <= 'z'):
                print("The entered name is not valid. Please enter a name using letters (e.g. Aa)")
                break
            
        else:
            print(f"Welcome {player_name}!")
            return player_name

def main():
    
    player_name = get_valid_player_name()
    #player_name = input("Please Enter your name:\n")

    # Let the user adjust the grid size
    #while True:
        #PLAYER_GRID_SIZE = int(input("Enter the size of the player's grid (e.g., 10):\n"))
        #if 4 <= PLAYER_GRID_SIZE <= 26:
            #break
        #else:
            #print("Invalid size. Please enter a size between 4 and 26!")

    #while True:
        #ENEMY_GRID_SIZE = int(input("Enter the size of the enemy's grid (e.g., 10):\n"))
        #if 4 <= ENEMY_GRID_SIZE <= 26:
            #break
        #else:
            #print("Invalid size. Please enter a size between 4 and 26!")

    player_grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    enemy_grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Get the number of ships for each type from the user for both player and enemy
    #num_ships_player = {}
    #num_ships_enemy = {}

    #for ship, _ in SHIPS.items():
        #num_player = int(input(f"Enter the number of {ship}s for the player:\n"))
        #num_enemy = int(input(f"Enter the number of {ship}s for the enemy:\n"))
        
        #num_ships_player[ship] = num_player
        #num_ships_enemy[ship] = num_enemy

    
    # Place ships on player's grid
    for ship, size in SHIPS.items():
        #for _ in range(size):
        while True:
            placed = place_ship(player_grid, ship, size, GRID_SIZE)
            if placed:
                break
        
    # Place ships on enemy's grid
    for ship, size in SHIPS.items():
        #for _ in range(size):
        while True:
            placed = place_ship(enemy_grid, ship, size, GRID_SIZE)
            if placed:
                break

    while sum(SHIPS.values()) > 0:
        player_messages = player_move(player_grid, enemy_grid, GRID_SIZE, player_name)
        enemy_messages = enemy_move(enemy_grid, GRID_SIZE)

        print_moves(player_name, player_messages, enemy_messages)

        #print('-' * (2 * GRID_SIZE + 1))  # Separator line
        #print_moves(player_move, enemy_move)
main()