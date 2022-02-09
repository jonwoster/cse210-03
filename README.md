# cse210-03
Team 6- Thursday 7PM
Contributors are: Monika Meyers, Camron Erickson, Arnaldo Suarez, Jonathan Woster
Team assignment- Jumper game

## Description:
- This is a simple interactive game where a user guesses whether a card will be higher or lower than the current card shown. This project was created for CSE 210 at BYU Idaho.

Within the cse210-03 repository there is this README file, a design file with internal team notes, and the jumper folder.

Within the jumper folder, there is:
- __main__.py which utilizes classes in different files
- game folder, which contains the files with various classes

Within the game folder, there is:
- director.py, which has the Director class
- terminal_service.py, which has the Terminal_service class
- evaluate_guess.py, which has the Evaluate_guess class
- word_generator.py, which has the Word_Generator class

## Technologies Used:
- The only software required for this program is Python. You can download it here: https://www.python.org
- The collaboration was done via github: https://github.com/jonwoster/cse210-03

## Game Instructions:
The puzzle is a secret word randomly chosen from a list.
The player guesses a letter in the puzzle.
If the guess is correct, the letter is revealed along with any remaining hidden characters
If the guess is incorrect, a line is cut on the player's parachute.
If the puzzle is solved the game is over and the player is informed that they were successful.
If the player has no more parachute (too many incorrect guesses), the game is over. The player is informed that they lost.