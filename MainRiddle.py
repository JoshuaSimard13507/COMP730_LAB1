"""
File: src/MainRiddle.py
Implements the main function of the Riddle Problem.
Author: Joshua Simard
Created: 8/28/25
Developer: Joshua Simard
Date: 8/28/25

This module contains the main logic for presenting and solving riddles.
It is designed for use in COMP730 Lab 1 and serves as the entry point
for riddle-related functionality.
"""

from Riddle import Riddle

def main():

    print("Enter 'hint' to see the answer.")

    riddle_obj = Riddle("Riddles.txt")
    riddle_obj.get_riddle()

    while True:
        print(riddle_obj)
        
        while True:
            user_answer = input("Your answer: ").strip().lower()
            if( user_answer == "hint" ):
                print(f"The answer is: {riddle_obj.answer}")
            elif ( user_answer == riddle_obj.answer.lower() ):
                print("Correct!")
                break
            else:
                print(f"Sorry, that's not right. The answer was \"{riddle_obj.answer}\"")
                break
        
        user_answer = input("Play again? [Y/N] ").strip().lower()
        if user_answer != 'y':
            print("Thanks for playing!")
            break
        riddle_obj.get_riddle()
            


if __name__ == "__main__":
    main()

