from PIL import Image
from math import ceil

def get_type(var) -> str: #Gets the type of variable and returns it as a string
    v = str(type(var))
    pos1 = v.find("'")
    pos2 = v.rfind("'")
    v = v[pos1+1:pos2]
    return v

def remove_repeats(var: str or list) -> str or list: #Analogue to set(), but saves the order
    if type(var) is str:
        clean_string = ''
        for letter in var:
            if not(letter in clean_string):
                clean_string+=letter
        return clean_string

    elif type(var) is list:
        clean_array = []
        for item in var:
            if not(item in clean_array):
                clean_array.append(item)
        return clean_array
    
    else:
        currentType = getType(var)
        RaiseTypeError('var', 'str or list', currentType)

def decode_position(string: str, alphabet: str) -> int: 
        res = alphabet.find(string[-1])
        rounds = int(string[:-1])
        position = rounds*len(alphabet)+res
        return position

def find_char_position(string: str) -> str: 
    digits = '0123456789'
    letter = 0
    while string[letter] in digits:
        letter+=1
    return string[:letter+1]

def split_by_unique_letters(string: str) -> list: 
    array= []
    for string_with_letter_positions in range(string.count(' ')):
        array.append(string[:string.find(' ')])
        string = string[string.find(' ')+1:]
    return array

def return_char_by_position(dictionary: dict, pos: int, alphabet: str) -> str:
    for letter in alphabet:
        if pos in dictionary[letter]:
            char = letter
            break    
    return char        

def sum_strings_lengths(dictionary: dict, alphabet: str) -> int:
    amount = 0
    for letter in alphabet:
        amount+=len(dictionary[letter])
    return amount

def swap_string(string: str, swap_step: int) -> list:
  array = []
  for gap in range(0,len(string),swap_step):
    array.append(string[:swap_step])
    string = string[swap_step:]
  return array

def swap_letters(string: str):
  if len(string)==1:
    return string
  else:
    return string[-1]+string[1:-1]+string[0]

def calculate_image_size(text: str) -> tuple:
    if len(text)<=12:
        return 4,3
    else:
        y = int((len(text)/4*3)**0.5)
        x = int(ceil(y/3)*4)
        if x*y>=len(text):
            return x,y
        else:
            while x*y<len(text):
                y+=1
            return x,y
        
    
def from_letter_to_rgb(letter: chr) -> tuple:
    letter = ord(letter)+1
    return letter%255, letter//255, 255-letter%255 

def get_current_pixel_position(index: int, width: int) -> tuple:
    x = index%width
    y = index//width
    return x, y

def decode_pixel(pixel: tuple):
    r,g = pixel[:2]
    return chr(g*255+r-1)
