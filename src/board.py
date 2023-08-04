
class Board():
    def __init__(self, categories=[""]) -> None:
        self.player_in_control = ""
        self.category_names = categories
        self.category_objs = []