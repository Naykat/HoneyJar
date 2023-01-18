#LTL encryption
import sys
sys.path.append('..')
from Utilities.utils import RaiseTypeError, RaiseValueError, bSet
from Bin.symbols import symbols

class LTL(): #this class helps to code messages in a several ways
    def __init__(self, alphabet: str = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()}{[]"№%:,.;_+-=/?\|±§<>'0123456789 ⠀''') -> None:
        
        if  not(type(alphabet) == str):
            currentType = getType(alphabet)
            RaiseTypeError('string', 'str', currentType)
        
        self.__alphabet = bSet(alphabet)
        self.__symbols = symbols
        
        self.__coding_dict = {}
        self.__decoding_dict = {}
        for letter in range(len(self.__alphabet)):
            
            self.__coding_dict[self.__alphabet[letter]] = self.__symbols[letter]
            self.__decoding_dict[self.__symbols[letter]] = self.__alphabet[letter]
            
    def encode(self, string: str) -> str: 
        if not(type(string) == str):
            currentType = getType(string)
            RaiseTypeError('string', 'str', currentType)
        result = ''
        for letter in range(len(string)):
            if string[letter] in self.__coding_dict:
                result+=self.__coding_dict[string[letter]]
            else:
                raise ValueError(f'Key letter ({string[letter]}) does not exist in alphabet')
        return result


    def decode(self, string: str) -> str: 
        if not(type(string) == str):
            currentType = getType(string)
            RaiseTypeError('string', 'str', currentType)
        result = ''
        for letter in range(len(string)):
            result+=self.__decoding_dict[string[letter]]
        return result

