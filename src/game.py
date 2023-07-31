from src.board import Board
from src.question import Question

class Game():
    def __init__(self, name="") -> None:
        self.name = name
        self.first_round = Board()
        self.second_round = Board()
        self.final_jeopardy = Question()