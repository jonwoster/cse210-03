import random

class Word_Generator:
    """Generates a secret word
    
    It randomly picks a word from a list for a secret word that the player has to guess.
    
    
    ****Attributes:
        _word_list (list of str): The list of words to choose a secret word from.
        _word (str): The word chosen from the word list for the secret word.

    """

    def __init__(self):
        """Constructs a new Word_Generator.

        Args:
            self (Word_Generator): An instance of Word_Generator.
        """
        # Sets up the list of words from which the secret word will come from
        self._word_list = ["apple","arm","ball","banana","bat","bed","bike","bird","book","boy","bun","cake","can","cap","car","cat","chin","clam","class","clover","club","corn","cow","crayon","crib","crow","crowd","crown","cub","cup","dad","day","desk","dime","dirt","dog","doll","dress","dust","fan","fang","feet","field","flag","flower","fog","game","girl","gun","hall","hat","heat","hen","hill","home","horn","hose","jar","joke","juice","kite","lake","maid","man","map","mask","meal","meat","men","mice","milk","mint","mom","moon","morning","mother","name","nest","nose","pan","pear","pen","pencil","pet","pie","pig","plant","pot","rain","rat","river","road","rock","room","rose","seed","shape","shoe","shop","show","sink","snail","snake","snow","soda","sofa","son","star","step","stew","stove","straw","string","summer","sun","swing","table","tank","team","tent","test","toe","toes","tree","tub","van","vest","water","wing","winter","woman","women"]

    def _generate_word(self):
        # This method generates the secret word by choosing from a list of words
        # Returns self._word
        
        # Randomly select one of the words in the word list
        self._word = random.choice(self._word_list)
        return self._word

