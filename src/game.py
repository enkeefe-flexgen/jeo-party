from src.board import Board
from src.category import Category

class Game():
    def __init__(self, name="") -> None:
        self.name = name
        self.first_round = Board()
        self.second_round = Board()
        self.final_jeopardy = Category()