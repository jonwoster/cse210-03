from game.evaluate_guess import Evaluate_guess
from game.terminal_service import Terminal_service
from game.word_generator import Word_Generator

class Director:
    """This class is where the main sequence of the game takes place by incorporating the other classes in the program."""
    
    def __init__(self):
        """Creates a new Director and sets the necessary attributes"""
        self._is_playing = True
        self._terminal_service = Terminal_service()
        self._evaluate_guess = Evaluate_guess()
        self._secret_word = Word_Generator().generate_word()

        # initialize user_guess
        self._user_guess = ""
        # setup hidden_word to show underscores representing the number of letters in the word
        self._hidden_word ="_"* len(self._secret_word) 
    

    def start_game(self):
        """starts and runs the main game loop until 'self._is_playing' becomes false.
        Returns nothing"""

        while self._is_playing:
            self._display_status()
            self._do_update()

    
    def _display_status(self):
        # This method uses methods of evaluate_guess and terminal_service classes to show
        # the word that has been guessed so far and the image of the parachute & jumper
        # Returns nothing.

        # Get the word with letters and/or underscores from evaluate guess
        self._show_word = self._evaluate_guess.get_word_printout(self._secret_word, self._user_guess, self._hidden_word)
        # Print out the word with letters and/or underscores using terminal service
        self._terminal_service.write_text(f"\n{self._show_word}\n")
        
        # Get the image of the parachute and jumper from evaluate guess
        self._image = self._evaluate_guess.get_jumper_image(self._user_guess, self._secret_word)
        # Print out the image of the parachute and jumper using terminal service
        self._terminal_service.write_text(f"{self._image}")

        # Update the hidden word to be what came from evaluate guess
        self._hidden_word = self._show_word

    def _capture_guess(self):
        # This method sends a question to terminal_service to get the guessed letter from the user
        # Returns nothing.
        self._user_guess = self._terminal_service.read_letter("Guess a letter [a-z]: ")
    
    def _do_update(self):
        # This method checks to see if the player won, lost, or should keep going
        # Returns nothing.
        
        # if there are no more underscores in the hidden word, declare victory and set flag to stop playing
        if '_' not in self._hidden_word:
            self._win = self._terminal_service.write_text(f"\nYou found the word: {self._secret_word}.\nThe jumper has landed safely!\nThanks for playing!\n")
            self._is_playing = False
        
        # if the jumper's head is an x (because they lost their whole parachute), let user know they did not land safetly
        # and set flag to stop playing
        elif 'x' in self._image:
            self._lose = self._terminal_service.write_text(f"\nThe word was {self._secret_word}.\nThe jumper did not land safely!\nGame Over.\nThanks for playing!\n")
            self._is_playing = False
        
        # If they didn't win or lose yet, keep playing
        else:
            self._is_playing = True
            self._capture_guess()

    


