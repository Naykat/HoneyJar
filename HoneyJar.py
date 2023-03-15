from Ciphers.AOL import AOL
from Ciphers.LTL import LTL
from Ciphers.SLC import SLC
from Data.constants import *

class HoneyJar():

    def __init__(self, alphabet: str = default_alphabet) -> None:
        #Protected variable. Can be called, but not changed outside the class
        self._alphabet = alphabet 

        #Private variables. Cannot be called or changed outside the class
        self.__Encryption1 = AOL(self._alphabet)
        self.__Encryption2 = LTL(int(len(self._alphabet)**0.5))
        self.__Encryption3 = SLC()

    def prepare(self, string: str) -> str:
        string = self.__Encryption1.encode(string)
        string = self.__Encryption2.encode(string)
        string = self.__Encryption3.encode(string)
        return string
        
    def unbar(self, string: str) -> str:
        string = self.__Encryption3.decode(string)
        string = self.__Encryption2.decode(string)
        string = self.__Encryption1.decode(string)
        return string

       

        
        
