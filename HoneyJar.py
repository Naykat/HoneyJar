from Ciphers.AOL import AOL
from Ciphers.LTL import LTL

class HoneyJar():

    def __init__(self, alphabet: str = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()}{[]"№%:,.;_+-=/?\|±§<>'0123456789 ⠀''') -> None:
        #Protected variable. Can be called, but not changed outside the class
        self._alphabet = alphabet 

        #Private variables. Cannot be called or changed outside the class
        self.__Encryption1 = AOL(self._alphabet)
        self.__Encryption2 = LTL(self.__Encryption1.encode(self._alphabet))

    def encrypt(self, string: str) -> str:
        string = self.__Encryption1.encode(string)
        string = self.__Encryption2.encode(string)
        return string
        
    def decrypt(self, string: str) -> str:
        string = self.__Encryption2.decode(string)
        string = self.__Encryption1.decode(string)
        return string

cm = HoneyJar('qwerty')
lt = HoneyJar('qwertty')
cm.encrypt
       

        
        
