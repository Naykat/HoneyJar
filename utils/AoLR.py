#AoLR utilities
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
