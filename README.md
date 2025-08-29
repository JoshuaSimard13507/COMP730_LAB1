# COMP730_LAB1
In this implementation of the riddle program, we utilize a list of 99 riddles with their answers.
This list is divided, on each line, into a problem with a corresponding answer separated by a "%" marker.
Every time the 'game' is played, a call is made to the Riddle class which selects a random riddle and answer from the file.

## Usage
As many of these riddles are rather confusing, there is the option to use the 'hint' command to bypass having to actually guess.
You will only have one chance for each riddle. 
It is not case-sensitive.

## Unit Tests
The Unit tests can be run directly by running the 'UnitTest.py' file. 
These tests are comprehensive, and test if the Riddle file loads properly, if it returns True for a good answer, returns False for a bad answer, and is non-case sensitive.