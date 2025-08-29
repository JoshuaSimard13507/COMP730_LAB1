"""
File: src/Riddle.py
Contains the Riddle class for managing riddles and their answers.
Author: Joshua Simard
Created: 8/27/25
Developer: Joshua Simard
Date: 8/29/25

This class provides methods to load riddles from a file, select a random riddle,
and check user answers for correctness. Each riddle and its answer are stored
in the Riddles.txt file, separated by a "%" symbol.
"""

import random

class Riddle:
    """
    Riddle class for managing riddles and their answers.
    This class provides methods to load riddles from a file.
    Instance variables
        riddles: list of riddles loaded from a file
        riddle: current riddle
        answer: current answer
    """
    def __init__(self, file):
        """
        Loads riddles from a specified file, then selects a random riddle.
        """
        self.riddles = self.load_riddles(file)
        self.riddle = None
        self.answer = None
        self.get_riddle()

    def __str__(self):
        """
        Returns a string representation of the current riddle.
        """
        return f"Riddle: {self.riddle}"
    
    def get_riddle(self):
        """
        Selects a random riddle from the list of riddles.
        Also sets the current answer.
        """
        self.riddle = random.choice(self.riddles)
        self.answer = self.riddle[1]
        self.riddle = self.riddle[0]
    
    def check_answer(self, user_answer):
        """
        Checks if the user's answer is correct.
        Returns True or False.
        """
        return user_answer.strip().lower() == self.answer.lower()
    
    def load_riddles(self, file):
        """
        Loads riddles from a specified file.
        Each line in the file should contain a riddle and its answer, separated by a "%" symbol.
        Returns a list of [riddle, answer] pairs.
        """
        riddles = []
        with open(file, 'r') as f:
            for line in f:
                parts = line.strip().split('%')
                riddles.append(parts)
        return riddles

        