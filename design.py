"""
The program must include a README file.
The program must remain true to game play described in the overview.
The program must include class and method comments.
The program must have at least four classes.

The parachute will be part of a list with 5 strings in it 
The person is also in the list and is made of 3 strings

Will use encapsulation by using "_" in front of attribute names (such as self._attribute) 
    to prevent classes from changing each others attributes directly. Data passed into 
    and out of classes to be done using arguments and return statements.

__main__.py will be in jumper folder, will call the Director class -Jonathan to create main, done
jumper folder will have a game folder
game folder will have:
    director.py (with Director class in it)  -Camron to create the file
    evaluate_guess.py (with Evaluate_guess class in it)  -Jonathan to create the file
    terminal_service.py (with Terminal_service class in it)  -Arnaldo to create the file
    word_generator.py (with Word_generator class in it) -Monika to create the file

Director class
    
    Director attributes: - Camron
    self._secret_word = WordGenerator().create_word()
    self._is_playing = True
    self._terminal_service = TerminalService()

     Methods:
    start_game(self)  - Camron
	(loop through methods)
  
    secret_word method which will call Word_generator class to get secret word-  Monika

    capture_guess(self)  - Arnaldo
	    guess = self._terminal_service.read_guess()

    do_update method will use Evaluate_guess class  - Camron

    display_status method which will use Terminal_service class to show the - Arnaldo
        remaining blanks and any correctly guessed letters
        what is left of the parachute and the person

Evaluate_guess class - Jonathan
    Gets the guess and secret word and guess count from Director via arguments
    Checks the guess against the secret word
    get_jumper_image(self, user_guess, secret_word)   Updates the string to remove lines from the parachute list if needed
        and returns self._jumper_image
    def get_word_printout()    returns the word to shows proper spaces and letters self._word_printout
    
    Returns updated list for parachute and returns the updated string for the word
    
Terminal_service class - Arnaldo
    set it up like input and output from seeker game
    * Not sure how it will handle multi-line strings like parachute & the person?
    
Word_generator class  -Monika
    self._words = [*this will be the list of words Monika has]
    generate_word(self)
	    word_index = random.randint(1,len(self.words))
	    return self.words[word_index]

"""