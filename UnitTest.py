"""
File: src/UnitTest.py
Implements unit tests for the Riddle Problem.
Author: Joshua Simard
Created: 8/27/25
Developer: Joshua Simard
Date: 8/29/25

This module tests loading riddles from a file, selecting random riddles,
and checking user answers for correctness. It uses a temporary riddles file
for testing purposes.
"""

import unittest
from Riddle import Riddle

class TestRiddle(unittest.TestCase):
    """
    Unit tests for the Riddle class.
    Tests loading riddles, selecting random riddles, and checking answers.
    instance variables
        riddle_obj: instance of Riddle class
    """

    def setUp(self):
        """
        Sets up a Riddle object for testing.
        """
        self.riddle_obj = Riddle("Riddles.txt")

    def test_load(self):
        """
        Test that the Riddle object can correclty establish a new Riddle object.
        """
        self.riddle_obj.get_riddle()
        self.assertIsNotNone(self.riddle_obj.riddle)
        self.assertIsNotNone(self.riddle_obj.answer)


    def test_check_answer_correct(self):
        """
        Test that check_answer returns True for correct answers.
        """
        self.assertTrue(self.riddle_obj.check_answer(self.riddle_obj.answer))

    def test_check_answer_incorrect(self):
        """
        Test that check_answer returns False for incorrect answers.
        """
        self.assertFalse(self.riddle_obj.check_answer("wrong answer^^"))

if __name__ == "__main__":
    """
    Runs the Unit Tests.
    """
    unittest.main()

