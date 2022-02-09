

class Evaluate_guess:

    """Evaluates the guess
        The responsibility of the Evaluate_guess class is to 
        Gets the guess and secret word from Director via arguments
        Checks the guess against the secret word
        Updates the string to remove lines from the parachute list if needed
        Updates the word to shows proper spaces and letters
        Returns updated list for parachute and returns the updated string for the word
    
    Attributes:
        
    """

    def __init__(self):
        """Constructs a new Evaluate_guess

        Args:
            self (Seeker): An instance of Evaluate_guess
        """
        # list of strings to represent the parachute and jumper
        self._jumper_image = ["  ___", " /   \\", "  ___", " \\   / ", "  \\ / ", '   O', "  /|\\", "  / \\", " ", "~~~~~~~~" ] 

        self._word_printout = ["- - - - - - word guessed so far will go here"] 
    
    def get_jumper_image(self, user_guess, secret_word, guess_number):
        """Receives the guess and the secret word from Director class
            Checks the guess against the secret word
            Updates the string to remove lines from the parachute list if needed
            Updates the word to shows proper spaces and letters
            Returns updated list for parachute and returns the updated string for the word
        
        Returns:
            list: the parachute and jumper strings (the GUI representation)
        """
        self._guess = user_guess.lower()  # make sure the guess is lower case
        self._secret_word = secret_word.lower()  # make sure the secret word is lower case
        self._guess_number = guess_number
        
        # Count how many times the guessed letter is in the secret word
        self._occurences = self._secret_word.count(self._guess)

        # if the letter that was guessed is not in self._secret_word
        if self._occurences == 0:
            # then remove the first item in self._jumper_image
            self._jumper_image.pop(0)

         # if the letter that was guessed is in self._secret_word then loop through to replace blanks with letters
        elif self._occurences > 0:
            # then update the self._word_printout
            list_of_occurences = []
            for pos,char in enumerate(self._secret_word):
                if(char == self._guess):
                    list_of_occurences.append(pos)


        print(f"Debugging: jumper image from within Evaluate_guess is {self._jumper_image}") # for debugging
        # send the jumper image list of strings back to the calling function/class
        return self._jumper_image

    def get_word_printout(self):
        # stuff goes here
        
        print(f"Debugging: word_printout from wihtin get_word_printout is {self._word_printout}") # for debugging
        return self._word_printout