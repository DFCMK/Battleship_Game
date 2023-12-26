import random


grid = [["."] * 10 for row in range(10)]

GRID_SIZE = 10
SHIPS = {"Carrier": 5, "Submarine": 3, "Battleship1": 4, "Battleship2": 4}


def display_game_info():
    '''
    Display general information about the Game
    '''
    # Define the box characters
    horizontal_line = "-" * 79
    vertical_line = "|"

    # Top border of the box
    print("+" + horizontal_line + "|")

    # Content
    print("|{:<79}|".format("BATTLESHIP GAME"))
    print("|{:<79}|".format("Game Overview:"))
    print("|{:<79}|".format("1. You find yourself in the midst of a naval battlefield on a 10x10 grid."))
    print("|{:<79}|".format("2. Four enemy battleships of various lengths are hidden throughout the grid."))
    print("|" + horizontal_line + "|")
    print("|{:<79}|".format("Game Rules:"))
    print("|{:<79}|".format("1. You can choose a target by specifying a row and column (e.g., A3)."))
    print("|{:<79}|".format("2. Each shot will be displayed on the grid, indicating whether it hit or missed."))
    print("|{:<79}|".format("3. Ships are oriented either horizontally or vertically, never diagonally."))
    print("|{:<79}|".format("4. The grid legend includes symbols to represent empty space, ship parts,\n hit ship parts, and missed shots.\n"))
    print("|" + horizontal_line + "|")
    print("|{:<79}|".format("Legend:"))
    print("|{:<79}|".format("1.'.': Empty space on the grid."))
    print("|{:<79}".format("2.B (Battleship), S (Submarine), C (Carrier): \n These letters represent parts of every Ship type of an battleship.\n"))
    print("|{:<79}|".format("3.@: Part of a battleship that was hit by a bullet."))
    print("|{:<79}|".format("Your objective:"))
    print("|{:<79}".format("Sink all the enemy battleships before your opponent is sinking all of yours to  secure victory!"))

    # Bottom border of the box
    print("+" + horizontal_line + "Game will start after entering a player name!\n")

display_game_info()

def random_row(GRID_SIZE, attacked_rows):
    '''
    generate a random starting point for each ship and keep track of attacked rows with writing them into a list.
    '''
    row = random.randint(0, GRID_SIZE -1)
    if row not in attacked_rows:
        return row

def random_col(GRID_SIZE, attacked_cols):
    '''
    generate a random starting point for each ship and keep track of attacked cols with writing them into a list.
    '''
    col = random.randint(0, GRID_SIZE -1)
    if col not in attacked_cols:
        return col

def place_ship(grid, ship, size, GRID_SIZE, attacked_rows, attacked_cols):
    '''
    Handle positioning of a single ship. while True loop keep trying until a valid position is found.
    It checks for both the boundary and overlapping conditions before placing the ship.
    '''
    while True:
        row = random_row(GRID_SIZE, attacked_rows)
        col = random_col(GRID_SIZE, attacked_cols)

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


def player_move(enemy_grid, GRID_SIZE, attacked_rows, attacked_cols):
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

        if mark == 'X' or mark == '@':
            player_messages.append("You already struck here!")
            return

        if mark[0] in ['S', 'C', 'B']:
            player_messages.append("BOOOM, you got a Hit!!!")
            enemy_grid[row][col] = '@'

        else:
            player_messages.append("Arhh, you Missed!") 
            enemy_grid[row][col] = 'X'

        #print("\n")
        #print(f"This is {player_name}'s Gameboard, with {player_name}'s Ships!:")
        #print_player_grid(player_grid, GRID_SIZE)

        # Print the enemy grid after player's move
        print("This is your oppenent's Gameboard with your shots!:")
        print_grid(enemy_grid, GRID_SIZE)
    
    else:
        player_messages.append("You shot out of the range, please try again")
    
    print_moves(player_messages)

    return player_messages, attacked_rows, attacked_cols

    
def enemy_move(player_grid, GRID_SIZE, attacked_rows, attacked_cols, player_name):
    '''
    Takes in the target coordinates, checks the player grid for a hit or miss, then prints output and updates the grid cell.
    '''
    
    ships_remaining = sum(SHIPS.values())

    # Initial move selection loop:
    while True: 
        row, col = random_row(GRID_SIZE), random_col(GRID_SIZE)
        
        if player_grid[row][col] not in ['M', '@']:
            break

    enemy_messages = []
    mark = player_grid[row][col]

    if mark[0] in ['S', 'C', 'B']:
        #enemy_messages.append("Computers move...")
        enemy_messages.append("Hit!")
        player_grid[row][col] = '@'
        ships_remaining -= 1
    else:
        #enemy_messages.append("Computers move...")
        enemy_messages.append("Missed!")
        player_grid[row][col] = 'M'

    print_grid(enemy_grid, GRID_SIZE)
    print("The Gameboard above is your opponent's Gameboard and shows where you shot already!")
    
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
            print('-' * (2 * GRID_SIZE + 1))
            print(f"Welcome {player_name}, good Luck!")
            print('-' * (2 * GRID_SIZE + 1))
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

    attacked_rows = []
    attacked_cols = []
    
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

    while True: # Game loop
        player_messages, attacked_rows, attacked_cols = player_move(enemy_grid, GRID_SIZE, attacked_rows, attacked_cols)
        
        enemy_messages = enemy_move(player_grid, GRID_SIZE, attacked_rows, attacked_cols, player_name)

        print_moves(player_name, player_messages, enemy_messages)

        if not player_messages and not enemy_messages:
            break

    while sum(SHIPS.values()) == 0:
        print("All ships have been sunk. Congratualtions!")
        break
main()