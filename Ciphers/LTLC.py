#LTL encryption
import sys
sys.path.append('..')
from Utilities.utils import RaiseTypeError, bSet, getType
from Data.constants import default_step

class LTLC(): #Letter-to-letter
    def __init__(self, step: int = default_step) -> None:
        if not(type(step) == int):
            currentType = getType(step)
            RaiseTypeError('step', 'int', currentType)

        #Constants
        self.__step = step

         
    def encode(self, string: str) -> str: 
        if not(type(string) == str):
            currentType = getType(string)
            RaiseTypeError('string', 'str', currentType)
        step = self.__step
        letters = bSet(string)
        result = ''
        for symbol in string:
            encoded_symbol = letters[(letters.index(symbol)+step)%len(letters)]
            result+=encoded_symbol
        return result[::-1]


    def decode(self, string: str) -> str:
        string = string[::-1]
        if not(type(string) == str):
            currentType = getType(string)
            RaiseTypeError('string', 'str', currentType)
        step = self.__step
        letters = bSet(string)
        result = ''
        for symbol in string:
            encoded_symbol = letters[(letters.index(symbol)-step)%len(letters)]
            result+=encoded_symbol
        return result


