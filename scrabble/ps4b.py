from ps4a import *
import time

def wordCheck(word, hand):
    """
    Returns True if word from wordList entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    new_hand = dict.copy(hand)
    
    if word == '':
        return False
    
    for i in word:
        if i not in hand:
            return False
            
    for i in word:
        if new_hand[i] < 1:
            return False
        else:
            new_hand[i] -= 1
        
    return True
    
#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0

    # Create a new variable to store the best word seen so far (initially None)  
    best_word = 'None'
   
    # For each word in the wordList
    for word in wordList:
        x = wordCheck(word, hand) 
        if x == True:
            if getWordScore(word, n) > max_score:
                max_score = getWordScore(word, n)
                best_word = word
    return best_word           
       
       


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    
    new_hand = dict.copy(hand)
    #new_hand = {'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}
    score = 0
    total = 0
    n = calculateHandlen(new_hand)
    
    while True:
        
        #display hand and computer chooses a word.
        word = compChooseWord(new_hand, wordList, n)
     
        
        x = calculateHandlen(new_hand)      
        if x != 0:
            print 'Current hand:',
            displayHand(new_hand)
        
        if len(word) == n:
            score = getWordScore(word, n)
            total += score
            print '"%s" earned %i points. Total: %i points \n' % (word, score, total)
            print 'Total score:', total
            return
                       
        if word not in wordList:
            print 'Total score:', total
            return
    
        score = getWordScore(word, new_hand)
        total += score
        print '\n "%s" earned %i points. Total: %i points \n' % (word, score, total)
        
        new_hand = updateHand(new_hand, word)
    

# Choose if a computer or human plays       
def who_plays(hand, n, wordList):
   
    while True:
        who_plays = raw_input('Enter u to have yourself play, c to have the computer play:')
    
        if who_plays == 'u':
            playHand(hand, wordList, n)
            return
        elif who_plays == 'c':
            compPlayHand(hand, wordList, n)
            return
        else:
            print 'Invalid command'
    
    return  
    
     
       
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    command = ''
    n = HAND_SIZE
    hand_check = 1
     
    while True:
    #get input
         command = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')   
    
    #check: in handlen == 0 print havent played yet
    #check: if unknown output: reenter letter
    #if n: dealHand, playHand
    #if r: playHand    
    #if e: print thanks, quit
         if command == 'n':
             hand = dealHand(n)
             who_plays(hand, n, wordList)
         elif command == 'r':
             try:
                 x = hand
             except UnboundLocalError:
                 print 'You have not played a hand yet. Please play a new hand first!'
             else:
                 who_plays(hand, n, wordList)
         elif command == 'e':
             return
         else:
             print 'Invalid command'
             

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


