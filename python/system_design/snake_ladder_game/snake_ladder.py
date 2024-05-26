# board # player # dice #game

class Board():
    def __init__(self, size=100) -> None:
        self.size = size
        self.snake = {}
        self.ladder = {}
    
    def add_snake(self, head, tail):
        self.snake[head] = tail
    
    def add_ladder(self, start, end):
        self.ladder[start] = end
    
    def get_next_position(self, position):
        if position in self.snake:
            return self.snake[position]
        if position in self.ladder:
            return self.ladder[position]
        return position

    def get_size(self):
        return self.size
    
class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.position = 0
    
    def move(self, step):
        self.position += step

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

import random
class Dice:
    @staticmethod
    def roll():
        return random.randint(1,6)

class Game():
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.current_player_index = 0
        self.winner = None
    
    def play_turn(self):
        current_player = self.players[self.current_player_index]
        roll = Dice.roll()
        print(f"{current_player.name} rolled a {roll}")

        current_player.move(roll)

        if current_player.get_position() > self.board.get_size():
            current_player.set_position(self.board.size)
        
        new_position = self.board.get_next_position(current_player.get_position())
        current_player.set_position(new_position)
        print(f"{current_player.name} is now at position {current_player.get_position()}")

        if current_player.get_position() == self.board.get_size():
            self.winner = current_player
            print(f"{current_player.name} wins!")

        
        self.current_player_index = (self.current_player_index+1)%len(self.players)

    def is_game_over(self):
        return self.winner is not None
    
    def start(self):
        while not self.is_game_over():
            self.play_turn()

# Initialize the board
board = Board(size=100)
board.add_snake(16, 6)
board.add_snake(47, 26)
board.add_snake(49, 11)
board.add_snake(56, 53)
board.add_snake(62, 19)
board.add_snake(64, 60)
board.add_snake(87, 24)
board.add_snake(93, 73)
board.add_snake(95, 75)
board.add_snake(98, 78)
board.add_ladder(1, 38)
board.add_ladder(4, 14)
board.add_ladder(9, 31)
board.add_ladder(21, 42)
board.add_ladder(28, 84)
board.add_ladder(36, 44)
board.add_ladder(51, 67)
board.add_ladder(71, 91)
board.add_ladder(80, 100)

# Initialize players
players = [Player("Alice"), Player("Bob")]

# Start the game
game = Game(board, players)
game.start()
