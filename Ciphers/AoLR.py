#AoRL encryption
import sys
sys.path.append('..')
from Utilities.utils import remove_repeats, decode_position, find_char_position, split_by_unique_letters, return_char_by_position, sum_strings_lengths
from Utilities.constants import default_alphabet

class AoLR():
    def __init__(self, alphabet: str = default_alphabet) -> None:
        
        alphabet = alphabet.replace(' ','⠀').replace('0','௦').replace('1','௧').replace('2','௨').replace('3','௩').replace('4','௪').replace('5','௫').replace('6','௬').replace('7','௭').replace('8','௮').replace('9','௯')
        self.__alphabet = remove_repeats(alphabet)
        
    def encode(self, string: str) -> str:
        string = string.replace(' ','⠀').replace('0','௦').replace('1','௧').replace('2','௨').replace('3','௩').replace('4','௪').replace('5','௫').replace('6','௬').replace('7','௭').replace('8','௮').replace('9','௯')
        result = ''
        alphabet = self.__alphabet
        for letter in range(len(alphabet)):
            if string.count(alphabet[letter])!=0:
                result+=alphabet[letter]   
                currentString = string
                numbers = ''
                for repeats in range(string.count(alphabet[letter])):
                    letter_index = currentString.rfind(alphabet[letter])
                    whole_number = letter_index//len(alphabet)
                    res = letter_index%len(alphabet)
                    result+=str(whole_number)+alphabet[res]
                    currentString = currentString[:letter_index] 
                result+=' '
        result = result[:-1]
        result = result[::-1]
        return result
    
    def decode(self, string: str) -> str:
        alphabet = ''
        string = string[::-1]+' '
        lap = {}
        symbols = split_by_unique_letters(string)
        for letter in symbols:
            alphabet+=letter[0]
        for letter, current_string in enumerate(symbols):
            array_with_positions = []
            current_letter = current_string[0]
            current_string = current_string[1:]
            while current_string!='':
                encoded_position = find_char_position(current_string)
                letter_pos = decode_position(encoded_position, self.__alphabet)
                array_with_positions.append(letter_pos)
                current_string = current_string.replace(encoded_position,'',1)
            lap[current_letter] = array_with_positions
        result = ''
        for letters in range(sum_strings_lengths(lap, alphabet)):
            result+=return_char_by_position(lap, letters, alphabet)
       
        result = result.replace(' ','⠀').replace('௦','0').replace('௧','1').replace('௨','2').replace('௩','3').replace('௪','4').replace('௫','5').replace('௬','6').replace('௭','7').replace('௮','8').replace('௯','9')
        
        return result
