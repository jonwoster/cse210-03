

    
class Evaluate_guess:

    """Evaluates the guess
    
    The responsibility of the Evaluate_guess class is to 
        Gets the guess and secret word from Director via arguments
        Checks the guess against the secret word
        Updates the string to remove lines from the parachute list if needed
        Updates the word to shows proper spaces and letters
        Returns updated list for parachute and returns the updated string for the word
    
    Attributes:
        ???
    """

    def __init__(self):
        """Constructs a new Evaluate_guess

        Args:
            self (Seeker): An instance of Evaluate_guess
        """
        # list of strings to represent the parachute and jumper
        self._jumper_image = ["  ___", " /   \\", "  ___", " \\   / ", "  \\ / ", '   O', "  /|\\", "  / \\", " ", "~~~~~~~~" ]  
    
    def get_jumper_image(self, user_guess, secret_word, guess_number):
        """Receives the guess and the secret word from Director class
        
            Checks the guess against the secret word
            Updates the string to remove lines from the parachute list if needed
            Updates the word to shows proper spaces and letters
            Returns updated list for parachute and returns the updated string for the word
        
        Returns:
            list: the parachute and jumper strings (the GUI representation)
        """
        self._guess = user_guess
        self._secret_word = secret_word
        self._guess_number = guess_number

        return self._jumper_image

    def get_word_printout():
        # stuff goes here
        return self._word_printout