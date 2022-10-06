
from random import randint

scores = {"computer": 0, "player": 0}

class Board:
    """
    Main Board class. Sets Board size, number of ships, the players name and
    the board type (player or computer's board)
    Has methods for adding ships and guesses and printing the board
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["-" for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print("  ".join(row))
    
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x,y) in self.ships:
            self.board[x][y] = "#"
            return "Hit!"
        else:
            return "Miss!"
    
    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
           print("All ships have been added.")
        else:
            self.ships.append((x,y))
            if self.type == "player"
                self.board [x][y] = "o"


def random_point(size):
    """
    Helper function to return a random interger
    """
    return randint(0, size -1)




def new_game():
    """
    Starts a new game. STes the board size, number of ships, resets the 
    scores and initialises the boards.
    """

    size = 6
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print ("~" * 40)
    print("Welcome to TORPEDO!")
    print(f"Board size: {size}. Number of Ships: {num_ships}")
    print("Top left corner is row: 0, column: 0")
    print("~" * 40)
    player_name = input("Please enter your name: \n")
    print("~" * 40)

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)
    
    play_game(computer_board, player_board)


new_game()