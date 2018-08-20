# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/Lao/Dropbox/Coding/Python/6.00.1x/words.txt"

# secretWord = 'hallellujah'
global mistakesMade
mistakesMade = 0
lettersGuessed = []

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded. \n"
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
    if len(secretWord) == 1:
        if secretWord[0] in lettersGuessed:
            return True
        else:
            return False
    elif(secretWord[0] in lettersGuessed):
            return isWordGuessed(secretWord[1:], lettersGuessed)
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    GuessedWord = ''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            GuessedWord += secretWord[i] 
        else:
             GuessedWord += ' _ '
    return GuessedWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = string.ascii_lowercase
    
    for i in availableLetters:
        if i in lettersGuessed:
            availableLetters = availableLetters.replace(i, '')
    return availableLetters
    

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
    global mistakesMade
    while mistakesMade < 8:
        attempts_left = 8 - mistakesMade
        print 'You have %i guesses left.' % (attempts_left)
    
    # print available letters
        availableLetters = getAvailableLetters(lettersGuessed)
        print 'Available letters: %s' %  availableLetters 
    
    #get guess and check correct input
        guess = raw_input("Please guess a letter:")
        guess = guess.lower()
        if guess in lettersGuessed:
            guess = raw_input("Oops. You've already guessed that letter:")
            guess = guess.lower()
        
        if guess in secretWord:
            lettersGuessed.append(guess)
            GuessedWord = getGuessedWord(secretWord, lettersGuessed)
            won = isWordGuessed(secretWord, lettersGuessed)
            if won:
                print GuessedWord
                return True
            print 'Good guess: % s' % GuessedWord
        else:
            lettersGuessed.append(guess)
            mistakesMade += 1
            GuessedWord = getGuessedWord(secretWord, lettersGuessed)
            print 'Oops. This letter is not in my word: %s' % GuessedWord
    
    return False     
     





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()


print 'Welcome to the game, Hangman!'
print 'I am thinking of a word that is %i letters long. \n' % len(secretWord)

won = hangman(secretWord)
if won:
    print 'Congratulations, you won!'
else:
    print 'Sorry, you ran out of guesses. The word was %s' % secretWord
