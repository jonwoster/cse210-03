from game.evaluate_guess import Evaluate_guess
from game.terminal_service import Terminal_service
from game.word_generator import Word_Generator

class Director:
    """This class will be where the main sequence of the game takes place by incorporating the other classes in the program."""
    def __init__(self):
        """Creates a new Director and sets the necessary attributes"""
        self._is_playing = True
        self._terminal_service = Terminal_service()
        self._evaluate_guess = Evaluate_guess()
        self._secret_word = ""
        #could be assigned here or in the method
        self._user_guess = ""
        #update through capture_guess?

    def start_game(self):
        """starts and runs the main game loop until 'self._is_playing' becomes false."""
        while self._is_playing:
            self.display_status()
            self.capture_guess()
            self.do_update()
            
    def secret_word(self):
        word = Word_Generator()
        self._secret_word = word.generate_word()
    
    def display_status(self):
        self._image = self._evaluate_guess.get_jumper_image(self._user_guess, self._secret_word)
        self._terminal_service.write_text(self._image)
    
    def capture_guess(self):
        self._user_guess = self._terminal_service.read_letter("Guess a letter [a-z]: ")
    
    def do_update(self):
        """Sends guess info to 'Evaluate_guess and recieves the updated image and word string. Then sends results to 'Terminal_service' to be displayed."""
        guess = Evaluate_guess()
        img = guess.get_jumper_image(self._user_guess, self._secret_word)
        word_print = guess.get_word_printout()
        #will need to send this to the terminal_service

    


