import random
import time

class Battleship:
    def __init__(self, grid_size=10, num_of_ships=2, bullets=50):
        '''
        Initialize the game with a grid of a given size as Gameboard with a number of ships and bullets.
        '''
       self.grid_size = grid_size
       self.num_of_ships = num_of_ships
       self.bullets = bullets
       self.grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
       self.ship_positions = []
       self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
       self.create_grid()
       
    def create_grid(self):
        '''
        Create a Gameboard and place ships on it.
        '''
        self.ship_positions = []
        while len(self.ship_positions) != self.num_of_ships:
            random_row = random.randint(0, self.grid_size - 1)
            random_col = random.randint(0, self.grid_size - 1)
            direction = random.choice(["left", "right", "up", "down"])
            ship_size = random.randint(3, 5)
        if self.try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            self.num_of_ships_placed += 1
            
    def play(self):
       print("-----Welcome to Battleships-----")
       print("You have 50 bullets to take down 8 ships, may the battle begin!")
     

if __name__ == '__main__':
    game = Battleship()
    game.play()