from utils.general import *
from utils.SPoL import *
from utils.AoLR import *
from utils.txt2pixels import *
from utils.RSA import *
from bin.default_values import *


#Amount of Letter Repeats
class AoLR():
    def __init__(self, alphabet: str = default_alphabet) -> None:
        if type(alphabet)!=str:
            raise TypeError(f"alphabet must be str, not {get_type(alphabet)}")
        alphabet = alphabet.replace(' ','⠀').replace('0','௦').replace('1','௧').replace('2','௨').replace('3','௩').replace('4','௪').replace('5','௫').replace('6','௬').replace('7','௭').replace('8','௮').replace('9','௯')
        self.__alphabet = remove_repeats(alphabet)
        
    def encode(self, string: str) -> str:
        if type(string)!=str:
            raise TypeError(f"string must be str, not {get_type(string)}")
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
        if type(string)!=str:
            raise TypeError(f"string must be str, not {get_type(string)}")
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


#Rivest, Shamir and Adleman
class RSA:
    def __init__(self, p: int, q: int) -> None:
        if p == q:
            raise ValueError("p and q values must be different!")
        elif not is_prime(p):
            raise ValueError(f"{p} is not prime number!")
        elif not is_prime(q):
            raise ValueError(f"{q} is not prime number!")
        else:
            n = p * q
            phi = (p-1) * (q-1)
            e = random.randrange(1, phi)
            g = gcd(e, phi)
            while g != 1:
                e = random.randrange(1, phi)
                g = gcd(e, phi)
            d = mod_inverse(e, phi)
            self.__public_key, self.__private_key = (e, n), (d, n)


    def encode(self, pk: tuple, text: str) -> str:
        key, n = pk
        cipher = [(ord(char) ** key) % n for char in text]
        return cipher

    def decode(self, pk: tuple, text: str) -> str:
        key, n = pk
        plain = [chr((char ** key) % n) for char in text]
        return ''.join(plain)

    def get_private_key(self) -> tuple:
        return self.__private_key

    def get_public_key(self) -> tuple:
        return self.__public_key


#Swap Pairs of Letters
class SPoL():
    def __init__(self, limit: int = default_limit):
        if type(limit)!=int:
            raise TypeError(f"limit must be int, not {get_type(limit)}")
        self.__limit = limit

    def encode(self, string: str) -> str:
        if type(string)!=str:
            raise TypeError(f"string must be str, not {get_type(string)}")
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
        if type(string)!=str:
            raise TypeError(f"string must be str, not {get_type(string)}")
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


#Vigenere Cipher Implementation
class VCI:
    def __init__(self, key: str):
        self.__key = key

    def encode(self, text: str):
        ciphertext = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                char = char.upper()
                key_char = self.__key[key_index % len(self.__key)].upper()
                shift = ord(key_char) - ord('A')
                char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                key_index += 1
            ciphertext += char
        return ciphertext

    def decode(self, text: str):
        plaintext = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                char = char.upper()
                key_char = self.__key[key_index % len(self.__key)].upper()
                shift = ord(key_char) - ord('A')
                char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                key_index += 1
            plaintext += char
        return plaintext

        
#Letter to Letter Change
class LtLC(): 
    def __init__(self, step: int = default_step) -> None:
        if type(step)!=int:
            raise TypeError(f"step must be int, not {get_type(step)}")
        self.__step = step
   
    def encode(self, string: str) -> str:
        if type(string)!=str:
            raise TypeError(f"string must be str, not {get_type(string)}")
        step = self.__step
        letters = remove_repeats(string)
        result = ''
        for symbol in string:
            encoded_symbol = letters[(letters.index(symbol)+step)%len(letters)]
            result+=encoded_symbol
        return result[::-1]

    def decode(self, string: str) -> str:
        if type(string)!=str:
            raise TypeError(f"string must be str, not {get_type(string)}")
        string = string[::-1]
        step = self.__step
        letters = remove_repeats(string)
        result = ''
        for symbol in string:
            encoded_symbol = letters[(letters.index(symbol)-step)%len(letters)]
            result+=encoded_symbol
        return result


#Text to pixels
def to_pixels(string: str) -> Image:
    if type(string)!=str:
        raise TypeError(f"string must be str, not {get_type(string)}")
    width, height = calculate_image_size(string)
    image = Image.new("RGB", (width,height))

    for index, letter in enumerate(string):
        x, y = get_current_pixel_position(index, width)
        image.putpixel((x, y),from_letter_to_rgb(letter))
    return image


#Pixels to text
def to_string(image: str or Image) -> str:
    if type(image)==Image.Image:
        pass
    elif type(image)==str:
        image = Image.open(image)
    else:
        raise TypeError(f"image must be str or Image, not {get_type(image)}")
    index = 0
    string = ""
    
    width, height = image.size
    while True:
        x, y = get_current_pixel_position(index, width)
        if (x+1)*(y+1)<width*height:
            if image.getpixel((x,y))==(0,0,0):
                break
            current_pixel = image.getpixel((x,y))
            string += decode_pixel(current_pixel)
            index+=1
        else:
            last_pixel = image.getpixel((x,y))
            string += decode_pixel(last_pixel)
            break
    return string
