import random

grid = [["."] * 11 for row in range(11)]

GRID_SIZE = 11
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
    generate a random starting point for each ship.
    '''
    while True:
        row = random.randint(0, GRID_SIZE -2)
        if row not in attacked_rows:
            return row

def random_col(GRID_SIZE, attacked_cols):
    '''
    generate a random starting point for each ship.
    '''
    while True:
        col = random.randint(0, GRID_SIZE -2)
        if col not in attacked_cols:
            return col

def place_ship(grid, ship, size, GRID_SIZE, attacked_cells):
    while True:
        row = random_row(GRID_SIZE, attacked_cells)
        col = random_col(GRID_SIZE, attacked_cells)

        # Ensure that the ship is not placed in the last column and row
        if col + size > GRID_SIZE or row + size > GRID_SIZE or col + size == GRID_SIZE or row + size == GRID_SIZE:
            continue

        # Randomly choose direction (horizontal, vertical, or diagonal)
        direction = random.choice(['horizontal', 'vertical', 'diagonal'])

        if direction == 'horizontal':
            valid_position = all(grid[row][col + i] == '.' for i in range(size))
            if not valid_position:
                continue

            for i in range(size):
                grid[row][col + i] = ship[0]

        elif direction == 'vertical':
            valid_position = all(grid[row + i][col] == '.' for i in range(size))
            if not valid_position:
                continue

            for i in range(size):
                grid[row + i][col] = ship[0]

        elif direction == 'diagonal':
            valid_position = all(grid[row + i][col + i] == '.' for i in range(size))
            if not valid_position:
                continue

            for i in range(size):
                grid[row + i][col + i] = ship[0]

        break

    return True


def player_move(enemy_grid, GRID_SIZE, attacked_cells):
    '''
    Handle player's move, displaying a hit with '@' and a miss with a 'X' on the opponent's grid. 
    It also give user the option to exit the game at any time by entering the 'exit' command.
    Additionally, it handles two-digit coordinate inputs like A10.
    '''
    while True:
        print("Enter coordinates to strike (e.g., A3): ")

        # Get input as a string
        coord = input().upper()

        if coord.lower() == "exit":
            print("Exiting the game. Goodbye!")
            exit()

        # Validate the input format
        if len(coord) >= 2 and 'A' <= coord[0] <= 'K':
            # Convert the alphabetical part to a numerical index
            row = ord(coord[0]) - ord('A')
            try:     
                # Convert the numerical part to an integer
                col = int(coord[1:]) - 1

                # Validate the column range
                if 0 <= col < GRID_SIZE:
                    pass
                else:
                    print("Invalid column. Please enter coordinates in the format A1 to J10.")
                    continue
            except ValueError:
                print("Invalid input. Please enter coordinates in the format A1 to J10.")
                continue
        else:
            print("Invalid input. Please enter coordinates in the format A1 to J10.")
            continue

        player_messages = []

        # Check if coordinates are within the valid range
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            if (row, col, "player") in attacked_cells:
                print("You already guessed these coordinates. Try again.")
                continue

            mark = enemy_grid[row][col]

            if mark in ['X', '@']:
                player_messages.append("You already struck here!")

            elif mark[0] in ['S', 'C', 'B']:
                player_messages.append("BOOOM, you got a Hit!!!")
                enemy_grid[row][col] = '@'

                attacked_cells.append((row, col, "player"))

            else:
                player_messages.append("Arhh, you Missed!")
                enemy_grid[row][col] = 'X'

                attacked_cells.append((row, col, "player"))

            # Print the enemy grid after the player's move
            print('-' * (4 * GRID_SIZE + 1))
            print(f"This is the computer's Grid, with your own shots!:")
            print_grid(enemy_grid, GRID_SIZE)
            break 

        else:
            player_messages.append("You shot out of the range, please try again")
            print_moves(player_messages)

    print_moves(player_messages)
    return player_messages, attacked_cells
   
def enemy_move(player_grid, GRID_SIZE, attacked_cells, player_name):
    '''
    Takes in the target coordinates, checks the player grid for a hit or miss, then prints output and updates the grid cell.
    '''

    # Check if all enemy ships have been sunk
    ships_remaining = sum(SHIPS.values())
    if ships_remaining == 0:
        print(f"{player_name} has sunk all enemy ships! {player_name} wins!")
        return None

    # Check if all rows have been hit by the player
    if all(row in [cell[0] for cell in attacked_cells if cell[2] == "player"] for row in range(GRID_SIZE)):
        print("All rows have been hit. The computer is unable to make a move.")
        return None

    # Initial move selection loop:
    while True:
        
        available_cells = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if (r, c, "enemy") not in attacked_cells]
        if not available_cells:
            print("No available rows to attack. The computer is unable to make a move.")
            return None

        row, col = random.choice(available_cells)

        # Check if the selected cell has already been hit
        if (row, col, "enemy") in [(cell[0], cell[1], cell[2]) for cell in attacked_cells]:
            print(f"Cell ({row}, {col}) already attacked. Skipping.")
            continue

        break

    enemy_messages = []
    mark = player_grid[row][col]

    if mark[0] in ['S', 'C', 'B']:
        enemy_messages.append("Hit!")
        player_grid[row][col] = '@'
        ships_remaining -= 1

    else:
        enemy_messages.append("Missed!")
        player_grid[row][col] = 'X'


    # Update attacked rows and cols for enemy move
    attacked_cells.append((row, col, "enemy"))

    # Print the player grid after enemy's move
    print_player_grid(player_grid, GRID_SIZE)
    print(f"The Grid above is {player_name}'s Gameboard, with {player_name}'s Ships!")
    print('-' * (2 * GRID_SIZE + 1))
    print_moves(enemy_messages)

    return enemy_messages


def print_grid(grid, GRID_SIZE):
    '''
    Display current state of the grid to the player and hide positioning of Ships from enemy and player Grid
    '''
    print(' ' + ' '.join(str(i) for i in range(1, GRID_SIZE)))
    print(' ' + '-' * (2 * GRID_SIZE - 1))

    for i, row in enumerate(grid[:-1]):
        # Hide Ships
        print(chr(i + ord('A')) + '|' + '|'.join('.' if cell in ['S', 'C', 'B'] else cell for cell in row[:-1]) + '|')
    print(' ' + '-' * (2 * GRID_SIZE - 1))

def print_player_grid(grid, GRID_SIZE):
    '''
    Display current state of the player's grid to the player with also showing positioning of player ships
    '''
    print(' ' + ' '.join(str(i) for i in range(1, GRID_SIZE)))
    print(' ' + '-' * (2 * GRID_SIZE - 1))

    for i, row in enumerate(grid[:-1]):
        # Display ships
        print(chr(i + ord('A')) + '|' + '|'.join(row[:-1]) + '|')
    print(' ' + '-' * (2 * GRID_SIZE - 1))


def print_moves(*args):
    '''
    This function prints enemy's and player's move to terminal seperated by a seperator line.
    '''
    if len(args) >= 2:
        player_name = args[0]
        player_messages = args[1]
        enemy_messages = args[2] if len(args) >= 3 else []

        separator = '-' * 25

        #print(separator)
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
            print('-' * (4 * GRID_SIZE + 1))
            print(f"Welcome {player_name}, good Luck!")
            print('-' * (4 * GRID_SIZE + 1))
            return player_name

def play_game(player_grid, enemy_grid, GRID_SIZE, attacked_cells, player_name):
    '''
    Contains main Game Loop.
    It is responsible for checking if all ships on the enemy's and player's Grid got sunk and if all cells got hit.  
    '''
    game_over = False

    while not game_over:
        player_messages, attacked_cells = player_move(enemy_grid, GRID_SIZE, attacked_cells)
        
        # Check if all player ships have been sunk
        if all(player_grid[row][col] == '@' for row in range(GRID_SIZE) for col in range(GRID_SIZE) if player_grid[row][col][0] in ['S', 'C', 'B']):
            print("All ship parts have been hit. The game is over!")
            game_over = True
            break


        # Check if all rows have been hit by the player
        if all(row in [cell[0] for cell in attacked_cells if cell[2] == "player"] for row in range(GRID_SIZE)):
            print(f"All player ships have been sunk. The computer wins!")
            game_over = True
            break

        # Check if all ship parts have been hit by the enemy
        if all(enemy_grid[row][col] == '@' for row in range(GRID_SIZE) for col in range(GRID_SIZE) if enemy_grid[row][col][0] in ['S', 'C', 'B']):
            print(f"All enemy ships have been sunk. {player_name} wins!")
            game_over = True
            break

        enemy_messages = enemy_move(player_grid, GRID_SIZE, attacked_cells, player_name)

        # Check if enemy_move returned None (indicating the game should end)
        if enemy_messages is None:
            game_over = True
            break

        print_moves(player_name, player_messages, enemy_messages)

        # Check if all cells have been hit
        if all((row, col) in [(cell[0], cell[1]) for cell in attacked_cells if cell[2] == "enemy"] for row in range(GRID_SIZE) for col in range(GRID_SIZE)):
            print("All cells have been hit. The game is over!")
            game_over = True
            break

        if not player_messages and not enemy_messages:
            game_over = True
            break

    print("Game over!")


def main():
    player_name = get_valid_player_name()

    attacked_cells = []

    # Reset player Grid at the start of each round
    player_grid = [['.'] * GRID_SIZE for _ in range(GRID_SIZE)]

    # Place ships on player's grid
    for ship, size in SHIPS.items():
        while True:
            placed = place_ship(player_grid, ship, size, GRID_SIZE, attacked_cells)
            if placed:
                break

    # Reset enemy Grid at the start of each round
    enemy_grid = [['.'] * GRID_SIZE for _ in range(GRID_SIZE)]

    # Place ships on the enemy's grid
    for ship, size in SHIPS.items():
        while True:
            placed = place_ship(enemy_grid, ship, size, GRID_SIZE, attacked_cells)
            if placed:
                break

    print("Ships placed, starting the game!", flush=True)
    print('-' * (4 * GRID_SIZE + 1))

    play_game(player_grid, enemy_grid, GRID_SIZE, attacked_cells, player_name)

main()