

class Player():
    def __init__(self, name: str) -> None:
        self.name = name
        self.score = 0

    def update_score(self, points_val: int):
        self.score = self.score + points_val
        return self.score