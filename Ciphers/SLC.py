import sys
sys.path.append("..")
from Utilities.utils import swap_string, swap_letters

class SLC():
    def __init__(self, limit: int = None):
        self.__limit = limit

    def encode(self, string: str) -> str:

        #Sets the number of "swaps"
        if self.__limit is None or self.__limit % len(string) == 0:
            limit = len(string)//2
        else:
            limit = self.__limit%len(string)
        
        for swap in range(2,limit):
            swapped_string = swap_string(string, swap)
            string = ""
            for element in swapped_string:
              string+=swap_letters(element)
        return string

    def decode(self, string: str) -> str:

        #Sets the number of "swaps"
        if self.__limit is None or self.__limit % len(string) == 0:
            limit = len(string)//2+1
        else:
            limit = self.__limit%len(string)+1
            
        for swap in range(2,limit):
            swapped_string = swap_string(string, limit-swap)
            string = ""
            for element in swapped_string:
                string+=swap_letters(element)
        return string

