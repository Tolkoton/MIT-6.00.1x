import string

def build_shift_dict(self, shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
    
    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26
    Returns: a dictionary mapping a letter (string) to 
             another letter (string). 
    '''

    shift_dict = {}
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


    for i in letters:
        index = letters.index(i) + 1
        if index in range(27) and index + shift > 26:
            shift_dict[i] = letters[index + shift - 26 - 1]
        elif index in range(27, 53) and index + shift > 52:
            shift_dict[i] = letters[index + shift - 26 - 1]
        else:
            shift_dict[i] = letters[(index + shift - 1)]

    return shift_dict

    
def apply_shift(self, shift):
    '''
    Applies the Caesar Cipher to self.message_text with the input shift.
    Creates a new string that is self.message_text shifted down the
    alphabet by some number of characters determined by the input shift        
    
    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
    down the alphabet by the input shift
    '''

#message = 'abcz!, ZA'  
#shift = 3

shift_message = ''
shift_dict = build_shift_dict(message, shift) 

for i in message:
    if i in shift_dict:
        shift_message += shift_dict.get(i)
    else:
        shift_message += i
        
return shift_message
    
   