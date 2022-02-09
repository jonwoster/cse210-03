

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
        self._jumper_image = ["  ___", " /___\\", " \\   / ", "  \\ / ", '   O', "  /|\\", "  / \\", " ", "~~~~~~~~" ] 

        
        

    def get_jumper_image(self, user_guess, secret_word):
        """Receives the guess and the secret word from Director class
            Checks the guess against the secret word
            Updates the string to remove lines from the parachute list if needed
            Updates the word to shows proper spaces and letters
            Returns updated list for parachute and returns the updated string for the word
        
        Returns:
            list: the parachute and jumper strings (the GUI representation)
        """
        self._picture = ""
        self._guess = user_guess.lower()  # make sure the guess is lower case
        self._secret_word = secret_word.lower()  # make sure the secret word is lower case
        
        if self._jumper_image[0] != '   x':
            # Count how many times the guessed letter is in the secret word
            self._occurences = self._secret_word.count(self._guess)

            if self._occurences == 0 and len(self._jumper_image) == 6:
                self._jumper_image.pop(0)
                self._jumper_image.pop(0)
                self._jumper_image.insert(0,'   x')

            # if the letter that was guessed is not in self._secret_word
            elif self._occurences == 0:
                # then remove the first item in self._jumper_image
                self._jumper_image.pop(0)

            # if the letter that was guessed is in self._secret_word then loop through to replace blanks with letters
            # elif self._occurences > 0:
            #     # then update the self._word_printout
            #     list_of_occurences = []
            #     for pos,char in enumerate(self._secret_word):
            #         if(char == self._guess):
            #             list_of_occurences.append(pos)

        for i in self._jumper_image:
            self._picture += i +'\n'

        # print(f"Debugging: jumper image from within Evaluate_guess is {self._jumper_image}") # for debugging
        # send the jumper image list of strings back to the calling function/class
        return self._picture

    def get_word_printout(self, secret_word, guess, hidden_word):
        # stuff goes here
        self._word_printout = "" 
        self.letter_list = list(hidden_word.replace(" ",""))
        """Checks the word to see is the letter guessed is in the word."""

        
        if guess in secret_word:
            for i in range(0,len(secret_word)):
                letter = secret_word[i]
                if guess == letter:
                    self.letter_list.insert(i, guess)
                    self.letter_list.pop(i+1)
                # elif self.letter_list[i] == :
                #     self.letter_list.append("-")
        for i in self.letter_list:
            self._word_printout += i + " "




        # print(f"Debugging: word_printout from wihtin get_word_printout is {self._word_printout}") # for debugging
        return self._word_printout