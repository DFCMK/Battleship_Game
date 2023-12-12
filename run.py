import random
import time

class Battleship:
   def __init__(self, grid_size=10, num_of_ships=2, bullets=50):
    """
    Initialize the game with a grid of a given size as Gameboard with a number of ships, and a number of bullets.
    """
    self.grid_size = grid_size
    self.num_of_ships = num_of_ships
    self.bullets = bullets
    self.grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    self.ship_positions = []
    self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    self.create_grid()

