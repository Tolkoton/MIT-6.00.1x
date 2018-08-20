# -*- coding: utf-8 -*-
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
n = HAND_SIZE
WORDLIST_FILENAME = "/Users/Tolk/Dropbox/Coding/Python/6.00.1x/ProblemSet4/words.txt"

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

hand =  {'a': 2, 'p': 2, 'r': 1, 'z': 1, 'e': 1}


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded.\n"
    return wordList


wordList = loadWords()


def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    sum = 0
    for i in hand:
        sum += hand[i]
    return sum


def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    #print                               # print an empty line


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = dict.copy(hand)
    
    for i in word:
        if i in new_hand.keys():
            if new_hand[i] != 0:
                new_hand[i] -= 1
            elif new_hand[i] == 0:
                del new_hand[i]
                
    
    return new_hand


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    sum = 0
    result = 0
    
    for i in word:
        if i in SCRABBLE_LETTER_VALUES:
            sum += SCRABBLE_LETTER_VALUES.get(i)
        
    if len(word) == n:
        result = n * sum + 50
    else:
        result = len(word) * sum
    
    return result
    

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    score = 0
    total = 0
    validWord = False
    new_hand = dict.copy(hand)
    lettercount = 0
    n = calculateHandlen(new_hand)
    hand_view = ''
     
    while True:   
        
        print
        print 'Current hand:',
        displayHand(new_hand)
        word = raw_input("Enter your or  word '.' to indicate that you are finished:")
        
        if word == '.':
            break
        
        # check if word exists
        if word in wordList:
            validWord = True  
        
        #print 'Word in wordlist:', (word in wordList)  
            
        #check if all used letters are in hand
        for letter in word:
            if letter not in new_hand:
                validWord = False  
          
        if len(word) == 1:
            validWord = False
            
        if validWord == False:    
            print 'Invalid word, please try again \n'
                         
        if validWord == True:
            # count wordscore and display new hand
            score = getWordScore(word, n)
            total += score 
            print '"%s" earned %i points. Total: %i' % (word, score, total)
            new_hand = updateHand(new_hand, word)
            
            
            #check if all letters are used
            lettercount += len(word)
            if lettercount == n:
                break        
   
    if lettercount == n:
        print 'Run out of letters. Total score: %i points' % total
    else:
        print 'Goodbye! Total score: %i points.' % total
    return         
        
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    command = ''
     
    while True:
    #get input
         command = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')   
    
    #check: in handlen == 0 print havent played yet
    #check: if unknown output: reenter letter
         if command == 'n':
             
    #if n: dealHand, playHand
    #if r: playHand
    
    #if e: print thanks, quit
            
         