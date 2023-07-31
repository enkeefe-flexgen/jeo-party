

class Question:
    def __init__(self, question="", answer="", pts=0, daily_double=False) -> None:
        self.question = question
        self.answer = answer
        self.points = pts
        self.is_daily_double = daily_double
        self.already_answered = False
    
    def mark_as_answered(self):
        self.already_answered = True