import random

class Riddle:
    def __init__(self, file):
        self.riddles = self.load_riddles(file)
        self.riddle = None
        self.answer = None
        self.get_riddle()

    def __str__(self):
        return f"Riddle: {self.riddle}"
    
    def get_riddle(self):
        self.riddle = random.choice(self.riddles)
        self.answer = self.riddle[1]
        self.riddle = self.riddle[0]
    
    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.answer.lower()
    
    def load_riddles(self, file):
        riddles = []
        with open(file, 'r') as f:
            for line in f:
                parts = line.strip().split('%')
                riddles.append(parts)
        return riddles

        