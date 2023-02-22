#AOL encryption
import sys
sys.path.append('..')
from Utilities.utils import RaiseTypeError, getType, bSet, findPos, createStringToDecode, createArrayWithDividedEncodedLetters, getLetter, getCharPos, getStringLength

class AOL():
    def __init__(self, alphabet: str = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()}{[]"№%:,.;_+-=/?\|±§<>'0123456789  ⠀''') -> None:
        if not(type(alphabet) == str):
            currentType = getType(alphabet)
            RaiseTypeError('string', 'str', currentType)
        alphabet = alphabet.replace(' ','⠀').replace('0','௦').replace('1','௧').replace('2','௨').replace('3','௩').replace('4','௪').replace('5','௫').replace('6','௬').replace('7','௭').replace('8','௮').replace('9','௯')
        
        #Constant
        self.__alphabet = bSet(alphabet)
        
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
        string = ' '+string
        string = string[::-1]
        lap = {}
        symbols = createArrayWithDividedEncodedLetters(string)
        
        for letter in range(len(symbols)):
            alphabet+=symbols[letter][0]
        for letter in range(len(symbols)):
            current_string = symbols[letter]
            current_letter = getLetter(current_string)
            current_string = current_string[1:]
            array_with_places = []
            while current_string!='':
                ministring = createStringToDecode(current_string)
                letter_pos = findPos(ministring, self.__alphabet)
                array_with_places.append(letter_pos)
                current_string = current_string.replace(ministring,'',1)
            lap[current_letter] = array_with_places
        result = ''
        for letters in range(getStringLength(lap, alphabet)):
            result+=getCharPos(lap, letters, alphabet)
       
        result = result.replace(' ','⠀').replace('௦','0').replace('௧','1').replace('௨','2').replace('௩','3').replace('௪','4').replace('௫','5').replace('௬','6').replace('௭','7').replace('௮','8').replace('௯','9')
        
        return result
