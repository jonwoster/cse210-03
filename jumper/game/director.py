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
        self._secret_word = Word_Generator().generate_word()
        #could be assigned here or in the method
        self._user_guess = ""
        self._hidden_word ="_"* len(self._secret_word)
        
        #update through capture_guess?

    def start_game(self):
        """starts and runs the main game loop until 'self._is_playing' becomes false."""
        while self._is_playing:
            self.display_status()
            self.do_update()
            # self.capture_guess()
            
    # def secret_word(self):
    #     word = Word_Generator()
    #     self._secret_word = word.generate_word()
    
    def display_status(self):
        
        self._show_word = self._evaluate_guess.get_word_printout(self._secret_word, self._user_guess, self._hidden_word)
        self._terminal_service.write_text(f"\n{self._show_word}\n")
        self._image = self._evaluate_guess.get_jumper_image(self._user_guess, self._secret_word)
        self._terminal_service.write_text(f"{self._image}")
        self._hidden_word = self._show_word

    def capture_guess(self):
        self._user_guess = self._terminal_service.read_letter("Guess a letter [a-z]: ")
    
    def do_update(self):
        """Sends guess info to 'Evaluate_guess and recieves the updated image and word string. Then sends results to 'Terminal_service' to be displayed."""
        # guess = Evaluate_guess()
        if '_' not in self._hidden_word:
            self._win = self._terminal_service.write_text(f"\nYou found the word: {self._secret_word}.\nThe jumper has landed safely!\nThanks for playing!\n")
            self._is_playing = False
            
        elif 'x' in self._image:
            self._lose = self._terminal_service.write_text(f"\nThe word was {self._secret_word}.\nThe jumper did not land safely!\nGame Over.\nThanks for playing!\n")
            self._is_playing = False
            
            
        else:
            self._is_playing = True
            self.capture_guess()
        # img = guess.get_jumper_image(self._user_guess, self._secret_word)
        # word_print = guess.get_word_printout()
        #will need to send this to the terminal_service

    


