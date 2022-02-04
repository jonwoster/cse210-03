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

__main__.py will be in jumper folder, will call the Director class
jumper folder will have a game folder
game folder will have:
    director.py (with Director class in it)
    evaluate_guess.py (with Evaluate_guess class in it)
    terminal_service.py (with Terminal_service class in it)
    word_generator.py (with Word_generator class in it)

Director class
    start_game method
    initialize attributes needed for this class
    secret_word method which will call Word_generator class to get secret word
    capture_guess method which will use Terminal_service class to ask user for their guess
    do_update method will use Evaluate_guess class
    display_status method which will use Terminal_service class to show the 
        remaining blanks and any correctly guessed letters
        what is left of the parachute and the person

Evaluate_guess class
    Gets the guess and secret word from Director via arguments
    Checks the guess against the secret word
    Updates the string to remove lines from the parachute list if needed
    Updates the word to shows proper spaces and letters
    Returns updated list for parachute and returns the updated string for the word
    
Terminal_service class
    set it up like input and output from seeker game
    * Not sure how it will handle multi-line strings like parachute & the person?
    
Word_generator class
    initialize with list of words
    generate_word method to pick secret word 

"""