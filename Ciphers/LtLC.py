#LTL encryption
import sys
sys.path.append('..')
from Utilities.utils import remove_repeats
from Utilities.constants import default_step

class LtLC(): #Letter-to-letter
    def __init__(self, step: int = default_step) -> None:
        
        self.__step = step

         
    def encode(self, string: str) -> str: 
        
        step = self.__step
        letters = remove_repeats(string)
        result = ''
        for symbol in string:
            encoded_symbol = letters[(letters.index(symbol)+step)%len(letters)]
            result+=encoded_symbol
        return result[::-1]


    def decode(self, string: str) -> str:
        
        string = string[::-1]
        step = self.__step
        letters = remove_repeats(string)
        result = ''
        for symbol in string:
            encoded_symbol = letters[(letters.index(symbol)-step)%len(letters)]
            result+=encoded_symbol
        return result


