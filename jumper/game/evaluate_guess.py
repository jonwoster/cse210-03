
class Evaluate_guess:

    """Evaluates the guess
        The responsibility of the Evaluate_guess class is to 
        Gets the guess and secret word from Director via arguments
        Checks the guess against the secret word
        Updates the string to remove lines from the parachute list if needed
        Updates the word to shows proper spaces and letters
        Returns updated image for parachute and returns the updated string for the word
    """

    def __init__(self):
        """Constructs a new Evaluate_guess

        Args:
            self: An instance of Evaluate_guess
        """
        # list of strings to represent the parachute and jumper
        self._jumper_image = ["  ___", " /___\\", " \\   / ", "  \\ / ", '   O', "  /|\\", "  / \\", " ", "~~~~~~~~" ] 


    def get_jumper_image(self, user_guess, secret_word):
        """Receives the guess and the secret word from Director class
            Checks the guess against the secret word
            Updates the list of strings to remove lines from the parachute list if needed
            Returns parachute image
        
        Returns:
            self._picture: the parachute and jumper image
        """
        self._picture = ""  # set this up as a blank string that will be modified in this method
        self._guess = user_guess.lower()  # make sure the guess is lower case
        self._secret_word = secret_word.lower()  # make sure the secret word is lower case
        
        #  Enter unless the jumper has already lost all pieces of their parachute
        if self._jumper_image[0] != '   x':

            # Count how many times the guessed letter is in the secret word
            self._occurences = self._secret_word.count(self._guess)

            # if the guess was wrong and the parachute has been exhausted, replace the jumper's head with an x
            if self._occurences == 0 and len(self._jumper_image) == 6:
                self._jumper_image.pop(0)
                self._jumper_image.pop(0)
                self._jumper_image.insert(0,'   x')

            # if the letter that was guessed shows 0 times in the secret word
            elif self._occurences == 0:
                # then remove the first item in self._jumper_image, to remove the next portion from parachute
                self._jumper_image.pop(0)

        # add line returns to have the image elements print on successive lines
        for i in self._jumper_image:
            self._picture += i +'\n'

        # send the jumper image list of strings back to the calling function/class
        return self._picture

    def get_word_printout(self, secret_word, guess, hidden_word):
        """Receives the hidden word string, the guess from user and the secret word from the calling class
            Checks the guess against the secret word
            Updates the hidden_word to show the right letters and dashes
            Returns the modified string to show what has been guessed so far
        
        Returns:
            self._word_printout  Which is the string that shows what letters have been guessed correctly
        """

        self._word_printout = "" # set this up as a blank string that will be modified in this method
        # Load the hidden word into letter_list
        self.letter_list = list(hidden_word.replace(" ",""))

        # If the guessed letter is in the secret word, loop through and put the right letter in the right spot
        if guess in secret_word:
            for i in range(0,len(secret_word)):
                letter = secret_word[i]
                if guess == letter:
                    self.letter_list.insert(i, guess)
                    self.letter_list.pop(i+1)
        
        # Loop through every item in letter_list to build string to print out for user
        for i in self.letter_list:
            self._word_printout += i + " "

        # Send the string back that will show the guessed letters and remaining underscores
        return self._word_printout