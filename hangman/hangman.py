# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    flag=1
    for a in secretWord :
        if a in lettersGuesed :
            flag=1
        else :
            break
    if flag==1 :
        return True
    else :
        return False
         

	

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
      return example: '_ p p _ _'
    '''
    
    
    
    
    result=""
    secretWord_1 = secretWord
    for x in secretWord_1 :
        result+="_"
    
    l=list(result)
    
    for x in lettersGuessed :
        for letters in secretWord_1 :
            if x==letters :
                p = secretWord_1.index(letters)
                l[p]=x
                secretWord_2=secretWord_1
                l1 = list(secretWord_2)
                l1[p] = '_'
                secretWord_2 = ''.join(l1)
                secretWord_1 = secretWord_2
                result=''.join(l)
                    
    
            
    return result
            
          

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    remaining=""
    
    for x in secretWord :
        if x not in lettersGuessed :
            remaining+=x
            
    return remaining
    
    
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    length=len(secretWord)
    guessed_word = ''
    lettersGuessed=[]
    print("\nGUESS the SECRETWORD by using ALPHABETS")
    print("\nLength of the word is {} ".format(length))
    
    chances_left = 5
    
    while chances_left > 0 :
    
        char = input("\nEnter a character : ")
        lettersGuessed += char
        
        if char in secretWord :
            guessed_word = getGuessedWord(secretWord,lettersGuessed)
            print(guessed_word)
        else :
            chances_left -= 1
        
        if chances_left < 5 and chances_left > 0 :
            print("\nBUCK UP !! You have {} chances left . . " .format(chances_left))
        elif chances_left == 0 :
            print("\nSORRY !! You lost.......")
            
            print("\nThe SECRETWORD is {} ".format(secretWord))   
    
    if guessed_word == secretWord:
        print("\nCONGRATULATIONS!!!  You got the Secretword")
        
    else :
        print("\nTRY AGAIN\n")
       
    

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
 
 
 
